import streamlit as st
import os
import sqlite3

import google.generativeai as genai

# configure our api key
genai.configure(api_key="AIzaSyCJyyGu0WEudYEtPJVHdYJlGFIaPV4avMQ")

# function to load local Gemini model and provide sql query as response
# def get_gemini_response(question, prompt):
async def get_gemini_response(question):  ####################
    model = genai.GenerativeModel('gemini-pro')
    # response = model.generate_content([prompt[0], question])
    response = model.generate_content(question) ######################
    return response.text.strip("'")

# # define your prompt
# prompt = [
#     """
#     You are an expert in converting English questions to SQL query!
#     The SQL database has the name Test and has the following columns - user_id, product_id, product_name,
#     brand, category and price \n\n For example,
#     Example 1 - How many entries of records are present in the database,
#     the SQL command will be something like this: SELECT COUNT(*) FROM Test;
#     Example 2 - Tell me the price of all the products with id 1,
#     the SQL command will be something like this: SELECT price FROM Test
#     WHERE product_id=1;
#     The SQL code should not have ' in the beginning or end and SQL word in the output.
    
#     """
# ]

# # get the generated SQL query
# sql_query = get_gemini_response("count rows in the database", prompt)

# # print the generated SQL query
# print(sql_query)

# get_gemini_response()