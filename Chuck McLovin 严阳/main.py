from fastapi import FastAPI, WebSocket
from typing import List

app = FastAPI()

class ConnectionManager:
    def __init__(self):
        self.active_connections = []

    async def connect(self, websocket: WebSocket, username: str):
        await websocket.accept()
        self.active_connections.append((username, websocket))

    def disconnect(self, websocket: WebSocket):
        for connection in self.active_connections:
            if connection[1] == websocket:
                self.active_connections.remove(connection)
                break

    async def broadcast(self, message: str, sender_username: str):
        for connection in self.active_connections:
            if connection[0] != sender_username:
                await connection[1].send_text(f"{sender_username}: {message}")

manager = ConnectionManager()

@app.websocket("/ws/{username}")
async def websocket_endpoint(websocket: WebSocket, username: str):
    await manager.connect(websocket, username)
    try:
        while True:
            data = await websocket.receive_text()
            await manager.broadcast(data, username)
    except WebSocketDisconnect:
        manager.disconnect(websocket)
