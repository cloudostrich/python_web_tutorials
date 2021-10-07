from fastapi import FastAPI, WebSocket 
from enum import Enum
import websockets, json

# example of using enums
class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"

# instantiate fastapi app
app = FastAPI()

# root endpoint
@app.get("/")
async def root():
    return {"message" : "Hello World"}

@app.get("/getdata")
async def getdata():
    uri = "wss://www.bitmex.com/realtime?subscribe=instrument:XBTUSD"
    # ws = WebSocket(uri)
    async with websockets.connect(uri) as wsc:
        while True:
            data = await wsc.recv()
            data = json.loads(data)
            try :
                #print('\n', data['data'][0]["lastPrice"])
                print('\n', data)
            except KeyError:
                continue

# type check input
@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}

# test enum endpoint
@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name == ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}

    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}

    return {"model_name": model_name, "message": "Have some residuals"}

# file path endpoint
@app.get("/files/{file_path:path}")
async def read_file(file_path: str):
    return {"file_path": file_path}

# fake items for query params eg
fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]

# query params
@app.get("/items/")
async def read_item(skip: int=0, limit: int=10):
    return fake_items_db[skip: skip + limit]
