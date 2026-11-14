from fastapi import FastAPI, WebSocket, WebSocketDisconnect


app = FastAPI()


@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):

    await websocket.accept()

    try:
        while True:
            # Receive message from client
            message = await websocket.receive_text()

            print(f"Client says: {message}")

            # Send message back to client
            await websocket.send_text(
                f"Server received: {message}"
            )

    except WebSocketDisconnect:
        print("Client disconnected")
