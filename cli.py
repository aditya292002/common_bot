import os
from hugchat import hugchat
from hugchat.login import Login
from models import *

class cli:
    def __init__(self):
        self.cookies_available = False
        self.cookies_file_name = None
        self.get_cookies_file()  # Corrected method call


    # method to get cookies file and update the class variables
    def get_cookies_file(self):
        current_directory = os.getcwd()
        file_list = os.listdir(current_directory)
        for file_name in file_list:
            if file_name.endswith('.json'):
                self.cookies_available = True
                self.cookies_file_name = file_name[:-5]
    
    def store_hugging_account_info(self, user_info: UserInfo):
        # Log in to huggingface and grant authorization to huggingchat
        email = user_info.email
        password = user_info.password
        sign = Login(email, password)
        cookies = sign.login()

        # Save cookies to the local directory
        cookie_path_dir = "."
        sign.saveCookiesToDir(cookie_path_dir)
        self.cookies_available = True

        self.get_cookies_file()  