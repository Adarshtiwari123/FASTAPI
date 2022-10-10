from fastapi import FastAPI
from typing import Union

app=FastAPI()

@app.get('/')
async def root():
    resp={'hello':'world'}
    return resp

@app.post('/help/{item_id}')
async def help(item_id:int,name:str,address:str):
    resp={'item_id':item_id,'name':name,'address':address}
    return resp

@app.get('/index/')
def hl(id:int,q:Union[str, None]=None):
    res={'id':id,'q':q}
    return res


@app.post('/op/{id}')
async def  cry(id:int,name:str,address:str,age:int,height:float,married:bool):
    resp={'id':id,'name':name,'address':address,'age':age,'height':height,'married':married}
    return resp