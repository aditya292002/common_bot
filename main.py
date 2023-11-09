from fastapi import FastAPI
from models import *
from cli import cli
from scrapper import read_content
from app import *

app = FastAPI()


@app.get("/")
async def root():   
    return {"message": "Hello World"}



# endpoints to handle your hugging face account info
@app.get("/login")
async def check_user_info():
    client = cli()
    if(client.cookies_available):
        return {"status": "successful", "message": "User information is already available."}
    else:
        return {"status": "unsuccessful", "message": "you can use post req. to same endpoint to save your info"}
        


# use this endpoint to add new info or add a info
@app.post("/login")
async def add_user_info(user_info: UserInfo):
    client = cli()
    return client.store_hugging_account_info(user_info)



#  "get route" to get url and process it
@app.post("/process_url")
async def process_url(url: Url):
    # add data from url to data.txt
    read_content_obj = read_content()
    read_content_obj.scrape_website(url.url)
    
    # process the data in chunks of 400 words
    app_obj = mcq_app()  # Renamed to avoid conflict with the 'app' variable
    app_obj.get_data_from_file()
    app_obj.process()
    return {
        "status": "successful",
        "mcq" : app_obj.mcqs
    }

    

#  "get route" to get the pdf and handle it 