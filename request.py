
from tkinter.messagebox import NO, RETRY
from fastapi import FastAPI
from pydantic import BaseModel

request_app=FastAPI()

class Item(BaseModel):
    name: str
    description:str | None=None
    price:float
    tax :float | None= None


@request_app.post('/update')
#@app.post("/items/")
async def update_item(item: Item):
    item_dict = item.dict()
    if item.tax:
        price_with_tax = item.price + item.tax
        item_dict.update({"price_with_tax": price_with_tax})
    return item_dict




@request_app.post('/items/')
async def create_item(item:Item):
    return item


class Food(BaseModel):
    name:str
    type: str | None=None
    description: str | None=None
    rate:float
    quantity: float |None =None

@request_app.post('/foody')
async def hey(food:Food):
    resp=food.description.casefold()
    return resp

class unknown(BaseModel):
    name:str
    description:str |None =None
    price:float
    tax:float |None =None  
@request_app.put('/unknown_data/{item_id}')
async def un(item_id:int,item:unknown):
    return {'item_id':item_id,**item.dict()}



@request_app.put('updated_data_by_put_method/{item_id}')
async def put_item_update(item_id: int, item: Item, q: str | None = None):
    result = {"item_id": item_id, **item.dict()}
    if q:
        result.update({"q": q})
    return result