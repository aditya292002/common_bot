import json
from models import UserInfo

class cli:
    def __init__(self):
        self.user_info_available = False
        try:
            with open('cookies.jsonl', 'r') as f:
                if f.read().strip():
                    self.user_info_available = True
        except FileNotFoundError:
            pass

    def store_hugging_account_info(self, user_info: UserInfo):
        try:
            with open('cookies.jsonl', 'w') as f:
                f.write(json.dumps(user_info.dict()) + '\n')
            return {"status": "Successful", "message": "User info added successfully"}
        except Exception as e: #file writing exception 
            return {"status": "unsuccessful", "message": "some error occured while performing writing operation: " + str(e)}