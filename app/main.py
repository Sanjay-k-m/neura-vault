from fastapi import FastAPI,WebSocket
from contextlib import asynccontextmanager
from app.routes import chat_router

# Lifespan context manager for startup/shutdown
@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup: Initialize database, vector store, etc.
    print("Starting up: Initializing resources...")
    # Example: Initialize vector store connection
    yield
    # Shutdown: Clean up resources
    print("Shutting down: Cleaning up resources...")

app = FastAPI(title="Neura vault Backend", version="1.0.0", lifespan=lifespan)

app.include_router(chat_router, prefix="/chat", tags=["chat"])


@app.get("/")
async def root():
    return {"message": "neura vault server is running ✅"}


@app.websocket("/ws/health")
async def websocket_health_check(websocket: WebSocket):
    await websocket.accept()
    print("Health check connected ✅")
    try:
        await websocket.send_text("WebSocket alive")
        await websocket.close()
        print("Health check completed ✅")
    except Exception as e:
        print(f"Health check failed ❌: {e}")