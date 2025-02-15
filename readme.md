# FastAPI Tool Rental API  

This is a simple **Tool Rental API** built with **FastAPI** and **SQLite**.  
Users can **add**, **rent**, **return**, and **view tools** using this API.  

## 🚀 Features  
- 📜 **Get available tools** (`GET /tools`)  
- ➕ **Add a new tool** (`POST /tools`)  
- 🔄 **Rent a tool** (`POST /rent`)  
- ✅ **Return a tool** (`POST /return`)  
- 📂 **View all rentals** (`GET /rentals`)  

---

## 🏗️ Installation  

### 1️⃣ Clone the repository  
```bash
git clone https://github.com/your-repo/tool-rental-api.git
cd tool-rental-api
```

### 2️⃣ Create and activate a virtual environment (optional but recommended)  
```bash
python -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate  # On Windows
```

### 3️⃣ Install dependencies  
```bash
pip install -r requirements.txt
```

### ⚡ Running the API  
```bash
uvicorn main:app --reload
```
The API will be available at: **http://127.0.0.1:8000**

---

## 📌 API Endpoints  

### 🔍 Get Available Tools  
**GET /tools**  
Response: List of available tools  
```json
[
  {
    "id": 1,
    "name": "Hammer",
    "available": true
  }
]
```

### ➕ Add a New Tool  
**POST /tools**  
Request Body:  
```json
{
  "name": "Drill"
}
```
Response:  
```json
{
  "id": 2,
  "name": "Drill",
  "available": true
}
```

### 🔄 Rent a Tool  
**POST /rent**  
Request Body:  
```json
{
  "tool_id": 1,
  "user_id": 101,
  "days": 5
}
```
Response:  
```json
{
  "id": 1,
  "tool_id": 1,
  "user_id": 101,
  "days": 5
}
```

### ✅ Return a Tool  
**POST /return**  
Request Body:  
```json
{
  "tool_id": 1
}
```
Response:  
```json
{
  "message": "Tool returned"
}
```

### 📂 Get All Rentals  
**GET /rentals**  
Response:  
```json
[
  {
    "id": 1,
    "tool_id": 1,
    "user_id": 101,
    "days": 5
  }
]
```

---

## 🛠️ Tech Stack  
- **FastAPI** 🚀 (Web framework)  
- **SQLite** 🗄️ (Database)  
- **SQLAlchemy** 🛢️ (ORM)  
- **Pydantic** ✅ (Data validation)  
- **Uvicorn** 🌐 (ASGI server)  
```

