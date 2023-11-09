from fastapi import FastAPI
from fastapi.responses import StreamingResponse
from models import *
from cli import cli
from scrapper import read_content
from app import *
import json

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




@app.post("/process_url")
async def process_url(url: Url):  # Ensure that the Url model is properly defined
    # add data from url to data.txt
    # Replace this with your actual implementation
    read_content_obj = read_content()
    read_content_obj.scrape_website(url.url)

    # make connection using cookies
    # Ensure mcq_app and chatbot objects are correctly defined and imported
    app_obj = mcq_app()
    app_obj.get_data_from_file()

    # process the data in chunks
    total_size = len(app_obj.data)
    chunk_size = 50
    chunks = []
    last_ind = 0

    while last_ind < total_size:
        chunk = ' '.join(app_obj.data[last_ind:min(last_ind + chunk_size, total_size)])
        last_ind += chunk_size

        prompt = """
        Generate 1 mcq for, not too many nor too less for the following '
        """ + chunk + """
        'return list of json objects
        use json format for each mcq
        e.g.
        [{
            "Question": "Question",
            "Option1": "Option1",
            "Option2": "Option2",
            "Option3": "Option3",
            "Option4": "Option4",
            "Answer": "Answer with 10-20 length description"
        }]
        """

        try:
            query_result = str(app_obj.chatbot.query(prompt))  # Assuming this is an async function
            chunks.append(query_result)
        except Exception as e:
            print(f"Some error occurred while processing the data: {e}")
            continue
        print(query_result)
    # Convert the result to JSON and write it to the response in chunks
    async def stream_response():
        for chunk in chunks:
            yield chunk

    return StreamingResponse(stream_response(), media_type="plain/text")