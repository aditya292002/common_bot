from icecream import ic
import streamlit as st
from utils import *
 
# Streamlit UI
st.title('Database Query Tool')
 
csv_dir = st.text_input('Enter directory path containing CSV files')
db_name = "new_db.sqlite3"
if st.button('Load CSV files'):
    if csv_dir and os.path.isdir(csv_dir):
        st.write(db_name)
        st.write(csv_dir)
        load_csv_to_sqlite(csv_dir, db_name)
        st.write("CSV files loaded into SQLite database successfully!")
    else:
        st.write("Please provide a valid directory path containing CSV files")
 
 
st.title("Click the button below once before asking question to load the table infos")
if st.button('Prepare to ask question'):
    get_table_structure()
    st.write("Data prepared to ask question")
 
with st.form("my_form"):
    question = st.text_input("Enter your question")
    submit_button = st.form_submit_button("Submit")
 
    if question and submit_button:
 
 
        # code to get the description
        description = f'''
        Given a questions: {question} some tables with description.
        Tables : Description,
        '''

        st.write(f"Description format is : {description}")
 
        tables = get_tables()
        # st.write("All tables are", tables, "with datatype", type(tables))
 
        # get table structure from table_data
        with open("table_data.json", 'r') as file:
            table_structure = json.load(file)
               
        # add the description
        for key in table_structure.keys():
            description = description + key + " : " + table_structure[key]
 
        description = description + "name the tables which you think can help answer the question."
        
        st.write(description)
        ##------------------------------------------------------------------------------------------
        # code to get the tables (unique ones)
        gemini_resp_tables = get_gemini_response(description)
        st.write("gemeni table suggestions response is", gemini_resp_tables)
        step1_tables = []
        for word in gemini_resp_tables.split():
            if word.lower() in [table[0].lower() for table in tables]:
                step1_tables.append(word.lower())
        step1_tables = list(set(step1_tables))
        st.write("suggested tables are", step1_tables )
 
 
        for table in step1_tables:
            # st.write the result
            st.write(f"From the table {table}")
            complete_question = "given question" + question + "write an sql query to answer the question from the table " + table_structure[table]
            st.write("Complete question : ",complete_question)
            query_response = get_gemini_response(complete_question)
            st.write("query_response ", query_response)
            st.write(process_query(query_response))