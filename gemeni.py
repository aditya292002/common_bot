import streamlit as st
import os
import sqlite3

import google.generativeai as genai

# configure our api key
genai.configure(api_key="AIzaSyCJyyGu0WEudYEtPJVHdYJlGFIaPV4avMQ")

def get_gemini_response(question): 
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(question) 
    return response.text.strip("'")

# print(get_gemini_response('hi'))