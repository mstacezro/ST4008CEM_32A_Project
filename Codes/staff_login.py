# import tkinter module to the program
from cgitb import text
from textwrap import fill
from tkinter import*
from tkinter import ttk
from tkinter import font
from tkinter.font import BOLD
from PIL import Image, ImageTk
from click import style

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
staff_info=Image.open("information.png")
resized_info_image=staff_info.resize((90,90))
converted_info_image=ImageTk.PhotoImage(resized_info_image)
information=Button(login_frame,image=converted_info_image, text="INFO",font=('Arial','11','bold'),bg='black',fg='white',compound='top',pady=10, command=NONE)
information.grid(row=9,column=0,columnspan=3,rowspan=2)


mainloop()