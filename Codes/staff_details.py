#import sqlite3
import sqlite3
# DATABASES
#create a database or connect to one
conn=sqlite3.connect('staff.db')

#create a cursor
'''
cursor class is an instance using which you can invoke methods that execute 
SQLite3 statements, fetch data from the result sets of the queries
'''
c=conn.cursor()

'''CREATE command is used to create a new SQLite database named "staff". '''

# print("Staff Table is created")