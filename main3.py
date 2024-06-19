# main3.py

import streamlit as st
import sqlite3
import pandas as pd
from utils2 import get_gemini_response, get_tables, find_synonyms

# Set Streamlit page configuration
st.set_page_config(page_title="NLP to SQL", page_icon="🚀")

# Display the TCS logo at the top-left corner
st.image('tcs_logo.png', width=150, caption="")    

st.sidebar.title("GenAI SOC Automation Tool")

st.title('Upload CSV and Query Data')

db_name = "new_db.sqlite3"  # Specify your database name

uploaded_file = st.file_uploader("Please choose a file")
if uploaded_file is not None:
    table_name = uploaded_file.name.lower().replace(" ", "_")
    table_name = table_name.replace("-", "_")
    table_name = table_name.replace(".csv", "")

    # Read the uploaded file as a pandas DataFrame
    df = pd.read_csv(uploaded_file)

    # Opening a connection and saving CSV file to DB
    conn = sqlite3.connect(db_name)
    df.to_sql(table_name, conn, index=False, if_exists='append')
    conn.commit()
    conn.close()
    st.success(f"File '{uploaded_file.name}' uploaded and saved to table '{table_name}' in '{db_name}'.")
    st.write("Data prepared to ask question")

with st.form("my_form"):
    question = st.text_input("Enter your question")
    submit_button = st.form_submit_button("Submit")

    if question and submit_button:
        try:
            # Opening a connection to the database
            conn = sqlite3.connect(db_name)

            tables = get_tables()

            # Dynamically extract column names from the table
            query = f"PRAGMA table_info({table_name})"
            cursor = conn.execute(query)
            columns_info = cursor.fetchall()
            column_names = [col_info[1] for col_info in columns_info]

            # Create a dictionary to store column names and their synonyms
            column_synonyms = {}
            for column in column_names:
                synonyms = find_synonyms(column)
                column_synonyms[column] = synonyms

            # Generate descriptions for Gemini based on column synonyms
            description = f"Given the question: '{question}', here are some tables with their descriptions:\n\n"
            for column, synonyms in column_synonyms.items():
                description += f"{column}: Synonyms - {', '.join(synonyms)}\n"

            description += "\nName the tables which you think can help answer the question."

            # Get suggested tables from Gemini
            gemini_resp_tables = get_gemini_response(description)

            if gemini_resp_tables:
                step1_tables = [word.lower() for word in gemini_resp_tables.split() if word.lower() in [table[0].lower() for table in tables]]
                step1_tables = list(set(step1_tables))

                if not step1_tables:
                    st.warning("No suitable tables found based on the question.")

                for table in step1_tables:
                    # Construct a query to fetch relevant data based on user's question
                    query = f"SELECT * FROM {table} WHERE ..."  # Define your query based on question context

                    # Execute the query and process the results
                    cursor.execute(query)
                    result = cursor.fetchall()

                    # Display the query response and results
                    st.write(f"Query Response for table '{table}':")
                    st.table(result)
            else:
                st.warning("No response from Gemini. Please check your question and try again.")

        except Exception as e:
            st.error(f"Error: {e}")

        finally:
            # Close the database connection
            if conn:
                conn.close()
