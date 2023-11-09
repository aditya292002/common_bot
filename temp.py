from hugchat import hugchat
from hugchat.login import Login
from cli import *
from icecream import ic
import json
# function
# read data.txt in chucks and append result to list of jsons
# return the result
mcqs = []

client = cli()
email = client.cookies_file_name
cookie_path_dir = "."
sign = Login(email, None)
cookies = sign.loadCookiesFromDir(cookie_path_dir) # This will detect if the JSON file exists, return cookies if it does and raise an Exception if it's not.

# Create a ChatBot
chatbot = hugchat.ChatBot(cookies=cookies.get_dict())  # or cookie_path="usercookies/<email>.json"


def process_mcq():
    data = []
    with open("data.txt", "r") as f:
        for line in f:
            data.extend(line.split(' '))
    total_size = len(data)
    last_ind = 0
    chuck_size = 400 # 400 words per chuck
    while(last_ind < total_size):
        chunk = ' '.join(data[last_ind: last_ind + chuck_size])
        last_ind += chuck_size
        
        prompt = """
        Generate appropiate number of mcq for, not too many nor too less for the following '
        """ + chunk + """
        'return list of json objects
        use json format for each mcq
        e.g.
        [{
            "Question": "Question",
            "Option1" : "Option1",
            "Option2" : "Option2",
            "Option3" : "Option3",
            "Option4" : "Option4",
            "Answer" : "Answer with 10-20 length description"
        }]
        """

        query_result = str(chatbot.query(prompt))
        print(query_result)
        print(type(query_result))

        start , end = 0, 0
        for i, e in enumerate(query_result):
            if e == '[':
                start = i
            if e == ']':
                end = i
                break

        query_result = query_result[start:end+1]
        query_result = json.loads(query_result)  # Parse the JSON string into a list

        mcqs.extend(query_result)



process_mcq()



