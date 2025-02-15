from pydantic import BaseModel

class ToolCreate(BaseModel):
    name: str

class RentRequest(BaseModel):
    tool_id: int
    user_id: int
    days: int

class ReturnToolRequest(BaseModel):
    tool_id: int