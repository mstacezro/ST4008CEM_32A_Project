# import tkinter module to the program
from cgitb import text
from textwrap import fill
from tkinter import*
from tkinter import ttk
from tkinter.font import BOLD
from PIL import Image, ImageTk
import os
# from click import style
import sqlite3

# create an application window
root= Tk()
#create the root title for the project
root.title("MANAGER LOGIN")

#default fullscreen
root.attributes('-fullscreen',True)

supervisor_ID= 101
supervisor_pin=0000

#setting photo as background
def resize_image(event):
    new_width = event.width
    new_height = event.height
    image = copy_of_image.resize((new_width, new_height))
    photo = ImageTk.PhotoImage(image)
    label.config(image = photo)
    label.image = photo #avoid garbage collection

image = Image.open('login_bg.jpg')
copy_of_image = image.copy()
photo = ImageTk.PhotoImage(image)
label = ttk.Label(root, image = photo)
label.bind('<Configure>', resize_image)
label.pack(fill=BOTH, expand = YES)


'''
READ CRUD
'''
'''
EDIT ICON FUNCTION
'''
def manager_query():
    '''
    SELECT statement is used to fetch the data from a SQLite database table 
    which returns data in the form of a result table. 
    These result tables are also called result sets.
    '''

    info_query=Toplevel()
    info_query.title("Datas of managers")
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
    c.execute("SELECT *,oid FROM Manager")   

    #Fetches the existing rows from a result set
    records=c.fetchall()
    print(records)
    
    
    columns = ('first_name', 'last_name', 'Serial_No')
    
    tree = ttk.Treeview(info_query, columns=columns, show='headings')

    ##dimensions for the columns #BUG # no atomatic sizing
    # tree.column("# 1",anchor=CENTER, stretch=NO, width=30)
    # tree.column("# 2",anchor=CENTER, stretch=NO, width=100)
    tree.column("# 3",anchor=CENTER, stretch=NO, width=30)

    
    # define headings
    tree.heading('first_name', text='First Name')
    tree.heading('last_name', text='Last Name')
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

    

'''frame for info/edit'''
top_frame = Frame(root,width=900,height=100)
top_frame.place(x=1040,y=10)


#info button
manager_info=Image.open("information.png")
resized_info_image=manager_info.resize((90,90))
converted_info_image=ImageTk.PhotoImage(resized_info_image)

information=Button(top_frame,image=converted_info_image, text="INFO",font=('Arial','11','bold'),bg='white',compound='top',pady=10,command=manager_query)
information.grid(row=0,column=0)

'''
TOPLEVEL VERIFICATION for EDIT'''
'''The toplevel widget is used when a python application needs to represent 
some extra information, pop-up, or the group of widgets on the new window.'''
def edit():
    verification_edit=Toplevel()
    verification_edit.title("Editor")
    verification_edit.geometry("500x350")
    verification_edit.configure(bg='#B1FB17')


    username_label=Label(verification_edit, borderwidth=3,relief=GROOVE,text="Manager ID",font=('Arial','15','bold'),width=12, anchor="w",bg='#C04000',fg='white')
    username_label.grid(row=1,column=1, padx=10,pady=10)

    pin_label=Label(verification_edit, borderwidth=3,relief=GROOVE,text="PIN",font=('Arial','15','bold'),width=12, anchor="w",bg='#C04000',fg='white')
    pin_label.grid(row=2,column=1, padx=10,pady=10)

    #Create entry boxes
    username_entry=ttk.Entry(verification_edit,font="arial 15 bold",width=27)
    username_entry.grid(row=1,column=2,padx=10,pady=10)

    pin_entry=ttk.Entry(verification_edit,font="arial 15 bold",width=27,show="*")
    pin_entry.grid(row=2,column=2,padx=10,pady=10)
    

    # Create sign in button    
    sign_in_btn=Button(verification_edit,text="LOGIN",font=('Arial','15','bold'),anchor="c",bg='blue',fg='white',width=15,command=NONE)
    sign_in_btn.grid(row=3,column=1,columnspan=2)
    
    
    '''SUPERVISOR pin to reset manager pincode'''
    supervisor_username_label=Label(verification_edit, borderwidth=3,relief=GROOVE,text="Supervisor ID",font=('Arial','15','bold'),width=12, anchor="w",bg='#C04000',fg='white')
    supervisor_username_label.grid(row=4,column=1, padx=10,pady=10)

    supervisor_pin_label=Label(verification_edit, borderwidth=3,relief=GROOVE,text="PIN",font=('Arial','15','bold'),width=12, anchor="w",bg='#C04000',fg='white')
    supervisor_pin_label.grid(row=5,column=1, padx=10,pady=10)

    #Create entry boxes
    supervisor_username_entry=ttk.Entry(verification_edit,font="arial 15 bold",width=27)
    supervisor_username_entry.grid(row=4,column=2,padx=10,pady=10)

    supervisor_pin_entry=ttk.Entry(verification_edit,font="arial 15 bold",width=27,show="*")
    supervisor_pin_entry.grid(row=5,column=2,padx=10,pady=10)
    

    # Create sign in button    
    supervisor_sign_in_btn=Button(verification_edit,text="LOGIN",font=('Arial','15','bold'),anchor="c",bg='blue',fg='white',width=15,command=NONE)
    supervisor_sign_in_btn.grid(row=6,column=1,columnspan=2)
    

#edit button
manager_edit=Image.open("edit.png")
resized_edit_image=manager_edit.resize((90,90))
converted_edit_image=ImageTk.PhotoImage(resized_edit_image)

edit=Button(top_frame,image=converted_edit_image, text="EDIT",font=('Arial','11','bold'),bg='white',compound='top',pady=10,command=edit)
edit.grid(row=0,column=1)

#product_edit button
product_edit=Image.open("burger.png")
resized_product_edit_image=product_edit.resize((90,90))
converted_product_edit_image=ImageTk.PhotoImage(resized_product_edit_image)

product_edit=Button(top_frame,image=converted_product_edit_image, text="PRODUCT",font=('Arial','11','bold'),bg='white',compound='top',pady=10,command=edit)
product_edit.grid(row=0,column=2)
'''
REGISTER VALIDATION FUNCTION
'''
def register_validate():
    register_verify=Toplevel()
    register_verify.title("Editor")
    register_verify.geometry("500x200")
    register_verify.configure(bg='#B1FB17')


    username_label=Label(register_verify, borderwidth=3,relief=GROOVE,text="Supervisor ID",font=('Arial','15','bold'),width=12, anchor="w",bg='#C04000',fg='white')
    username_label.grid(row=1,column=1, padx=10,pady=10)

    pin_label=Label(register_verify, borderwidth=3,relief=GROOVE,text="PIN",font=('Arial','15','bold'),width=12, anchor="w",bg='#C04000',fg='white')
    pin_label.grid(row=2,column=1, padx=10,pady=10)

    #Create entry boxes
    username_entry=ttk.Entry(register_verify,font="arial 15 bold",width=27)
    username_entry.grid(row=1,column=2,padx=10,pady=10)

    pin_entry=ttk.Entry(register_verify,font="arial 15 bold",width=27,show="*")
    pin_entry.grid(row=2,column=2,padx=10,pady=10)
    

    # Create sign in button    
    sign_in_btn=Button(register_verify,text="LOGIN",font=('Arial','15','bold'),anchor="c",bg='blue',fg='white',width=15,command=NONE)
    sign_in_btn.grid(row=3,column=1,columnspan=2)
    



# Create Frame
login_frame = Frame(root,width=230,height=590)
login_frame.place(x=910,y=172)


# Create textbox labels

manager_profile=Image.open("manager.png")
resized_image=manager_profile.resize((200,200))
converted_image=ImageTk.PhotoImage(resized_image)
manager_profile_pic=Label(login_frame,image=converted_image, text="MANAGER LOGIN",font=('Arial','30','bold'),compound='top')
manager_profile_pic.grid(row=0,column=1,columnspan=2)

username_label=Label(login_frame, borderwidth=3,relief=GROOVE,text="Manager ID",font=('Arial','15','bold'),width=12, anchor="w",bg='#C04000',fg='white')
username_label.grid(row=3,column=1, padx=10,pady=10)

pin_label=Label(login_frame, borderwidth=3,relief=GROOVE,text="PIN",font=('Arial','15','bold'),width=12, anchor="w",bg='#C04000',fg='white')
pin_label.grid(row=4,column=1, padx=10,pady=10)

#Create entry boxes
username_entry=ttk.Entry(login_frame,font="arial 15 bold",width=27)
username_entry.grid(row=3,column=2,padx=10,pady=10)

pin_entry=ttk.Entry(login_frame,font="arial 15 bold",width=27,show="*")
pin_entry.grid(row=4,column=2,padx=10,pady=10)

def login():
    conn= sqlite3.connect('CRISTY_RECORD.db')
    c= conn.cursor()
    pin=pin_entry.get()
    c.execute("SELECT * FROM Manager WHERE")

# Create sign in button    
sign_in_btn=Button(login_frame,text="LOGIN",font=('Arial','15','bold'),anchor="c",bg='blue',fg='white',width=15,command=NONE)
sign_in_btn.grid(row=6,column=1,columnspan=2)

# Create sign up  button    
sign_up_btn=Button(login_frame,text="REGISTER",font=('Arial','15','bold'),anchor="c",bg='#046307',fg='white',width= 15,command=register_validate)
sign_up_btn.grid(row=7,column=1,columnspan=2)

notice_label=Label(login_frame,text="* NOTE: Registration under Supervisor only!",font=('Arial','10','italic'),anchor="c",fg='red',width= 40)
notice_label.grid(row=8,column=0,columnspan=4)


mainloop()