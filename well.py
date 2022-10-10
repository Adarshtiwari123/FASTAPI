from email.headerregistry import Address
from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel

app=FastAPI()
@app.get('/')
def help():
    resp={'heyy':'world'}
    return resp

"""@app.put('/welcome/{item_id}')
def welcome(item_id:int):
    resp={'item_id':item_id}
    return resp

@app.put('/done/{item_id}')
def done(item_id:int,item_name:str):
    resp={'item_id':item_id,'item_name':item_name}
    return resp

@app.put('/honey/{roll_no}')
def honey(roll_no:int,name:str,age:int,height:float):
    resp={'roll_no':roll_no,'name':name,'age':age,'height':height}
    return resp




class Item(BaseModel):
    name:str
    price:float
    age:int
    Address=str
    is_offer:Union[bool,None] =None

@app.put('database/{item_id}')
def update_item(item_id:int,item :Item):
    resp={'item_id':item_id,"item_name":item.name}
    return resp

@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}
"""
