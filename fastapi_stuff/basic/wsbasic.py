import asyncio
import websockets

async def hello():
    uri ="wss://stream.binance.com:9443/ws/ethbusd@kline_1m" 
    async with websockets.connect(uri) as websocket:
        print("Getting Started Baby")
        async for message in websocket:
#            print(message)
            greeting = await message.recv()
            print(f"I GOT THIS: {greeting}")

if __name__ == "__main__":
    print("got the __name__")
    asyncio.get_event_loop().run_until_complete(hello())
