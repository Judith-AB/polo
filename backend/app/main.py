from fastapi import FastAPI,HTTPException,WebSocket,WebSocketDisconnect,Depends
from fastapi.middleware.cors import CORSMiddleware
from app.manager import ConnectionManager
from pydantic import BaseModel
from app.auth import hash_password,verify_password,create_token,decode_token
from app.database import engine,get_db,SessionLocal
from sqlalchemy.orm import Session


app=FastAPI()
from app import models
models.Base.metadata.create_all(bind=engine)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
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

def register(req: RegisterRequest, db: Session = Depends(get_db)):
    if db.query(models.User).filter(models.User.username == req.username).first():
        raise HTTPException(status_code=400, detail="Username already exists")
    new_user = models.User(username=req.username, password=hash_password(req.password))
    db.add(new_user)
    db.commit()
    return {"message": "User registered successfully"}

@app.post("/login")
def login(req: LoginRequest, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.username == req.username).first()
    if not user:
        raise HTTPException(status_code=400, detail="User not found")
    if not verify_password(req.password, user.password):
        raise HTTPException(status_code=400, detail="Wrong Password")
    token = create_token({"sub": req.username})
    return {"access_token": token, "token_type": "bearer"}
@app.websocket("/ws/{room_id}")
async def connect(websocket: WebSocket, room_id: str, token: str):
    try:
        username = decode_token(token)['sub']
    except:
        await websocket.close(code=1008)
        return
    await manager.connect(websocket, room_id)
    try:
        while True:
            data = await websocket.receive_text()
            
            # Save message to database
            db = SessionLocal()
            try:
                new_message = models.Message(
                    room_id=room_id,
                    username=username,
                    content=data,
                    status="sent"
                )
                db.add(new_message)
                db.commit()
            finally:
                db.close()
            
            await manager.broadcast(f"{username}: {data}", room_id)
    except WebSocketDisconnect:
        manager.disconnect(websocket, room_id)
@app.get("/messages/{room_id}")
def getallmessage(room_id:str,db:Session=Depends(get_db),):
    return db.query(models.Message).filter(models.Message.room_id == room_id).all()