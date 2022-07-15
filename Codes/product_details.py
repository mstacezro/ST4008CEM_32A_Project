# import tkinter module to the program
from cgitb import text
from textwrap import fill
from tkinter import*
from tkinter import ttk
from tkinter import font
from tkinter.font import BOLD
from PIL import Image, ImageTk
import sqlite3
from tkinter import messagebox
import os

# create an application window
root= Tk()
#create the root title for the project
root.title("PRODUCT DATABASE")


'''FULLSCREEN'''
#default fullscreen
root.attributes('-fullscreen',True)


'''WALLPAPER'''
#setting photo as background
def resize_image(event):
    new_width = event.width
    new_height = event.height
    image = copy_of_image.resize((new_width, new_height))
    photo = ImageTk.PhotoImage(image)
    label.config(image = photo)
    label.image = photo #avoid garbage collection

image = Image.open('registration_bg.jpg')
copy_of_image = image.copy()
photo = ImageTk.PhotoImage(image)
label = ttk.Label(root, image = photo)
label.bind('<Configure>', resize_image)
label.pack(fill=BOTH, expand = YES)



# DATABASES
#create a database or connect to one
conn=sqlite3.connect('Products.db')

#create a cursor
'''
cursor class is an instance using which you can invoke methods that execute 
SQLite3 statements, fetch data from the result sets of the queries
'''
c=conn.cursor()

def product_add():
    '''
    This function adds user details as data to the database table
    '''
    #connect to the database 
    conn=sqlite3.connect('Products.db')

    #create cursor
    c=conn.cursor()

    '''INSERT INTO Statement is used to add new rows of data into a table in the database.'''
    #the values of attributes is obtained by .get() from respective entry box
    c.execute("INSERT INTO user VALUES(:p_name,:p_price)",{
        'p_name':p_name.get(),
        'p_price':p_price.get()
    })

    #messagebox to show when datas are added 
    messagebox.showinfo("Success","New product is added.")


    '''
    Once you are done with your changes and you want to commit the changes 
    then call .commit() method on connection object 
    '''
    #commit changes
    conn.commit()
    #close connection
    conn.close()

    #clear the text boxes
    p_name.delete(0,END)
    p_price.delete(0,END)

def update():
    '''
    UPDATE Query is used to modify the existing records in a table. 
    You can use WHERE clause with UPDATE query to update selected rows, 
    otherwise all the rows would be updated.
    '''
    #connect to database

    conn=sqlite3.connect('Products.db')
    #create cursor
    c=conn.cursor()
    
    #retrieve the row number of data to be updated by using .get() from entry box
    record_id=delete_box.get()

#update the data from the update window into product_details window
    c.execute("""Update Products SET
    p_name=:product_name,
    p_price=:product_price,
    WHERE oid=:oid""",
    {
        'product_name':p_name_editor.get(),
        'product_price':p_price_editor.get(),
        'oid':record_id
    })

  

    conn.commit()
    conn.close()

    #destroying all the data and closing window
    editor.destroy()


def delete():
    '''
    DELETE Query is used to delete the existing records from a table.
    You can use WHERE clause with DELETE query to delete the selected rows, 
    otherwise all the records would be deleted.
    '''
    #connect to database
    conn=sqlite3.connect('Products.db')
    
    #create cursor
    c=conn.cursor()

    #delete the unnecessary row which is obtained using .get()
    c.execute("DELETE FROM product_details WHERE oid="+delete_box.get())

    #inform the product_details that the data row is deleted
    print("Deleted")

    #messagebox to show when datas are deleted
    messagebox.showinfo("Success","Record has been deleted")

    #clears the delete box
    delete_box.delete(0,END)

    #commit changes
    conn.commit()
    conn.close()


def edit():
    '''
    This block of function is opened when update is clicked in product_details window
    after required row is determined. 
    If row is not specified, it opens an empty window.
    '''
    #new window editor is created with specific designs,backgrounds

    #global identifier to enable modification 
    global editor

   

    #connect to main database
    conn=sqlite3.connect('Products.db')
    c=conn.cursor()

    #SELECT retrieves all data respective to the row in given box with .get()
    record_id=delete_box.get()
    c.execute("SELECT * FROM product_details WHERE oid="+record_id)
    records=c.fetchall()

#global editors for modification
    global p_name_editor
    global p_price_editor
    
    

    #the data to be updated are recorded in 
    # respective attribute noted by index numbers in  database
    for record in records:
        p_name_editor.insert(0,record[0])
        p_price_editor.insert(0,record[1])

    #update button for the update dialog box
    edit_btn=Button(product_frame,text="Update",bg='#046307',fg='white',command=update)
    edit_btn.grid(row=8,column=0,pady=10,padx=10,ipadx=100)

def product_query():
    '''
    SELECT statement is used to fetch the data from a SQLite database table 
    which returns data in the form of a result table. 
    These result tables are also called result sets.
    '''

    info_query=Toplevel()
    info_query.title("Datas of products")
    info_query.configure(bg='#B1FB17')

    #connect to main database
    conn=sqlite3.connect('Products.db')
    c=conn.cursor()
    
    #create cursor
    c=conn.cursor()

    #select query of the database
    '''
    OID is auto-incrementing integer value,  
    that can be automatically assigned to each row of a table created WITH OIDS option.
    ID can be used as an identity (auto-increment) primary key column
    '''
    c.execute("SELECT *,oid FROM products")   #table name ????

    #Fetches the existing rows from a result set
    records=c.fetchall()
    print(records)
    


    
    
    columns = ('p_name', 'p_price', 'Serial_No')
    

    tree = ttk.Treeview(info_query, columns=columns, show='headings')

    ##dimensions for the columns #BUG # no atomatic sizing
    # tree.column("# 1",anchor=CENTER, stretch=NO, width=30)
    # tree.column("# 2",anchor=CENTER, stretch=NO, width=100)
    tree.column("# 3",anchor=CENTER, stretch=NO, width=30)

    

    # define headings
    tree.heading('p_name', text='Product Name')
    tree.heading('p_price', text='Product Price')
    tree.heading('Serial_No',text='S.N.')
    



    # query_label=Label(info_query,text=print_records, anchor="w")
    # query_label.grid(row=8,column=0,columnspan=4)

    # add data to the treeview
    for record in records:
        tree.insert('', END, values=record)

    #position of tree label
    tree.grid(row=0, column=0, sticky=NSEW)

    # vertical scrollbar
    vbar = ttk.Scrollbar(info_query, orient=VERTICAL, command=tree.yview)
    tree.configure(yscrollcommand=vbar.set)
    vbar.grid(row=0, column=1, sticky=NS)


'''FRAME'''
'''Arrangement by GRID'''
# Create Frame
product_frame = Frame(root,width=230,height=590,highlightthickness=10,highlightbackground='yellow')
product_frame.place(x=10,y=165)


'''LABELS'''
# Create textbox labels and image labels
product_profile=Image.open("burger.png")
resized_image=product_profile.resize((150,150))
converted_image=ImageTk.PhotoImage(resized_image)
myLabel=Label(product_frame,image=converted_image, text="PRODUCT DATABASE",font=('Arial','20','bold'),compound='top')

myLabel.grid(row=0,column=1,columnspan=1)


'''
Labels
'''
    

# Create textbox labels
p_name_label=Label(product_frame,text="Product",borderwidth=2,relief=GROOVE, font=('Arial','11','bold'),width=11, anchor="w",bg='#C04000',fg='white')
p_name_label.grid(row=1,column=0,padx=5,pady=2)

p_price_label=Label(product_frame,text="Price",borderwidth=2,relief=GROOVE, font=('Arial','11','bold'),width=11, anchor="w",bg='#C04000',fg='white')
p_price_label.grid(row=2,column=0,padx=5,pady=2)


'''
ENTRY
'''
# Create text entries
p_name=Entry(product_frame,width=45,bg='white')
p_name.grid(row=1,column=1,padx=5)

p_price=Entry(product_frame,width=45)
p_price.grid(row=2,column=1,padx=5)


'''
BACK FUNCTION
'''

def backspace():
    root.destroy()
    os.system('python product_login.py')

#create back button
back_btn=Button(product_frame,text="BACK",font=('Arial','10','bold'),bg='black',fg='white',width=5,command=backspace)
back_btn.grid(row=0,column=0)



# Create register button    
add_btn=Button(product_frame,text="ADD",font=('Arial','20','bold'),bg='#046307',fg='white',command=product_add)
add_btn.grid(row=3,column=0,padx=10,pady=10,columnspan=2,ipadx=120)


delete_box_label=Label(product_frame,text="ID-delete/update",width=15, anchor="w",bg="red",fg='black')
delete_box_label.grid(row=4,column=0,pady=2)

delete_box=Entry(product_frame,width=32,bg='grey',fg='white')
delete_box.grid(row=4,column=1,pady=2)

# Create delete button
delete_box_btn=Button(product_frame,text="DELETE",font=('Arial','20','bold'),bg='red',command=delete)
delete_box_btn.grid(row=5,column=0,columnspan=2,pady=1,padx=0,ipadx=120)

# Create update button
edit_box_btn=Button(product_frame,text="UPDATE",font=('Arial','20','bold'),bg='#046307',fg='white',command=edit)
edit_box_btn.grid(row=6,column=0,columnspan=2,pady=1,padx=10,ipadx=120)


#info button
product_info=Image.open("information.png")
resized_info_image=product_info.resize((90,90))
converted_info_image=ImageTk.PhotoImage(resized_info_image)

information=Button(product_frame,image=converted_info_image, text="INFO",font=('Arial','11','bold'),bg='white',compound='top',pady=10,command=product_query)
information.grid(row=7,column=0)
# commit change
conn.commit()

# # close connection
conn.close()

#running the project till it is closed
mainloop()





