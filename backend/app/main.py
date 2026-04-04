from fastapi import FastAPI,HTTPException,WebSocket,WebSocketDisconnect
from app.manager import ConnectionManager
from pydantic import BaseModel
from app.auth import hash_password,verify_password,create_token,decode_token
app=FastAPI()
fake_db={}
manager=ConnectionManager()

class RegisterRequest(BaseModel):
    username: str
    password: str
class LoginRequest(BaseModel):
    username: str
    password: str
@app.get("/")
def root():
    return {"message": "Polo is alive"}
            
@app.post("/register")
def register(req:RegisterRequest):
    if req.username in fake_db:
        raise HTTPException(status_code=400, detail="Username already exists")
    fake_db[req.username] = hash_password(req.password)
    return {"message": "User registered successfully"}

@app.post("/login")
def login(req:LoginRequest):
    if req.username not in fake_db:
         raise HTTPException(status_code=400, detail="User not found") 
    if not verify_password(req.password,fake_db[req.username]):
        raise HTTPException(status_code=400, detail="Wrong Password") 
    token = create_token({"sub": req.username})
    return {"access_token": token, "token_type": "bearer"}
@app.websocket("/ws/{room_id}")
async def connect(websocket:WebSocket,room_id:str):
    await manager.connect(websocket,room_id)
    try:
        while True:
            data=await websocket.receive_text()
            await manager.broadcast(data, room_id)
    except WebSocketDisconnect:
       manager.disconnect(websocket,room_id)
    