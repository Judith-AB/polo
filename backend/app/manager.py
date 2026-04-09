from fastapi import WebSocket
import redis.asyncio as aioredis
class ConnectionManager:
    def __init__(self,redis_url:str):
        self.rooms={}
        self.redis = aioredis.from_url(redis_url)
    async def connect(self,websocket:WebSocket,room_id:str):
        if room_id not in self.rooms:
            self.rooms[room_id]=[]
        self.rooms[room_id].append(websocket)
        await websocket.accept()
    def disconnect(self,websocket:WebSocket,room_id:str):
        self.rooms[room_id].remove(websocket)
    
    async def publish(self, message: str, room_id: str):
        await self.redis.publish(room_id, message)

    async def subscribe(self, room_id: str):
        pubsub = self.redis.pubsub()
        await pubsub.subscribe(room_id)
        return pubsub
     
            





