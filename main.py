import logging
from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session
from sqlalchemy import Boolean, Column, Float, ForeignKey, Integer, String, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker


from schemas import ToolCreate, RentRequest, ReturnToolRequest

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

DATABASE_URL = "sqlite:///./rental.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()

class Tool(Base):
    __tablename__ = "tools"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    available = Column(Boolean, default=True)

class Rental(Base):
    __tablename__ = "rentals"
    id = Column(Integer, primary_key=True, index=True)
    tool_id = Column(Integer, ForeignKey("tools.id"))
    user_id = Column(Integer, index=True)
    days = Column(Integer)


Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/tools")
def get_tools(db: Session = Depends(get_db)):
    tools = db.query(Tool).filter(Tool.available == True).all()
    return tools

@app.post("/tools")
def add_tool(tool_data: ToolCreate, db: Session = Depends(get_db)):
    tool = Tool(name=tool_data.name)
    db.add(tool)
    db.commit()
    db.refresh(tool)
    return tool

@app.post("/rent")
def rent_tool(rent_data: RentRequest, db: Session = Depends(get_db)):
    tool = db.query(Tool).filter(Tool.id == rent_data.tool_id).first()
    if not tool.available:
        return {"message": "Tool not available"}
    rental = Rental(tool_id=rent_data.tool_id, user_id=rent_data.user_id, days=rent_data.days)
    tool.available = False
    db.add(rental)
    db.commit()
    db.refresh(rental)
    return rental

@app.post("/return")
def return_tool(request: ReturnToolRequest, db: Session = Depends(get_db)):
    tool = db.query(Tool).filter(Tool.id == request.tool_id).first()
    if tool.available:
        return {"message": "Tool already available"}
    tool.available = True
    db.commit()
    return {"message": "Tool returned"}

@app.get("/rentals")
def get_rentals(db: Session = Depends(get_db)):
    rentals = db.query(Rental).all()
    return rentals