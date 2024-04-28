from gemeni import get_gemini_response
from data import *
import streamlit as st
import os
import sqlite3
from icecream import ic
from asyncio import *
import asyncio

# Add a title to the app    
st.title("File Uploader")

# Add a file uploader widget
file = st.file_uploader("Upload a file", type=["csv", "txt"])

# Display the uploaded file name
if file:
    st.write(f"File name: {file.name}")
else:
    st.write("No file was uploaded.")

# Add a description input widget
desc = st.text_input("Enter a description for the file")

# Add a submit button
if st.button("Submit"):
    # Save the file and description if both are provided
    if file and desc:
        # Define the directory where the file will be saved
        files_dir = "filesDIR"

        # Create the directory if it doesn't exist
        if not os.path.exists(files_dir):
            os.makedirs(files_dir)

        # Save the file to the directory
        file_path = os.path.join(files_dir, file.name)
        with open(file_path, "w") as f:
            f.write(file.read().decode("utf-8"))
        st.write(f"File {file.name} with description '{desc}' uploaded successfully.")

        # write functionality to add table and table description to a dictionary 
        tables_description[file.name] = desc
        tables.append(file.name)
        ic(tables_description)

        # code to upload the file to db

    else:
        st.write("File and description not saved.")
else:
    st.write("Please upload a file and enter a description.")


st.header("Ask question")

# function to get the result
def get_result(table_name, question):
    return get_gemini_response(
        f'''
            Given table {table_name} and table structure 
            {tables_structure[table_name]} 
            write a sql query to answer the question : {question}
        '''
    )
with st.form("my_form"):
    question = st.text_input("Enter your question")
    submit_button = st.form_submit_button("Submit")

    if question and submit_button:


        # code to get the description 
        description = f'''
        Given a questions: {question} some tables with description.
        Tables : Description, 
        '''
        # ic("description before text")
        # ic(description)

        # add the description
        for key in tables_description.keys():
            description = description + key + " : " + tables_description[key]

        description = description + "name the tables which you think can help answer the question."
        # ic(description)
        # code to get the tables (unique ones)
        st.write(description)
        gemini_resp_tables = get_gemini_response(description)
        st.write("Gemeni step 1 response is : " + gemini_resp_tables)
        step1_tables = []

        for word in gemini_resp_tables.split():
            word = word.strip().replace("•", "")    
            if word.strip().lower() in [table.lower() for table in tables]:  # tables coming from daata.py file
                step1_tables.append(word.lower())
        step1_tables = list(set(step1_tables))
      
        # for each table call a async function -> (get_result)
    
        resp = []
        for table in step1_tables:
            st.markdown(f"From the table {table}")
            st.write(get_result(table, question))
