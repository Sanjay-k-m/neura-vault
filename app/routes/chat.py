from fastapi import APIRouter, WebSocket

router = APIRouter()

@router.websocket("/ws/{user_id}")
async def websocket_chat_endpoint(websocket: WebSocket, user_id: str):
    await websocket.accept()
    print("Client connected ✅")
    try:
        while True:
            
            data = await websocket.receive_text()
            await websocket.send_text(f'{data} got it')
    except Exception as e:
        print(f"Client disconnected ❌: {e}")
        await websocket.close()