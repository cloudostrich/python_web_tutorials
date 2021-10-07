from fastapi import FastAPI, WebSocket
from fastapi.responses import HTMLResponse

app = FastAPI()

html = """
<!DOCTYPE html>
<html>
    <head>
        <title>Binapi</title>
    </head>
    <body>
        <h1>Binapi Feed</h1>

        <div>
             <form action="" onsubmit="startfeed(event)">
            <input type="text" id="messageText" autocomplete="off"/>
            <button>Send</button>
        </form>
            <div id="livedata"></div>
        </div>
        <br/>
        <div>
        <form action="" onsubmit="sendMessage(event)">
            <input type="text" id="messageText" autocomplete="off"/>
            <button>Send</button>
        </form>
        <ul id='messages'>
        </ul>
        </div>
        <script>
            var ws = new WebSocket("ws://localhost:8000/ws");
            ws.onmessage = function(event) {
                var messages = document.getElementById('messages')
                var message = document.createElement('li')
                var content = document.createTextNode(event.data)
                message.appendChild(content)
                messages.appendChild(message)
            };
            function sendMessage(event) {
                var input = document.getElementById("messageText")
                ws.send(input.value)
                input.value = ''
                event.preventDefault()
            }
            function startfeed(event) {
                event.preventDefault()
            }
        </script>
    </body>
</html>
"""


uri = "wss://www.bitmex.com/realtime?subscribe=instrument:XBTUSD"

@app.get("/")
async def get():
    return HTMLResponse(html)

async def capture_data(wsw: WebSocket):
    uri = "wss://www.bitmex.com/realtime?subscribe=instrument:XBTUSD"
    async with wsw.connect(uri) as websocket:
        while True:
            data = await websocket.recv()
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
