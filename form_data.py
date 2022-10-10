from fastapi import FastAPI,Form

app=FastAPI()

@app.post('/login/')
async def login(username:str=Form(),password:str=Form()):
    return {'username':username,'password':password}

@app.post('/register/')
async def register(name:str=Form(),age:int=Form(),adress:str=Form(),city:str=Form(),pwd:str=Form()):
    resp={'name':name,'age':age,'adress':adress,'city':city,'pwd':pwd}
    return resp