from fastapi.websockets import WebSocket

class WebSocketManager:
    def __init__(self):
        self.connected_clients = []

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.connected_clients.append(websocket)
        print(f"Client {websocket.client.host}:{websocket.client.port} connected.")
        print(f"Total connections: {len(self.connected_clients)}")

    async def broadcast(self, message: str, sender: WebSocket):
        payload = {
            "client": f"{sender.client.host}:{sender.client.port}",
            "message": message
        }
        for client in self.connected_clients:
            try:
                await client.send_json(payload)
            except Exception:
                # Handle stale connections
                pass

    async def disconnect(self, websocket: WebSocket):
        if websocket in self.connected_clients:
            self.connected_clients.remove(websocket)
            print(f"Client {websocket.client.host}:{websocket.client.port} disconnected.")
            print(f"Total connections: {len(self.connected_clients)}")

