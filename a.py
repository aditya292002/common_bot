
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

import os
# from PyPDF2 import PdfReader
# from pypdf import PdfReader

# def add_pdf_content_to_file(filename):
#     # reader = PdfReader(filename)
#     # number_of_pages = len(reader.pages)
#     # content = []
#     # for i in range(number_of_pages):
#     #     page = reader.pages[0]
#     #     text = page.extract_text()
#     #     content.append(text)
#     # ic(content)
#     reader = PdfReader("pdf_files/Aditya_Keshari_Resume.pdf")
#     number_of_pages = len(reader.pages)
#     page = reader.pages[0]
#     text = page.extract_text()
#     ic(number_of_pages)
#     ic(page)
#     ic(text)
    
#     # with open("data.txt", "w") as f:
#     #     for page in content:
#     #         f.write("%s\n" % page)   
      
# add_pdf_content_to_file("pdf_files/Aditya_Keshari_Resume.pdf")

import fitz  # PyMuPDF

def extract_text_from_pdf(pdf_path):
    text = ""
    try:
        with fitz.open(pdf_path) as pdf_document:
            num_pages = pdf_document.page_count
            for page_num in range(num_pages):
                page = pdf_document[page_num]
                text += page.get_text()
    except Exception as e:
        print(f"Error: {e}")
    return text

# Replace 'your_pdf_file.pdf' with the path to your PDF file
pdf_path = 'pdf_files/dbms-notes-by-love-babbar.pdf'
extracted_text = extract_text_from_pdf(pdf_path)

# Print or process the extracted text
print(extracted_text)