
'''
The maximum amount of context that HugChat can process or remember is not specified in the given information. It may depend on various factors such as the hardware and software used, the size of the memory available, and the complexity of the conversation being processed.

Sources:
Will upgrading my RAM and Processor speed up functions on QGIS Desktop 2.12.0? favicon
gis.stackexchange.com
RAM vs. Processor—Which Is More Important to Your Business? - Intel favicon
intel.com
[PDF] Processing-in-memory: A workload-driven perspective - Parallel Data Lab favicon
pdl.cmu.edu
'''



from icecream import ic
# from hugchat import hugchat
# from hugchat.login import Login

# check = 0
# try:
#     # Attempt to log in to Hugging Face
#     sign = Login("keshariaditya90@gmail.com", "Adikes209.")
#     cookies = sign.login()  # Assuming that 'login' is a method of the 'Login' class
#     check = 1
# except Exception as e:
#     # Handle exceptions that may occur during the login process
#     print(f"An exception occurred while logging in: {e}")
# else:
#     # Code to run when login is successful
#     print("Login successful")
#     # Grant authorization to Hugging Chat here



# # Code to run whether login succeeds or not
# print("Done1")

# if(check == 1):

#     # Save cookies to the local directory
#     cookie_path_dir = "./cookies_snapshot"
#     sign.saveCookiesToDir(cookie_path_dir)

#     # Load cookies when you restart your program:
#     # sign = login(email, None)
#     # cookies = sign.loadCookiesFromDir(cookie_path_dir) # This will detect if the JSON file exists, return cookies if it does and raise an Exception if it's not.

#     # Create a ChatBot
#     chatbot = hugchat.ChatBot(cookies=cookies.get_dict())  # or cookie_path="usercookies/<email>.json"

#     #
#     chatbot.switch_llm(3) # Switch to the second model

#     # non stream response
#     query_result = chatbot.query("hi")
#     print(query_result) # or query_result.text or query_result["text"]



# # stream response
# for resp in chatbot.query(
#     "Hello",
#     stream=True
# ):
#     print(resp)

# # Use web search (new feature)
# query_result = chatbot.query("Hi!", web_search=True)
# print(query_result) # or query_result.text or query_result["text"]
# for source in query_result.web_search_sources:
#     print(source.link)
#     print(source.title)
#     print(source.hostname)

# # Create a new conversation
# id = chatbot.new_conversation()
# chatbot.change_conversation(id)

# # Get conversation list
# conversation_list = chatbot.get_conversation_list()
# ic(conversation_list)

# # Get the available models (not hardcore)
# models = chatbot.get_available_llm_models()

# # Switch model to the given index
# chatbot.switch_llm(0) # Switch to the first model

# # Get information about the current conversation
# info = chatbot.get_conversation_info()
# print(info.id, info.title, info.model, info.system_prompt, info.history)

# # Get conversations on the server that are not from the current session (all your conversations in huggingchat)
# chatbot.get_remote_conversations(replace_conversation_list=True)

# # [DANGER] Delete all the conversations for the logged in user
# chatbot.delete_all_conversations()


# import json
# user_info = {
#     "email":"keshariaditya90@gmail.com",
#     "password":"Adikes209@@@@@"
# }

# try:
#     with open('cookies.jsonl', 'w') as f:
#         f.write(json.dumps(user_info) + '\n')
# except Exception as e: #file writing exception 
#     print(e)

user_info_available = False
try:
    with open('cookies.jsonl', 'r') as f:
        if f.read().strip():
            user_info_available = True
except FileNotFoundError:
    pass

print(user_info_available)