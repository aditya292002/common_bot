from fastapi import FastAPI
from models import UserInfo
from cli import cli
import json
app = FastAPI()


@app.get("/")
async def root():   
    return {"message": "Hello World"}


# endpoints to handle your hugging face account info
@app.get("/login")
async def check_user_info():
    client = cli()
    if(client.user_info_available):
        return {"status": "successful", "message": "User information is already available."}
    else:
        return {"status": "unsuccessful", "message": "you can use post req. to same endpoint to save your info"}
        
# use this endpoint to add new info or add a info
@app.post("/login")
async def add_user_info(user_info: UserInfo):
    client = cli()
    return client.store_hugging_account_info(user_info)

# get route to accept and url and process it 
