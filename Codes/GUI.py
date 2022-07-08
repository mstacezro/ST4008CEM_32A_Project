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




""" Frame for billing"""
bill_frame = Frame(root,width=450,height=600)
bill_frame.place(x=910,y=160)




'''
TAB frame'''
tab_frame = Frame(root,width=880,height=600)
tab_frame.place(x=10,y=160)

# # Create a tab control that manages multiple tabs
tabsystem = ttk.Notebook(tab_frame)

# Create new tabs using Frame widget
burger_tab = Frame(tabsystem)
sideDish_tab = Frame(tabsystem)
drinks_tab = Frame(tabsystem)
orderStatus_tab = Frame(tabsystem)

tabsystem.add(burger_tab, text='BURGER')
tabsystem.add(sideDish_tab, text='SIDE DISH')
tabsystem.add(drinks_tab, text='DRINKS')
tabsystem.add(orderStatus_tab, text='ORDER STATUS')
tabsystem.pack(expand=1, fill="both")


'''BURGER MENU buttons'''

burger1=Image.open("BuffBurger.PNG")
resized_burger1=burger1.resize((200,150))
converted_burger1=ImageTk.PhotoImage(resized_burger1)

burger1=Button(burger_tab,image=converted_burger1, text="Buff Burger \nRs 200 ",font=('Arial','11','bold'),bg='white',compound='top',pady=10,command=NONE)
burger1.grid(row=0,column=0,padx=30,pady=30)


burger2=Image.open("ChickenBurger.PNG")
resized_burger2=burger2.resize((200,150))
converted_burger2=ImageTk.PhotoImage(resized_burger2)

burger2=Button(burger_tab,image=converted_burger2, text="Chicken Burger \nRs 200 ",font=('Arial','11','bold'),bg='white',compound='top',pady=10,command=NONE)
burger2.grid(row=0,column=2,padx=30,pady=10)

burger3=Image.open("EggBurger.PNG")
resized_burger3=burger3.resize((200,150))
converted_burger3=ImageTk.PhotoImage(resized_burger3)

burger3=Button(burger_tab,image=converted_burger3, text="Egg Burger \nRs 150 ",font=('Arial','11','bold'),bg='white',compound='top',pady=10,command=NONE)
burger3.grid(row=1,column=0,padx=30,pady=30)

burger4=Image.open("VeggieBurger.PNG")
resized_burger4=burger4.resize((200,150))
converted_burger4=ImageTk.PhotoImage(resized_burger4)

burger4=Button(burger_tab,image=converted_burger4, text="Fish Burger \nRs 200 ",font=('Arial','11','bold'),bg='white',compound='top',pady=10,command=NONE)
burger4.grid(row=0,column=3,padx=30,pady=10)

burger5=Image.open("VeggieBurger.PNG")
resized_burger5=burger5.resize((200,150))
converted_burger5=ImageTk.PhotoImage(resized_burger5)

burger5=Button(burger_tab,image=converted_burger5, text="Paneer Burger \nRs 200 ",font=('Arial','11','bold'),bg='white',compound='top',pady=10,command=NONE)
burger5.grid(row=1,column=2,padx=30,pady=10)

burger6=Image.open("MuttonBurger.png")
resized_burger6=burger6.resize((200,150))
converted_burger6=ImageTk.PhotoImage(resized_burger6)

burger6=Button(burger_tab,image=converted_burger6, text="Pork Burger \nRs 200 ",font=('Arial','11','bold'),bg='white',compound='top',pady=10,command=NONE)
burger6.grid(row=1,column=3,padx=30,pady=10)

'''SIDE DISHbuttons'''

sideDish1=Image.open("Fries.PNG")
resized_sideDish1=sideDish1.resize((200,150))
converted_sideDish1=ImageTk.PhotoImage(resized_sideDish1)

sideDish1=Button(sideDish_tab,image=converted_sideDish1, text="Fries \nRs 100 ",font=('Arial','11','bold'),bg='white',compound='top',pady=10,command=NONE)
sideDish1.grid(row=0,column=0,padx=30,pady=30)

sideDish2=Image.open("ChickenWings.png")
resized_sideDish2=sideDish2.resize((200,150))
converted_sideDish2=ImageTk.PhotoImage(resized_sideDish2)

sideDish2=Button(sideDish_tab,image=converted_sideDish2, text="Chicken Wings \nRs 200 ",font=('Arial','11','bold'),bg='white',compound='top',pady=10,command=NONE)
sideDish2.grid(row=0,column=1,padx=30,pady=30)

sideDish3=Image.open("Nuggets.png")
resized_sideDish3=sideDish3.resize((200,150))
converted_sideDish3=ImageTk.PhotoImage(resized_sideDish3)

sideDish3=Button(sideDish_tab,image=converted_sideDish3, text="Nuggets \nRs 200 ",font=('Arial','11','bold'),bg='white',compound='top',pady=10,command=NONE)
sideDish3.grid(row=0,column=2,padx=30,pady=30)

sideDish4=Image.open("ApplePie.png")
resized_sideDish4=sideDish4.resize((200,150))
converted_sideDish4=ImageTk.PhotoImage(resized_sideDish4)

sideDish4=Button(sideDish_tab,image=converted_sideDish4, text="Apple Pie \nRs 100 ",font=('Arial','11','bold'),bg='white',compound='top',pady=10,command=NONE)
sideDish4.grid(row=1,column=0,padx=30,pady=30)

sideDish5=Image.open("BBQ-Wrap.png")
resized_sideDish5=sideDish5.resize((200,150))
converted_sideDish5=ImageTk.PhotoImage(resized_sideDish5)

sideDish5=Button(sideDish_tab,image=converted_sideDish5, text="BBQ Wrap \nRs 200 ",font=('Arial','11','bold'),bg='white',compound='top',pady=10,command=NONE)
sideDish5.grid(row=1,column=1,padx=30,pady=30)

sideDish6=Image.open("chickenSalad.png")
resized_sideDish6=sideDish6.resize((200,150))
converted_sideDish6=ImageTk.PhotoImage(resized_sideDish6)

sideDish6=Button(sideDish_tab,image=converted_sideDish6, text="Chicken Salad \nRs 200 ",font=('Arial','11','bold'),bg='white',compound='top',pady=10,command=NONE)
sideDish6.grid(row=1,column=2,padx=30,pady=30)

'''DRINKS DISHbuttons'''

drinks1=Image.open("Coke.png")
resized_drinks1=drinks1.resize((200,150))
converted_drinks1=ImageTk.PhotoImage(resized_drinks1)

drinks1=Button(drinks_tab,image=converted_drinks1, text="Coke \nRs 100 ",font=('Arial','11','bold'),bg='white',compound='top',pady=10,command=NONE)
drinks1.grid(row=0,column=0,padx=30,pady=30)

drinks2=Image.open("Fanta.png")
resized_drinks2=drinks2.resize((200,150))
converted_drinks2=ImageTk.PhotoImage(resized_drinks2)

drinks2=Button(drinks_tab,image=converted_drinks2, text="Fanta \nRs 100 ",font=('Arial','11','bold'),bg='white',compound='top',pady=10,command=NONE)
drinks2.grid(row=0,column=1,padx=30,pady=30)

drinks3=Image.open("Sprite.png")
resized_drinks3=drinks3.resize((200,150))
converted_drinks3=ImageTk.PhotoImage(resized_drinks3)

drinks3=Button(drinks_tab,image=converted_drinks3, text="Sprite \nRs 100 ",font=('Arial','11','bold'),bg='white',compound='top',pady=10,command=NONE)
drinks3.grid(row=0,column=2,padx=30,pady=30)

drinks4=Image.open("Chocolate-Frappe.png")
resized_drinks4=drinks4.resize((200,150))
converted_drinks4=ImageTk.PhotoImage(resized_drinks4)

drinks4=Button(drinks_tab,image=converted_drinks4, text="Chocolate Frappe \nRs 200 ",font=('Arial','11','bold'),bg='white',compound='top',pady=10,command=NONE)
drinks4.grid(row=1,column=0,padx=30,pady=30)

drinks5=Image.open("Chocolate-Oreo-Frappé.png")
resized_drinks5=drinks5.resize((200,150))
converted_drinks5=ImageTk.PhotoImage(resized_drinks5)

drinks5=Button(drinks_tab,image=converted_drinks5, text="Chocolate Oreo Frappe \nRs 200 ",font=('Arial','11','bold'),bg='white',compound='top',pady=10,command=NONE)
drinks5.grid(row=1,column=1,padx=30,pady=30)

drinks6=Image.open("Vanilla-Frappe.png")
resized_drinks6=drinks6.resize((200,150))
converted_drinks6=ImageTk.PhotoImage(resized_drinks6)

drinks6=Button(drinks_tab,image=converted_drinks6, text="Vanilla Frappe \nRs 200 ",font=('Arial','11','bold'),bg='white',compound='top',pady=10,command=NONE)
drinks6.grid(row=1,column=2,padx=30,pady=30)


#call mainloop to keep the window visible
mainloop()