# import tkinter module to the program
from cgitb import text
from textwrap import fill
from tkinter import*
from tkinter import ttk
from tkinter import font
from tkinter.font import BOLD
from PIL import Image, ImageTk
from click import style
import sqlite3

# create an application window
root= Tk()
#create the root title for the project
root.title("STAFF LOGIN")



#default fullscreen
root.attributes('-fullscreen',True)
#icon 
# root.iconbitmap("logo.ico") 
# from PIL import Image, ImageTk
# logo = ImageTk.PhotoImage(file='/home/mstacezro/Documents/ST4008CEM_32A_LED_Project/Code/logo_cristy.png')
# root.tk.call('wm', 'iconphoto', root._w, logo)



#setting photo as background
def resize_image(event):
    new_width = event.width
    new_height = event.height
    image = copy_of_image.resize((new_width, new_height))
    photo = ImageTk.PhotoImage(image)
    label.config(image = photo)
    label.image = photo #avoid garbage collection

image = Image.open('log_screen.jpg')
copy_of_image = image.copy()
photo = ImageTk.PhotoImage(image)
label = ttk.Label(root, image = photo)
label.bind('<Configure>', resize_image)
label.pack(fill=BOTH, expand = YES)



# Create Frame
login_frame = Frame(root,width=230,height=590)
login_frame.place(x=910,y=172)


# Create textbox labels

staff_profile=Image.open("user_photo.png")
resized_image=staff_profile.resize((200,200))
converted_image=ImageTk.PhotoImage(resized_image)
staff_profile_pic=Label(login_frame,image=converted_image, text="STAFF LOGIN",font=('Arial','30','bold'),compound='top')
staff_profile_pic.grid(row=0,column=1,columnspan=2)



username_label=Label(login_frame, borderwidth=3,relief=GROOVE,text="staff ID",font=('Arial','15','bold'),width=10, anchor="w",bg='#C04000',fg='white')
username_label.grid(row=3,column=1, padx=10,pady=10)

pin_label=Label(login_frame, borderwidth=3,relief=GROOVE,text="PIN",font=('Arial','15','bold'),width=10, anchor="w",bg='#C04000',fg='white')
pin_label.grid(row=4,column=1, padx=10,pady=10)

#Create entry boxes
username_entry=ttk.Entry(login_frame,font="arial 15 bold",width=27)
username_entry.grid(row=3,column=2,padx=10,pady=10)

pin_entry=ttk.Entry(login_frame,font="arial 15 bold",width=27,show="*")
pin_entry.grid(row=4,column=2,padx=10,pady=10)

# Create sign in button    
sign_in_btn=Button(login_frame,text="LOGIN",font=('Arial','15','bold'),anchor="c",bg='blue',fg='white',width=15,command=NONE)
sign_in_btn.grid(row=6,column=1,columnspan=2)

# Create sign up  button    
sign_up_btn=Button(login_frame,text="REGISTER",font=('Arial','15','bold'),anchor="c",bg='#046307',fg='white',width= 15,command=NONE)
sign_up_btn.grid(row=7,column=1,columnspan=2)

notice_label=Label(login_frame,text="* NOTE: Registration under Manager only!",font=('Arial','10','italic'),anchor="c",fg='red',width= 40)
notice_label.grid(row=8,column=0,columnspan=4)

'''
READ CRUD
'''

def staff_query():
    '''
    SELECT statement is used to fetch the data from a SQLite database table 
    which returns data in the form of a result table. 
    These result tables are also called result sets.
    '''

    info_query=Toplevel()
    info_query.title("Datas of Staffs")
    info_query.configure(bg='#B1FB17')

    #connect to main database
    conn=sqlite3.connect('staff_details.db')
    c=conn.cursor()
    
    #create cursor
    c=conn.cursor()

    #select query of the database
    '''
    OID is auto-incrementing integer value,  
    that can be automatically assigned to each row of a table created WITH OIDS option.
    ID can be used as an identity (auto-increment) primary key column
    '''
    c.execute("SELECT *,oid FROM staffs")   #table name ????

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

    

staff_info=Image.open("information.png")
resized_info_image=staff_info.resize((90,90))
converted_info_image=ImageTk.PhotoImage(resized_info_image)
information=Button(login_frame,image=converted_info_image, text="INFO",font=('Arial','11','bold'),bg='black',fg='white',compound='top',pady=10, command=staff_query)
information.grid(row=9,column=0,columnspan=3,rowspan=2)


mainloop()