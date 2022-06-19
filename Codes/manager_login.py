# import tkinter module to the program
from tkinter import*
from tkinter import ttk


# create an application window
root= Tk()
#create the root title for the project
root.title("MANAGER LOGIN")

#dimension, background color of project
root.geometry("535x700")
root.resizable(0,0)     #nonresizable, for resizable (True,True)
root.config(bg='#3090C7')

#icon 
##NOTE:  root.iconbitmap("*.ico") 

# Create textbox labels
manager_login=Label(root,text="Manager Login",width=25, anchor="w",bg='#C04000',fg='white')
manager_login.grid(row=1,column=0,padx=20)

username_label=Label(root,text="Username",width=25, anchor="w",bg='#C04000',fg='white')
username_label.grid(row=2,column=0)

password_label=Label(root,text="Password",width=25, anchor="w",bg='#C04000',fg='white')
password_label.grid(row=3,column=0)

#Create entry boxes
username_entry=Entry(root,width=30)
username_entry.grid(row=2,column=1)

password_entry=Entry(root,width=30)
password_entry.grid(row=3,column=1)

# Create sign in button    
sign_in_btn=Button(root,text="LOGIN",bg='#046307',fg='white',command=NONE)
sign_in_btn.grid(row=4,column=0,columnspan=2,pady=10,padx=10,ipadx=120)

# Create sign up  button    
sign_up_btn=Button(root,text="REGISTER",bg='#046307',fg='white',command=NONE)
sign_up_btn.grid(row=5,column=0,columnspan=2,pady=10,padx=10,ipadx=120)


