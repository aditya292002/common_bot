from hugchat import hugchat
from hugchat.login import Login

class hugChat:
    def openConnection():
        cookie_path_dir = "."
        # code to find .json file in current directory
        # pass the file in Login()
        sign = Login("keshariaditya90@gmail.com", None)
        cookies = sign.loadCookiesFromDir(cookie_path_dir) # This will detect if the JSON file exists, return cookies if it does and raise an Exception if it's not.

        # Create a ChatBot
        chatbot = hugchat.ChatBot(cookies=cookies.get_dict())  # or cookie_path="usercookies/<email>.json"

        
        # non stream response
        query_result = chatbot.query("Hi!")
        print(query_result) # or query_result.text or query_result["text"]
