import websockets
import asyncio
import json

async def capture_data():
    uri = "wss://www.bitmex.com/realtime?subscribe=instrument:XBTUSD"
    async with websockets.connect(uri) as websocket:
        while True:
            data = await websocket.recv()
            data = json.loads(data)
            try :
                #print('\n', data['data'][0]["lastPrice"])
                print('\n', data)
            except KeyError:
                continue


asyncio.get_event_loop().run_until_complete(capture_data())
