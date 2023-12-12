import sqlite3


conn = sqlite3.connect('company.db')

cursor = conn.cursor()

employees_sql = '''
                    Create Table If Not Exists employees (
                        employee_id Integer Primary Key,
                        name Text Not Null,
                        surname Tex Not Null,
                        address Text
                        )'''
cursor.execute(employees_sql)

wages_sql = '''
                Create Table If Not Exists wages (
                    wage_id Integer Primary Key,
                    employee_id Integer,
                    hours Integer,
                    rate Real,
                    total_wage Real,
                    date Text,
                    Foreign Key (employee_id) References employees (employee_id)
                    )'''
                    
cursor.execute(wages_sql)

conn.commit()
conn.close()