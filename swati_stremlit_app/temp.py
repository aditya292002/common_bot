# from icecream import ic
# import sqlite3

# def get_tables():
#     # Connect to your SQLite database
#     conn = sqlite3.connect('new_db.sqlite3')
#     # Fetch table names and their columns dynamically
#     cursor = conn.cursor()
#     cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
#     tables = cursor.fetchall()
#     conn.close()
#     return tables
 

# ic(get_tables())


from icecream import ic
import google.generativeai as genai
import sqlite3
import pandas as pd
import os
import json
 
# constants
db_name = 'test_db.sqlite'
 
 
# ---------------------- GETTING LLM RESPONSE FROM GEMENI LLM ------------------------------
# configure our api key
genai.configure(api_key="AIzaSyCJyyGu0WEudYEtPJVHdYJlGFIaPV4avMQ")
 
# function to load local Gemini model and provide sql query as response
def get_gemini_response(question):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(question)
    return response.text.strip("'")
 
 
ic(get_gemini_response("who are ya?"))
'''
Notes:
1. Name of db: new_db.sqlite3

'''