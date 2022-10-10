from tkinter.messagebox import RETRY
from fastapi import FastAPI,Cookie

app=FastAPI()
@app.get('/cookie/')
async def hello(as_id:str | None=Cookie(default=None)):
    return {'as_id':as_id}