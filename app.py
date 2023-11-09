from hugchat import hugchat
from hugchat.login import Login
from cli import *
import json


class mcq_app:
    def __init__(self):
        self.mcqs = []
        self.data = []
        # make connection using cookies
        self.client = cli()
        self.email = self.client.cookies_file_name
        self.cookie_path_dir = "."
        self.sign = Login(self.email, None)
        self.cookies = self.sign.loadCookiesFromDir(self.cookie_path_dir)

        # Create a ChatBot
        self.chatbot = hugchat.ChatBot(cookies=self.cookies.get_dict())

    # get the data from data.txt to data list
    def get_data_from_file(self):
        with open("data.txt", "r") as f:
            for line in f:
                self.data.extend(line.split(' '))

    # process the data in chunks of 400 words
    def process(self):
        total_size = len(self.data)
        last_ind = 0
        chuck_size = 400    
        while(last_ind < total_size):
            chunk = ' '.join(self.data[last_ind: last_ind + chuck_size])
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

            query_result = str(self.chatbot.query(prompt))


            start , end = 0, 0
            for i, e in enumerate(query_result):
                if e == '[':
                    start = i
                if e == ']':
                    end = i
                    break
            self.mcqs.extend(json.loads(query_result[start:end+1]))