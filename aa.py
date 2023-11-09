import threading
from icecream import ic
from hugchat import hugchat
from hugchat.login import Login

# Log in to huggingface and grant authorization to huggingchat
sign = Login("keshariaditya90@gmail.com", "Adikes209.")
cookies = sign.login()

# Save cookies to the local directory
cookie_path_dir = "./cookies_snapshot"
sign.saveCookiesToDir(cookie_path_dir)

# Create a ChatBot
chatbot = hugchat.ChatBot(cookies=cookies.get_dict())  # or cookie_path="usercookies/<email>.json"

# non stream response
query_result = chatbot.query("Hi!")
print(query_result) # or query_result.text or query_result["text"]


# Define your chunks
chunk1 = "Hi"
chunk2 = "..."

# Create threads for each chunk
thread1 = threading.Thread(target=process_chunk, args=(chunk1,))
thread2 = threading.Thread(target=process_chunk, args=(chunk2,))

# Start the threads
thread1.start()
thread2.start()

# Wait for both threads to finish
thread1.join()
thread2.join()