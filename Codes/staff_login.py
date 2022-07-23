# import tkinter module to the program
from cgitb import text
from textwrap import fill
from tkinter import*
from tkinter import ttk
from tkinter import font
from tkinter import messagebox
from tkinter.font import BOLD
from PIL import Image, ImageTk
import os
# from click import style
import sqlite3

# create an application window
root= Tk()
#create the root title for the project
root.title("STAFF LOGIN")

#default fullscreen
root.attributes('-fullscreen',True)

# Database connection
conn=sqlite3.connect('CRISTY_RECORD.db')
c=conn.cursor()
#setting photo as background
def resize_image(event):
    new_width = event.width
    new_height = event.height
    image = copy_of_image.resize((new_width, new_height))
    photo = ImageTk.PhotoImage(image)
    label.config(image = photo)
    label.image = photo #avoid garbage collection

image = Image.open('img/login_bg.jpg')
copy_of_image = image.copy()
photo = ImageTk.PhotoImage(image)
label = ttk.Label(root, image = photo)
label.bind('<Configure>', resize_image)
label.pack(fill=BOTH, expand = YES)

def login():
    conn=sqlite3.connect('CRISTY_RECORD.db')
    c=conn.cursor()
    
    c.execute("SELECT * FROM Staff WHERE staff_id=? and pin=?",(username_entry.get(),pin_entry.get()))
    if c.fetchall():
        c.execute("UPDATE Staff SET Status='inactive'")
        conn.commit()
        
        c.execute("UPDATE Staff SET Status='active' WHERE staff_id=?",(username_entry.get()))
        conn.commit()
        
        messagebox.showinfo('Login Sucessful','Welcome to the system')
        root.destroy()
        import GUI
    else:
        messagebox.showinfo('Login unsucessful','Incorrect credentials')
    conn.commit()
    conn.close()
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
    conn=sqlite3.connect('CRISTY_RECORD.db')
    
    #create cursor
    c=conn.cursor()

    #select query of the database
    '''
    OID is auto-incrementing integer value,  
    that can be automatically assigned to each row of a table created WITH OIDS option.
    ID can be used as an identity (auto-increment) primary key column
    '''
    c.execute("SELECT *,oid FROM Staff")   

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
        first_name=record[0]
        last_name=record[1]
        staff_id=record[11]
        tree.insert('', END, values=(first_name,last_name,staff_id))

    #position of tree label
    tree.grid(row=0, column=0, sticky=NSEW)

    # vertical scrollbar
    vbar = ttk.Scrollbar(info_query, orient=VERTICAL, command=tree.yview)
    tree.configure(yscrollcommand=vbar.set)
    vbar.grid(row=0, column=1, sticky=NS)
    
    conn.commit()
    conn.close()

    


'''frame for info/edit/logout'''
top_frame = Frame(root,width=900,height=100)
top_frame.place(x=1060,y=10)

'''
LOGOUT FUNCTION
'''
def backspace():
    '''THis function logouts the active account. Input is a click on the button with the confirmation from a dialogue box and output returns back to the previous page'''
    
    ask=messagebox.askyesno('Logout','DO YOU WANT TO LOGOUT?')
    if ask==True:
        conn=sqlite3.connect('CRISTY_RECORD.db')
        c=conn.cursor()
        
        c.execute("SELECT * FROM Manager WHERE Status='active'")
        conn.commit()
        c.execute("UPDATE Manager SET Status='inactive'")
        root.destroy()
        os.system('python manager_login.py')
        conn.commit()
        conn.close()
    else:
        pass
#logout button
manager_logout=Image.open("img/logout.png")
resized_logout_image=manager_logout.resize((90,90))
converted_logout_image=ImageTk.PhotoImage(resized_logout_image)

logout=Button(top_frame,image=converted_logout_image, text="LOGOUT",font=('Arial','11','bold'),bg='white',compound='top',pady=10,command=backspace)
logout.grid(row=0,column=2)


'''
REGISTER VALIDATION FUNCTION
'''

def register_validate():
    '''This function verifies supervisor for registering new managers. 
    Input is entry in the entrybox '''
    register_verify=Toplevel()
    register_verify.title("Editor")
    register_verify.geometry("500x200")
    register_verify.configure(bg='#B1FB17')


    username_label=Label(register_verify, borderwidth=3,relief=GROOVE,text="Manager ID",font=('Arial','15','bold'),width=12, anchor="w",bg='#C04000',fg='white')
    username_label.grid(row=1,column=1, padx=10,pady=10)

    pin_label=Label(register_verify, borderwidth=3,relief=GROOVE,text="PIN",font=('Arial','15','bold'),width=12, anchor="w",bg='#C04000',fg='white')
    pin_label.grid(row=2,column=1, padx=10,pady=10)

    #Create entry boxes
    username_entry=ttk.Entry(register_verify,font="arial 15 bold",width=27)
    username_entry.grid(row=1,column=2,padx=10,pady=10)

    pin_entry=ttk.Entry(register_verify,font="arial 15 bold",width=27,show="*")
    pin_entry.grid(row=2,column=2,padx=10,pady=10)
    
    def managerRegister_login():
        '''This function checks manager details and give success maessage if it is correct'''
        
        conn=sqlite3.connect('CRISTY_RECORD.db')
        c=conn.cursor()
    
        c.execute("SELECT * FROM Manager WHERE manager_id=? and pin=?",(username_entry.get(),pin_entry.get()))
        if c.fetchall():
            messagebox.showinfo('Login Sucessful','Welcome')
            root.destroy()
            import staff_registration
        else:
            messagebox.showinfo('Login unsucessful','Incorrect credentials')
        
        conn.commit()
        conn.close()

    # Create sign in button    
    sign_in_btn=Button(register_verify,text="LOGIN",font=('Arial','15','bold'),anchor="c",bg='blue',fg='white',width=15,command=managerRegister_login)
    sign_in_btn.grid(row=3,column=1,columnspan=2)
    
#info button
manager_info=Image.open("img/information.png")
resized_info_image=manager_info.resize((90,90))
converted_info_image=ImageTk.PhotoImage(resized_info_image)

information=Button(top_frame,image=converted_info_image, text="INFO",font=('Arial','11','bold'),bg='white',compound='top',pady=10,command=staff_query)
information.grid(row=0,column=0)

'''
TOPLEVEL VERIFICATION for EDIT'''
'''The toplevel widget is used when a python application needs to represent 
some extra information, pop-up, or the group of widgets on the new window.'''
def edit():
    '''This function enables modification in manager table. 
    Input is manager credentials and output is redirection to manager UD page'''
    
    verification_edit=Toplevel()
    verification_edit.title("Editor")
    verification_edit.geometry("500x350")
    verification_edit.configure(bg='#B1FB17')


    username_label=Label(verification_edit, borderwidth=3,relief=GROOVE,text="Staff ID",font=('Arial','15','bold'),width=12, anchor="w",bg='#C04000',fg='white')
    username_label.grid(row=1,column=1, padx=10,pady=10)

    pin_label=Label(verification_edit, borderwidth=3,relief=GROOVE,text="PIN",font=('Arial','15','bold'),width=12, anchor="w",bg='#C04000',fg='white')
    pin_label.grid(row=2,column=1, padx=10,pady=10)

    #Create entry boxes
    username_entry=ttk.Entry(verification_edit,font="arial 15 bold",width=27)
    username_entry.grid(row=1,column=2,padx=10,pady=10)

    pin_entry=ttk.Entry(verification_edit,font="arial 15 bold",width=27,show="*")
    pin_entry.grid(row=2,column=2,padx=10,pady=10)
    
    def manager_login():
        '''This function authenciates manager login'''
        conn=sqlite3.connect('CRISTY_RECORD.db')
        c=conn.cursor()
    
        c.execute("SELECT * FROM Manager WHERE manager_id=? and pin=?",(manager_username_entry.get(),manager_pin_entry.get()))
        if c.fetchall():
            conn=sqlite3.connect('CRISTY_RECORD.db')
            c=conn.cursor()
            c.execute("SELECT * FROM Staff WHERE status='active' ")
            if c.fetchall():
                c.execute("UPDATE Staff SET status='inactive'")
                conn.commit()
            else:
                pass
            messagebox.showinfo('Login Sucessful','Welcome')
            root.destroy()
            import staff_UD
        else:
            messagebox.showinfo('Login unsucessful','Incorrect credentials')
        conn.commit()
        conn.close()
    
    def edit_login():
        '''This function authenciates staff login'''
        conn=sqlite3.connect('CRISTY_RECORD.db')
        c=conn.cursor()
    
        c.execute("SELECT * FROM Staff WHERE staff_id=? and pin=?",(username_entry.get(),pin_entry.get()))
        if c.fetchall():
            c.execute("UPDATE Staff SET Status='inactive'")
            conn.commit()
        
            c.execute("UPDATE Staff SET Status='active' WHERE staff_id=?",(username_entry.get()))
            conn.commit()
            messagebox.showinfo('Login Sucessful','Welcome')
            root.destroy()
            import staff_UD
        else:
            messagebox.showinfo('Login unsucessful','Incorrect credentials')
        conn.commit()
        conn.close()

    # Create sign in button    
    sign_in_btn=Button(verification_edit,text="LOGIN",font=('Arial','15','bold'),anchor="c",bg='blue',fg='white',width=15,command=edit_login)
    sign_in_btn.grid(row=3,column=1,columnspan=2)
    
    
    '''MANAGER pin to reset staff pincode'''
    manager_username_label=Label(verification_edit, borderwidth=3,relief=GROOVE,text="Manager ID",font=('Arial','15','bold'),width=12, anchor="w",bg='#C04000',fg='white')
    manager_username_label.grid(row=4,column=1, padx=10,pady=10)

    manager_pin_label=Label(verification_edit, borderwidth=3,relief=GROOVE,text="PIN",font=('Arial','15','bold'),width=12, anchor="w",bg='#C04000',fg='white')
    manager_pin_label.grid(row=5,column=1, padx=10,pady=10)

    #Create entry boxes
    manager_username_entry=ttk.Entry(verification_edit,font="arial 15 bold",width=27)
    manager_username_entry.grid(row=4,column=2,padx=10,pady=10)

    manager_pin_entry=ttk.Entry(verification_edit,font="arial 15 bold",width=27,show="*")
    manager_pin_entry.grid(row=5,column=2,padx=10,pady=10)
    

    # Create sign in button    
    manager_sign_in_btn=Button(verification_edit,text="LOGIN",font=('Arial','15','bold'),anchor="c",bg='blue',fg='white',width=15,command=manager_login)
    manager_sign_in_btn.grid(row=6,column=1,columnspan=2)
    
#edit button
manager_edit=Image.open("img/edit.png")
resized_edit_image=manager_edit.resize((90,90))
converted_edit_image=ImageTk.PhotoImage(resized_edit_image)

edit=Button(top_frame,image=converted_edit_image, text="EDIT",font=('Arial','11','bold'),bg='white',compound='top',pady=10,command=edit)
edit.grid(row=0,column=1)


'''Create Frame for login'''
login_frame = Frame(root,width=230,height=590)
login_frame.place(x=910,y=172)


# Create textbox labels

staff_profile=Image.open("img/user_photo.png")
resized_image=staff_profile.resize((200,200))
converted_image=ImageTk.PhotoImage(resized_image)
staff_profile_pic=Label(login_frame,image=converted_image, text="STAFF LOGIN",font=('Arial','30','bold'),compound='top')
staff_profile_pic.grid(row=0,column=1,columnspan=2)



username_label=Label(login_frame, borderwidth=3,relief=GROOVE,text="Staff ID",font=('Arial','15','bold'),width=10, anchor="w",bg='#C04000',fg='white')
username_label.grid(row=3,column=1, padx=10,pady=10)

pin_label=Label(login_frame, borderwidth=3,relief=GROOVE,text="PIN",font=('Arial','15','bold'),width=10, anchor="w",bg='#C04000',fg='white')
pin_label.grid(row=4,column=1, padx=10,pady=10)

#Create entry boxes
username_entry=ttk.Entry(login_frame,font="arial 15 bold",width=27)
username_entry.grid(row=3,column=2,padx=10,pady=10)

pin_entry=ttk.Entry(login_frame,font="arial 15 bold",width=27,show="*")
pin_entry.grid(row=4,column=2,padx=10,pady=10)

# Create sign in button    
sign_in_btn=Button(login_frame,text="LOGIN",font=('Arial','15','bold'),anchor="c",bg='blue',fg='white',width=15,command=login)
sign_in_btn.grid(row=6,column=1,columnspan=2)

# Create sign up  button    
sign_up_btn=Button(login_frame,text="REGISTER",font=('Arial','15','bold'),anchor="c",bg='#046307',fg='white',width= 15,command=register_validate)
sign_up_btn.grid(row=7,column=1,columnspan=2)

notice_label=Label(login_frame,text="* NOTE: Registration under Manager only!",font=('Arial','10','italic'),anchor="c",fg='red',width= 40)
notice_label.grid(row=8,column=0,columnspan=4)


conn.commit()
conn.cursor()
mainloop()