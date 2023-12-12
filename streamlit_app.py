import sqlite3
import streamlit as st 
import pandas as pd
from io import StringIO


conn = sqlite3.connect('company.db')
cursor = conn.cursor()

st.title('Employee Wages Calculator ')

st.subheader('Register Employees Manually:')
employee_name = st.text_input('Name:')
employee_surname = st.text_input('Sruname:')
employee_address = st.text_input('Address:')

if st.button('Register Employee'):
    cursor.execute('Insert Into employees (name,surname,address) Values (?,?,?)',
                   (employee_name,employee_surname, employee_address))
    conn.commit()
    st.success(f'Employee {employee_name} {employee_surname} registered successfully!')
    
    
uploaded_file = st.file_uploader('Upload CSV file', type=['csv'])

if uploaded_file is not None:
    
    df = pd.read_csv(uploaded_file)
    st.subheader('Uploaded Data:')
    st.write(df)
    
    if st.button("Calculate Wages"):
        
        df['total_wage'] = df['hours'] * df['rate']
        st.subheader('Calculated Wages')
        st.write(df)
        
        for index, row in df.iterrows():
            cursor.execute('Insert Into wages (employee_id, hours, rate, total_wage, date) Values (?,?,?,?,?)',
                           (row['employee_id'],row['hours'],row['rate'],row['total_wage'],row['date']))
        
        conn.commit()
        
        st.success('Wages calculated and saved to the database!')    
    

st.subheader('View wages for Employee:')
employee_id_view = st.number_input('Enter Employee ID:')
if st.button("View Wages"):
    wages_query = cursor.execute('Select * From wages Where employee_id=?',(employee_id_view,))
    wages_data = wages_query.fetchall()
    
    if not wages_data:
        st.warning(f'No wages for Employee Id {employee_id_view}')
        
    else:
        wages_df = pd.DataFrame(wages_data,columns=['wage_id','employee_id','hours','rate','total_wage','date'])
        st.subheader('Wages for Employee ID')
        st.write(wages_df)
        
        employee_name_sql = cursor.execute('Select name from employees where employee_id=?',(employee_id_view,))
        employee_name_view = employee_name_sql.fetchone()
        
        total_wage = wages_df['total_wage'].sum()
        st.success(f'Total Wage for Employee id {employee_id_view} with name {employee_name_view} is {total_wage}!')
        
conn.close()