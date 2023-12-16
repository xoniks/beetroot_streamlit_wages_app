# streamlit_app.py

import streamlit as st
import pymongo

# Initialize connection.
# Uses st.cache_resource to only run once.
@st.cache_resource
def init_connection():
    try:
        return pymongo.MongoClient(**st.secrets['mongo']['url'])
    except pymongo.errors.ServerSelectionTimeoutError as e:
        st.error(f"Failed to connect to MongoDB: {e}")
        raise e

client = init_connection()

st.title('Employee Wages App')

st.subheader('Register Employees Manually:')
employee_name = st.text_input('Name:')
employee_surname = st.text_input('Sruname:')
employee_address = st.text_input('Address:')

if st.button('Register Employee'):
    db = client.mydb
    employee_collection = db.employees
    employee_data = {'name':employee_name,
                     'surname':employee_surname,
                     'address':employee_address}  
    employee_collection.insert_one(employee_data)
    st.success('Employee added!')