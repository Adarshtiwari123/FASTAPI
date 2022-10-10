from  fastapi import FastAPI
from typing import Union
from enum import Enum
my_app=FastAPI()

@my_app.get('/helo')
async def help():
    resp={'hello':'worlddd'}
    return resp

@my_app.get('/item/{item_id}')
async def read(item_id):
    resp={'item_id':'foo'}
    return resp
@my_app.get('/indexx/{item_id}')
async def indexx(item_id:int):
    resp={'item_id':item_id}
    return resp
@my_app.get('/user/me')
async def hellp():
    return {'user_id':'the current user'}

@my_app.get('/user/{id}')
async def help(id:str):
    return {'id':id}
@my_app.get('/user')
async def user():
    resp=['hello','world']
    return resp
@my_app.get('/user')
async def user2():
    resp=['hiii','byyy']
    return resp



"""
class fruits(str,Enum):
    mango="mango"
    banana='banana'
    apple="apple"
@my_app.get('/models/{model_name}')
async def desi(model_name:fruits):
    if model_name.value=="mango":
        resp={'model_name': model_name,"msg":"mango are come to july" }
        return resp
    elif model_name.value =="banana":
        resp={'model_name':model_name,"msg":"banana comes to every season"}
        return resp
    else:
        return {'model_name':model_name,"msg":"they are heavy season fruits"} """


class Modelname(str,Enum):
    autumn="Autumn"
    summer="Summer"
    winter="Winter"
@my_app.get('/models/{model_name}')
async def help_data(model_name:Modelname):
    if model_name is Modelname.autumn:
        resp={'model_name':model_name,"msg":"you are in autumn season"}
        return resp
    elif model_name.value == "Summer":
        return {'model_name':model_name,"msg":"hello you are in summer season"}
    else:
        return {'model_name':model_name,"msg":"heyy fuck off winter"}


    """  QUERY PARAMETER STARTED HERE    """ 
item_db=[{'item_name':"heyy"},{'item_name':'world'},{"item_name":'adarsh'}]
@my_app.get('/items/') 
async def hello_query(skip :int=0,limit :int =10):
    return item_db[skip : skip + limit]      




data_db=[{'data1':'good'},{'data1':"morning"},{'data1':'buddy'},{'data1':"adarsh"},{'data1':'tiwari'}]
@my_app.get('/data/')
async def helooop(welcome:int=0,query:int=10):
    return data_db[welcome:welcome + query]