from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from manager import WebSocketManager

app = FastAPI()
manager = WebSocketManager()

@app.get("/")
def read_root():
    return {"message": "Hello World"}
