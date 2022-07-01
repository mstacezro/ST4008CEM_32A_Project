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

'''Date Time'''
date_frame = Frame(root,width=900,height=909)
date_frame.place(x=990,y=10)

date = dt.datetime.now()
# Create Label to display the Date
label = Label(date_frame, text=f"{date:%H:%M:%S %p \n %A \n %x}", font="Calibri, 10")
label.grid(row=1,column=1)

# Create an instance of ttk style
s = ttk.Style()
s.theme_use('default')
s.configure('TNotebook.Tab', background="green3",font=('Helvetica', 20,BOLD),foreground='maroon',   
            height= 10,width=19,padx=10,pady=10)


'''
TAB frame'''
tab_frame = Frame(root,width=880,height=600)
tab_frame.place(x=10,y=160)

# # Create a tab control that manages multiple tabs
tabsystem = ttk.Notebook(tab_frame)

# Create new tabs using Frame widget
menu_tab = Frame(tabsystem)
order_tab = Frame(tabsystem)
member_tab = Frame(tabsystem)

tabsystem.add(menu_tab, text='MENU')
tabsystem.add(order_tab, text='ORDER STATUS')
tabsystem.add(member_tab, text='MEMBERS')
tabsystem.pack(expand=1, fill="both")


""" Frame for billing"""
bill_frame = Frame(root,width=450,height=650)
bill_frame.place(x=910,y=110)




#call mainloop to keep the window visible
mainloop()