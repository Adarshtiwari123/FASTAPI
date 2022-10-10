from fastapi import FastAPI
from typing import Union

app=FastAPI()

@app.get('/')
def hello():
    resp={'hello':'world'}
    return resp
