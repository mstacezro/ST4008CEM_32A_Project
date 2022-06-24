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
root.title("MANAGER LOGIN")


'''FULLSCREEN'''
#default fullscreen
root.attributes('-fullscreen',True)
#icon 
# root.iconbitmap("logo.ico") 
# from PIL import Image, ImageTk
# logo = ImageTk.PhotoImage(file='/home/mstacezro/Documents/ST4008CEM_32A_LED_Project/Code/logo_cristy.png')
# root.tk.call('wm', 'iconphoto', root._w, logo)


'''WALLPAPER'''
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



'''FRAME'''
'''Arrangement by GRID'''
# Create Frame
login_frame = Frame(root,width=230,height=590)
login_frame.place(x=910,y=172)


'''LABELS'''
# Create textbox labels and image labels
manager_profile=Image.open("manager.png")
resized_image=manager_profile.resize((200,200))
converted_image=ImageTk.PhotoImage(resized_image)
myLabel=Label(login_frame,image=converted_image, text="MANAGER LOGIN",font=('Arial','30','bold'),compound='top')

myLabel.grid(row=0,column=1,columnspan=2)


username_label=Label(login_frame, borderwidth=3,relief=GROOVE,text="Manager ID",font=('Arial','15','bold'),width=10, anchor="w",bg='#C04000',fg='white')
username_label.grid(row=3,column=1, padx=10,pady=10)

pin_label=Label(login_frame, borderwidth=3,relief=GROOVE,text="PIN",font=('Arial','15','bold'),width=10, anchor="w",bg='#C04000',fg='white')
pin_label.grid(row=4,column=1, padx=10,pady=10)


'''ENTRY BOXES'''
#defining a string variable  for entry boxes
# user_value=StringVar()
# user_value.set("") #setting initial value of string variable as blank

# pin_value=StringVar()
# pin_value.set("") #setting initial value of string variable as blank


equation = StringVar()
'''FUNCTIONS for NUMBERS BUTTONS'''

# function clear button

def clear():
    global exp
    exp = " "
    equation.set(exp)

def click(num):
    global exp
    exp=exp + str(num)
    equation.set(exp)


# def click(event):       #inputing numbers as in buttons in display
#     global user_value 
#     global pin_value     #global value can be modified inside this function
#     text=event.widget.cget("text")      #event.widget gives the button which is clicked and cget gives me texts from a widget
#     print(text)
        
#     user_value.set(user_value.get()+text)   #modifying scvalue with text inputed
#     username_entry.update                   #updates screen value with new scvalue  

#     pin_value.set(user_value.get()+text)   #modifying scvalue with text inputed
#     pin_entry.update                   #updates screen value with new scvalue  

#entry boxes
username_entry=ttk.Entry(login_frame,textvariable=equation,font="arial 15 bold",width=27)
username_entry.grid(row=3,column=2,padx=10,pady=10)

pin_entry=ttk.Entry(login_frame,textvar=equation,font="arial 15 bold",width=27)
pin_entry.grid(row=4,column=2,padx=10,pady=10)

'''BUTTONS'''
# Create sign in button    
sign_in_btn=Button(login_frame,text="LOGIN",font=('Arial','15','bold'),anchor="c",bg='blue',fg='white',width=15,command=NONE)
sign_in_btn.grid(row=6,column=1,columnspan=2)

# Create sign up  button    
sign_up_btn=Button(login_frame,text="REGISTER",font=('Arial','15','bold'),anchor="c",bg='#046307',fg='white',width= 15,command=NONE)
sign_up_btn.grid(row=7,column=1,columnspan=2)

notice_label=Label(login_frame,text="* NOTE: Registration via Supervisor only!",font=('Arial','10','italic'),anchor="c",fg='red',width= 40)
notice_label.grid(row=8,column=0,columnspan=4)




'''NUMBER FRAME'''
'''Arrangement by GRID'''
# Create Frame
number_frame = Frame(login_frame,width=230,height=590)
number_frame.grid(row=9, column=0,columnspan=4)

'''
NUMBER BUTTON
'''
#define number buttons for input
button_clear=Button(number_frame, text="C",font= ('Arial','13','bold'),padx=30,pady=59,bg="yellow",command=clear)
button_0=Button(number_frame, text="0",font= ('Arial','13','bold'),padx=30,pady=23,bg="#6A0DAD",command=lambda:click('0'))
button_1=Button(number_frame, text="1",font= ('Arial','13','bold'),padx=30,pady=23,bg="#6A0DAD",command=lambda:click('1'))
button_2=Button(number_frame, text="2",font= ('Arial','13','bold'),padx=30,pady=23,bg="#6A0DAD",command=lambda:click('2'))
button_3=Button(number_frame, text="3",font= ('Arial','13','bold'),padx=30,pady=23,bg="#6A0DAD",command=lambda:click('3'))
button_4=Button(number_frame, text="4",font= ('Arial','13','bold'),padx=30,pady=23,bg="#6A0DAD",command=lambda:click('4'))
button_5=Button(number_frame, text="5",font= ('Arial','13','bold'),padx=30,pady=23,bg="#6A0DAD",command=lambda:click('5'))
button_6=Button(number_frame, text="6",font= ('Arial','13','bold'),padx=30,pady=23,bg="#6A0DAD",command=lambda:click('6'))
button_7=Button(number_frame, text="7",font= ('Arial','13','bold'),padx=30,pady=23,bg="#6A0DAD",command=lambda:click('7'))
button_8=Button(number_frame, text="8",font= ('Arial','13','bold'),padx=30,pady=23,bg="#6A0DAD",command=lambda:click('8'))
button_9=Button(number_frame, text="9",font= ('Arial','13','bold'),padx=30,pady=23,bg="#6A0DAD",command=lambda:click('9'))



# # #display buttons on screen
# #first row
button_clear.grid(row=1,column=0,rowspan=2)
button_0.grid(row=1,column=1)
button_1.grid(row=1,column=2)
button_2.grid(row=1,column=3)
button_3.grid(row=1,column=4)
button_4.grid(row=1,column=5)

#second row
button_5.grid(row=2,column=1)
button_6.grid(row=2,column=2)
button_7.grid(row=2,column=3)
button_8.grid(row=2,column=4)
button_9.grid(row=2,column=5)




# #Events can be key presses or mouse operations by the user using bind syntax to the left-mouse click button
# button_clear.bind("<Button-1>",click)
# button_1.bind("<Button-1>",click)
# button_2.bind("<Button-1>",click)
# button_3.bind("<Button-1>",click)
# button_4.bind("<Button-1>",click)
# button_5.bind("<Button-1>",click)
# button_6.bind("<Button-1>",click)
# button_7.bind("<Button-1>",click)
# button_8.bind("<Button-1>",click)
# button_9.bind("<Button-1>",click)
# button_0.bind("<Button-1>",click)

mainloop()