import sqlite3
from tkinter import mainloop

'''
cursor class is an instance using which you can invoke methods that execute 
SQLite3 statements, fetch data from the result sets of the queries
'''

'''
Manager Database
'''
conn=sqlite3.connect('CRISTY_RECORD.db')
c=conn.cursor()
# Creating Table
try:
    c.execute("""CREATE TABLE Manager(
        f_name text,
        l_name text,
        age integer,
        gender text,
        pin integer,
        re_pin integer,
        father_name text,
        phone integer,
        address text,
        city text,
        zipcode integer,
        Manager_id integer PRIMARY KEY,
        Status text
    )""")
except:
    pass
'''
Staff Database
'''
try:
    c.execute("""CREATE TABLE Staff(
        f_name text,
        l_name text,
        age integer,
        gender text,
        pin integer,
        re_pin integer,
        father_name text,
        phone integer,
        address text,
        city text,
        zipcode integer,
        Staff_id integer PRIMARY KEY,
        Status text
    )""")

    print("Table Created")
except:
    pass

'''
Product Database
'''
try:
    c.execute("""CREATE TABLE Product(
        product_name text,
        product_price integer,
        product_id integer PRIMARY KEY
    )""")

    print("Table Created")
except:
    pass

'''
Billing Table
'''
try:
    c.execute("""CREATE TABLE Bill(
        bill_id integer PRIMARY KEY AUTOINCREMENT,
        bill_date text,
        status text
    )""")

except:
    pass

conn.commit()
conn.close()
# mainloop()

