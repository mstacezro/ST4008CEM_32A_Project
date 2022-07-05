import sqlite3

'''
Manager DB
'''
conn=sqlite3.connect('RECORD.db')
c=conn.cursor()
# Creating Table
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
    Manager_id integer,
)""")

'''
Staff DB
'''
c.execute("""CREATE TABLE=Staff(
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
    Staff_id integer
)""")

print("Table Created")


'''
Product DB
'''
c.execute("""CREATE TABLE Product(
    product_name text,
    product_price integer,
    product_id integer
)""")

print("Table Created")
