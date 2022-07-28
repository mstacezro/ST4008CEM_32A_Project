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

# def add():
    
'''WALLPAPER'''
#setting photo as background
def resize_image(event):
    new_width = event.width
    new_height = event.height
    image = copy_of_image.resize((new_width, new_height))
    photo = ImageTk.PhotoImage(image)
    label.config(image = photo)
    label.image = photo #avoid garbage collection

image = Image.open('img/registration_bg.jpg')
copy_of_image = image.copy()
photo = ImageTk.PhotoImage(image)
label = ttk.Label(root, image = photo)
label.bind('<Configure>', resize_image)
label.pack(fill=BOTH, expand = YES)


def backspace():
    '''This function returns back to the previous page'''
    root.destroy()
    os.system('python manager_login.py')
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
    conn=sqlite3.connect('CRISTY_RECORD.db')

    #create cursor
    c=conn.cursor()

    '''INSERT INTO Statement is used to add new rows of data into a table in the database.'''
    #the values of attributes is obtained by .get() from respective entry box
    c.execute("INSERT INTO Product(product_name,product_price) VALUES(?,?)",(p_name.get(),p_price.get()))

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


def delete():
    '''This deletes the product data in the table. Input is the product ID and output is the deletion of the data'''
    conn=sqlite3.connect('CRISTY_RECORD.db')
    c=conn.cursor()
    c.execute("SELECT * FROM Product WHERE product_id=?",(delete_box.get(),))
    data=c.fetchall()
    if data==[]:
        messagebox.showinfo("Error","Product is not found.")
    else:
        conn=sqlite3.connect('CRISTY_RECORD.db')
        c=conn.cursor()
        c.execute("DELETE FROM Product WHERE product_id=?",(delete_box.get(),))
        conn.commit()
        conn.close()
        delete_box.delete(0,END)
        messagebox.showinfo("Success","Product is deleted.")


def edit():
    '''This function edits the data of the products in the datbase'''
    global p_name_editor,p_price_editor,top
    conn=sqlite3.connect('CRISTY_RECORD.db')
    c=conn.cursor()
    c.execute("SELECT * FROM Product WHERE product_id=?",(delete_box.get(),))
    data=c.fetchall()
    if data==[]:
        messagebox.showinfo("Error","Product is not found.")
    else:
        top=Toplevel()
        top.title("Edit Product")
        top.configure(bg='#B1FB17')
        p_name_label_editor=Label(top,text="Product Name",font=('arial',12,'bold'),bg='#B1FB17')
        p_name_label_editor.grid(row=0,column=0,sticky=W)
        p_name_editor=Entry(top,font=('arial',12,'bold'),bg='#B1FB17')
        p_name_editor.grid(row=0,column=1,sticky=W)
        p_price_label_editor=Label(top,text="Product Price",font=('arial',12,'bold'),bg='#B1FB17')
        p_price_label_editor.grid(row=1,column=0,sticky=W)
        p_price_editor=Entry(top,width=30,font=('arial',12,'bold'),bg='#B1FB17')
        p_price_editor.grid(row=1,column=1,padx=20,pady=20)
        conn=sqlite3.connect('CRISTY_RECORD.db')
        c=conn.cursor()
        c.execute("SELECT * FROM product WHERE product_id=?",(delete_box.get(),))
        records=c.fetchall()
        for i in records:
            p_name_editor.insert(0,i[0])
            p_price_editor.insert(0,i[1])

        edit_btn=Button(top,text="Update",command=update,font=('arial',12,'bold'),bg='#B1FB17')
        edit_btn.grid(row=2,column=1,sticky=W)
        conn.commit()
        conn.close()
        top.mainloop()
def update():
    '''THis function updates the database of products'''
    conn=sqlite3.connect('CRISTY_RECORD.db')
    c=conn.cursor()
    c.execute("UPDATE Product SET product_name=?,product_price=? WHERE product_id=?",(p_name_editor.get(),p_price_editor.get(),delete_box.get()))
    conn.commit()
    conn.close()
    p_name_editor.delete(0,END)
    p_price_editor.delete(0,END)
    messagebox.showinfo("Success","Product is updated.")
    delete_box.delete(0,END)
    top.destroy()



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
    conn=sqlite3.connect('CRISTY_RECORD.db')
    c=conn.cursor()
    
    #create cursor
    c=conn.cursor()

    #select query of the database
    '''
    OID is auto-incrementing integer value,  
    that can be automatically assigned to each row of a table created WITH OIDS option.
    ID can be used as an identity (auto-increment) primary key column
    '''
    c.execute("SELECT *,oid FROM product")   #table name ????

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
    tree.heading('Serial_No',text='ID')
    



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
product_profile=Image.open("img/burger.png")
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
product_info=Image.open("img/information.png")
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




