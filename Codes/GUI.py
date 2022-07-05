# import tkinter module to the program
from tkinter import*
from tkinter import ttk
from tkinter import font
from tkinter.font import BOLD
from turtle import width
from PIL import Image, ImageTk
import datetime as dt

# create an application window
root= Tk()

#create the root title for the project
root.title("POS")


#default fullscreen
root.attributes('-fullscreen',True)

#setting photo as background
def resize_image(event):
    new_width = event.width
    new_height = event.height
    image = copy_of_image.resize((new_width, new_height))
    photo = ImageTk.PhotoImage(image)
    label.config(image = photo)
    label.image = photo #avoid garbage collection

image = Image.open('menu_bg.jpg')
copy_of_image = image.copy()
photo = ImageTk.PhotoImage(image)
label = ttk.Label(root, image = photo)
label.bind('<Configure>', resize_image)
label.pack(fill=BOTH, expand = YES)



'''FRAMES for different sections'''
'''frame for date/time'''


'''frame for date/time/info/logout'''
top_frame = Frame(root,width=900,height=100)
top_frame.place(x=990,y=10)


#info button
manager_info=Image.open("information.png")
resized_info_image=manager_info.resize((90,90))
converted_info_image=ImageTk.PhotoImage(resized_info_image)

information=Button(top_frame,image=converted_info_image, text="INFO",font=('Arial','11','bold'),bg='white',compound='top',pady=10,command=NONE)
information.grid(row=0,column=0)

#edit button
manager_edit=Image.open("edit.png")
resized_edit_image=manager_edit.resize((90,90))
converted_edit_image=ImageTk.PhotoImage(resized_edit_image)

edit=Button(top_frame,image=converted_edit_image, text="EDIT",font=('Arial','11','bold'),bg='white',compound='top',pady=10,command=NONE)
edit.grid(row=0,column=1)

#logout button
manager_logout=Image.open("logout.png")
resized_logout_image=manager_logout.resize((90,90))
converted_logout_image=ImageTk.PhotoImage(resized_logout_image)

logout=Button(top_frame,image=converted_logout_image, text="LOGOUT",font=('Arial','11','bold'),bg='white',compound='top',pady=10,command=NONE)
logout.grid(row=0,column=2)



'''
Menu frame
'''
menu_frame = Frame(root,width=880,height=600)
menu_frame.place(x=10,y=160)




""" Frame for billing"""
bill_frame = Frame(root,width=450,height=650)
bill_frame.place(x=910,y=160)




#call mainloop to keep the window visible
mainloop()