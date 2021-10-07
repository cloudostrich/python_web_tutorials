from fastapi import FastAPI, WebSocket
from fastapi.responses import HTMLResponse
import websockets, json

app = FastAPI()


uri = "wss://www.bitmex.com/realtime?subscribe=instrument:XBTUSD"

@app.get("/")
async def get():
    return HTMLResponse(html)

async def capture_data():
    uri = "wss://www.bitmex.com/realtime?subscribe=instrument:XBTUSD"
    async with websockets.connect(uri) as wsc:
        while True:
            data = await wsc.recv()
            data = json.loads(data)
            try :
                #print('\n', data['data'][0]["lastPrice"])
                print('\n', data)
                return data
            except KeyError:
                continue

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    
    await websocket.accept()
    while True:
        data = await websocket.receive_text()
        await websocket.send_text(f"Message text was: {data}")
