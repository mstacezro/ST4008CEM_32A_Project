import sqlite3
# DATABASES
#create a database or connect to one
conn=sqlite3.connect('manager.db')

#create a cursor
'''
cursor class is an instance using which you can invoke methods that execute 
SQLite3 statements, fetch data from the result sets of the queries
'''
c=conn.cursor()


#manager table

'''CREATE command is used to create a new SQLite database named "manager. '''
c.execute("""CREATE TABLE manager(
    first_name text,
    last_name text,
    father_name text,
    DOB text,
    Phone integer,
    address text,
    city text,
    provine text,
    zipcode integer,
    pin integer,
    re_pin integer,
    manager_id integer
    )""")
print("Manager Table is is created.")

#.......................



#staff table

'''CREATE command is used to create a new SQLite database named "staff. '''
c.execute("""CREATE TABLE staff(
    first_name text,
    last_name text,
    father_name text,
    DOB text,
    Phone integer,
    address text,
    city text,
    provine text,
    zipcode integer,
    pin integer,
    re_pin integer,
    staff_id integer
    )""")
print("Staff Table is is created.")

#.......................

#product table

'''CREATE command is used to create a new SQLite database named "product. '''
c.execute("""CREATE TABLE product(
    product_name text,
    product_id integer,
    product_rate integer
    )""")
print("Product Table is is created.")

#.......................


