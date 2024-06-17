from enum import Enum
from typing import Union
from fastapi import FastAPI

from pydantic import BaseModel


class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"


class Item(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    tax: Union[float, None] = None



app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

# fastapi dev tutorial.py

# Path Parameters¶
#@app.get("/items/{item_id}")
async def read_item(item_id):
    return {"item_id": item_id}

# Path parameters with types¶
@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}


# Order matters
@app.get("/users/me")
async def read_user_me():
    return {"user_id": "the current user"}


@app.get("/users/{user_id}")
async def read_user(user_id: str):
    return {"user_id": user_id}

@app.get("/users")
async def read_users():
    return ["Rick", "Morty"]


@app.get("/users")
async def read_users2():
    return ["Bean", "Elfo"]

"""
Order matters for route `/users`
The first one will always be used since the path matches first.
"""


# Predefined values
@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    # Compare enumeration members¶
    if model_name is ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}

    # Get the enumeration value
    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}

    # Return enumeration members
    return {"model_name": model_name, "message": "Have some residuals"}



# Query Parameters
fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]

@app.get("/items/")
async def read_item(skip: int = 0, limit: int = 10):
    return fake_items_db[skip : skip + limit]

"""
http://127.0.0.1:8000/items/?skip=0&limit=10
"""

# Optional parameters

#@app.get("/items/{item_id}")
async def read_item(item_id: str, q: Union[str, None] = None):
    if q:
        return {"item_id": item_id, "q": q}
    return {"item_id": item_id}

"http://127.0.0.1:8000/items/foo?q=1"


# Query parameter type conversion
#@app.get("/items/{item_id}")
async def read_item(item_id: str, q: Union[str, None] = None, short: bool = False):
    item = {"item_id": item_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update(
            {"description": "This is an amazing item that has a long description"}
        )
    return item

"""
http://127.0.0.1:8000/items/foo?short=1

http://127.0.0.1:8000/items/foo?short=True

http://127.0.0.1:8000/items/foo?short=true
"""

# Request Body
#@app.post("/items/")
async def create_item(item: Item):
    return item

# Use the model
"""
Inside of the function, you can access all the attributes of the model object directly:
"""

@app.post("/items/")
async def create_item(item: Item):
    item_dict = item.dict()
    if item.tax:
        price_with_tax = item.price + item.tax
        item_dict.update({"price_with_tax": price_with_tax})
    return item_dict


# Request body + path parameters
@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    return {"item_id": item_id, **item.dict()}
