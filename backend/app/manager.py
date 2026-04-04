from fastapi import WebSocket
class ConnectionManager:
    def __init__(self):
        self.rooms={}
    async def connect(self,websocket:WebSocket,room_id:str):
        if room_id not in self.rooms:
            self.rooms[room_id]=[]
        self.rooms[room_id].append(websocket)
        await websocket.accept()
    def disconnect(self,websocket:WebSocket,room_id:str):
        self.rooms[room_id].remove(websocket)
    async def broadcast(self,message:str,room_id:str):
        for i in self.rooms[room_id]:
            await i.send_text(message)
        
     
            





