# import tkinter module to the program
from cgitb import text
from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk

# create an application window
root= Tk()
#create the root title for the project
root.title("staff LOGIN")

# #dimension, background color of project
# root.geometry("535x700")
# root.resizable(0,0)     #nonresizable, for resizable (True,True)
# root.config(bg='#3090C7')

#default fullscreen
root.attributes('-fullscreen',True)
#icon 
# root.iconbitmap("logo.ico") 
# from PIL import Image, ImageTk
# logo = ImageTk.PhotoImage(file='/home/mstacezro/Documents/ST4008CEM_32A_LED_Project/Code/logo_cristy.png')
# root.tk.call('wm', 'iconphoto', root._w, logo)


# #setting background image
# my_image=ImageTk.PhotoImage(Image.open("log_screen.jpg"))  
# #create a label
# my_label=Label(image=my_image)
# my_label.place(x = 0, y = 0)


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
login_frame = Frame(root)
login_frame.place(x=910,y=172)
# Top Frame
top_frame=Frame(login_frame,width=230,height=590)
top_frame.pack(side=RIGHT)

# Create textbox labels
staff_login=Label(login_frame,text="staff LOGIN",width=25, anchor="c",bg='#C04000',fg='white')
staff_login.pack(padx=20,pady=20,anchor=N)
# staff_login.place(relx=0.5, rely=0.5, anchor=CENTER)

# username_label=Label(login_frame,text="staff ID",width=25, anchor="w",bg='#C04000',fg='white')
# username_label.pack(ipadx=10,ipady=10)

# pin_label=Label(root,text="PIN",width=25, anchor="w",bg='#C04000',fg='white')
# pin_label.pack(ipadx=10,ipady=10)

# #Create entry boxes
# username_entry=ttk.Entry(root,width=30)
# username_entry.pack(ipadx=10,ipady=10)

# pin_entry=ttk.Entry(root,width=30)
# pin_entry.pack(ipadx=10,ipady=10)

# # Create sign in button    
# sign_in_btn=Button(root,text="LOGIN",bg='#046307',fg='white',command=NONE)
# sign_in_btn.pack(ipadx=10,ipady=10)

# # Create sign up  button    
# sign_up_btn=Button(root,text="REGISTER",bg='#046307',fg='white',command=NONE)
# sign_up_btn.pack(ipadx=10,ipady=10)


mainloop()