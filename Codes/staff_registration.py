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
from tkinter import messagebox

# create an application window
root= Tk()
#create the root title for the project
root.title("STAFF REGISTRATION")


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

image = Image.open('registration_bg.jpg')
copy_of_image = image.copy()
photo = ImageTk.PhotoImage(image)
label = ttk.Label(root, image = photo)
label.bind('<Configure>', resize_image)
label.pack(fill=BOTH, expand = YES)



# DATABASES
#create a database or connect to one
conn=sqlite3.connect('staff_details.db')

#create a cursor
'''
cursor class is an instance using which you can invoke methods that execute 
SQLite3 statements, fetch data from the result sets of the queries
'''
c=conn.cursor()

def register():
    '''
    This function adds user details as data to the database table
    '''
    #connect to the database 
    conn=sqlite3.connect('staffs.db')

    #create cursor
    c=conn.cursor()

    '''INSERT INTO Statement is used to add new rows of data into a table in the database.'''
    #the values of attributes is obtained by .get() from respective entry box
    c.execute("INSERT INTO user VALUES(:f_name,:l_name,:age,:gender,:pin,:re_pin,:father_name, :phone, :address,:city,:zipcode)",{
        'f_name':f_name.get(),
        'l_name':l_name.get(),
        'age':age.get(),
        'gender':gender.get(),
        'pin':pin.get(),
        're_pin':re_pin.get(),
        'father_name':father_name.get(),
        'phone':phone.get(),
        'address':address.get(),
        'city':city.get(),
        'zipcode':zipcode.get()
    })

    #messagebox to show when datas are added 
    messagebox.showinfo("Success","New STAFF is registered.")


    '''
    Once you are done with your changes and you want to commit the changes 
    then call .commit() method on connection object 
    '''
    #commit changes
    conn.commit()
    #close connection
    conn.close()

    #clear the text boxes
    f_name.delete(0,END)
    l_name.delete(0,END)
    age.delete(0,END)
    gender.delete(0,END)
    pin.delete(0,END)
    re_pin.delete(0,END)
    father_name.delete(0,END)
    phone.delete(0,END)
    address.delete(0,END)
    city.delete(0,END)
    zipcode.delete(0,END)



'''FRAME'''
'''Arrangement by GRID'''
# Create Frame
register_frame = Frame(root,width=230,height=590,highlightthickness=10,highlightbackground='yellow')
register_frame.place(x=10,y=172)


'''LABELS'''
# Create textbox labels and image labels
manager_profile=Image.open("user_photo.png")
resized_image=manager_profile.resize((150,150))
converted_image=ImageTk.PhotoImage(resized_image)
myLabel=Label(register_frame,image=converted_image, text="STAFF REGISTRATION",font=('Arial','20','bold'),compound='top')

myLabel.grid(row=0,column=1,columnspan=1)


'''
Labels
'''
    

# Create textbox labels
f_name_label=Label(register_frame,text="First Name",borderwidth=2,relief=GROOVE, font=('Arial','11','bold'),width=11, anchor="w",bg='#C04000',fg='white')
f_name_label.grid(row=1,column=0,padx=5,pady=2)

l_name_label=Label(register_frame,text="Last Name",borderwidth=2,relief=GROOVE, font=('Arial','11','bold'),width=11, anchor="w",bg='#C04000',fg='white')
l_name_label.grid(row=2,column=0,padx=5,pady=2)

age_label=Label(register_frame,text="Age",borderwidth=2,relief=GROOVE, font=('Arial','11','bold'),width=11, anchor="w",bg='#C04000',fg='white')
age_label.grid(row=3,column=0,padx=5,pady=2)

gender_label=Label(register_frame,text="Gender",borderwidth=2,relief=GROOVE, font=('Arial','11','bold'),width=11, anchor="w",bg='#C04000',fg='white')
gender_label.grid(row=4,column=0,padx=5,pady=2)

pin_label=Label(register_frame,text="Pin",borderwidth=2,relief=GROOVE, font=('Arial','11','bold'),width=11, anchor="w",bg='#C04000',fg='white')
pin_label.grid(row=6,column=0,padx=5,pady=2)

re_pin_label=Label(register_frame,text="Re-pin",borderwidth=2,relief=GROOVE, font=('Arial','11','bold'),width=11, anchor="w",bg='#C04000',fg='white')
re_pin_label.grid(row=7,column=0,padx=5,pady=2)

father_name_label=Label(register_frame,text="Father Name",borderwidth=2,relief=GROOVE, font=('Arial','11','bold'),width=11, anchor="w",bg='#C04000',fg='white')
father_name_label.grid(row=8,column=0,padx=5,pady=2)

phone_label=Label(register_frame,text="Phone",borderwidth=2,relief=GROOVE, font=('Arial','11','bold'),width=11, anchor="w",bg='#C04000',fg='white')
phone_label.grid(row=9,column=0,padx=5,pady=2)

address_label=Label(register_frame,text="Address",borderwidth=2,relief=GROOVE, font=('Arial','11','bold'),width=11, anchor="w",bg='#C04000',fg='white')
address_label.grid(row=10,column=0,padx=5,pady=2)

city_label=Label(register_frame,text="City",borderwidth=2,relief=GROOVE, font=('Arial','11','bold'),width=11, anchor="w",bg='#C04000',fg='white')
city_label.grid(row=11,column=0,padx=5,pady=2)

zipcode_label=Label(register_frame,text="zipcode",borderwidth=2,relief=GROOVE, font=('Arial','11','bold'),width=11, anchor="w",bg='#C04000',fg='white')
zipcode_label.grid(row=12,column=0,padx=5,pady=2)

'''
ENTRY
'''
# Create text entries
f_name=Entry(register_frame,width=45,bg='white')
f_name.grid(row=1,column=1,padx=5)

l_name=Entry(register_frame,width=45)
l_name.grid(row=2,column=1,padx=5)

age=Entry(register_frame,width=45)
age.grid(row=3,column=1,padx=5)


def add():
    print()
var=IntVar()
gender=Radiobutton(register_frame,text='Male',variable= var, value=1,anchor= "w", command=add)
gender.grid(row=4,column=1,padx=5)
gender=Radiobutton(register_frame,text='Female',variable= var, value=2,anchor= "w", command=add)
gender.grid(row=5,column=1,padx=5)

pin=Entry(register_frame,width=45,show="*")
pin.grid(row=6,column=1,padx=5)

re_pin=Entry(register_frame,width=45,show="*")
re_pin.grid(row=7,column=1,padx=5)

father_name=Entry(register_frame,width=45)
father_name.grid(row=8,column=1,padx=5)

phone=Entry(register_frame,width=45)
phone.grid(row=9,column=1,padx=5)

address=Entry(register_frame,width=45)
address.grid(row=10,column=1,padx=5)

city=Entry(register_frame,width=45)
city.grid(row=11,column=1,padx=5)

zipcode=Entry(register_frame,width=45)
zipcode.grid(row=12,column=1,padx=5)





# Create register button    
register_btn=Button(register_frame,text="REGISTER",font=('Arial','20','bold'),bg='#046307',fg='white',command=register)
register_btn.grid(row=13,column=0,padx=10,pady=10,columnspan=2,ipadx=120)

#create back button
back_btn=Button(register_frame,text="BACK",font=('Arial','10','bold'),bg='black',fg='white',width=5,command=NONE)
back_btn.grid(row=0,column=0)



# commit change
conn.commit()

# # close connection
conn.close()

#running the project till it is closed
mainloop()





