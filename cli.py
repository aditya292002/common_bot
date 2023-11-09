import os
from hugchat import hugchat
from hugchat.login import Login

class cli:
    def __init__(self):
        self.cookies_available = False
        current_directory = os.getcwd()
        file_list = os.listdir(current_directory)
        for file_name in file_list:
            if file_name.endswith('.json'):
                self.cookies_available = True
        
        
    def store_hugging_account_info(self, user_info: UserInfo):
        # Log in to huggingface and grant authorization to huggingchat
        email = user_info.email
        password = user_info.password
        sign = Login(email, password)
        cookies = sign.login()
        # You might want to store the cookies for future use here