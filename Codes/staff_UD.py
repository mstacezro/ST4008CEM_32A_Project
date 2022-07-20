# import tkinter module to the program
from cgitb import text
from textwrap import fill
from tkinter import*
from tkinter import ttk
from tkinter import font
from tkinter.font import BOLD
from PIL import Image, ImageTk
import sqlite3
from tkinter import messagebox
import os

# create an application window
root= Tk()
#create the root title for the project
root.title("EDIT STAFF DATA")


'''FULLSCREEN'''
#default fullscreen
root.attributes('-fullscreen',True)

'''WALLPAPER'''
#setting photo as background
def resize_image(event):
    new_width = event.width
    new_height = event.height
    image = copy_of_image.resize((new_width, new_height))
    photo = ImageTk.PhotoImage(image)
    label.config(image = photo)
    label.image = photo #avoid garbage collection

image = Image.open('img/edit_bg.jpg')
copy_of_image = image.copy()
photo = ImageTk.PhotoImage(image)
label = ttk.Label(root, image = photo)
label.bind('<Configure>', resize_image)
label.pack(fill=BOTH, expand = YES)


def backspace():
    root.destroy()
    os.system('python staff_login.py')

'''FRAME'''
'''Arrangement by GRID'''
# Create Frame
editor_frame = Frame(root,width=150,height=500,highlightthickness=10,highlightbackground='yellow')
editor_frame.place(x=480,y=250)


'''LABELS'''
# Create textbox labels and image labels
staff_profile=Image.open("img/user_photo.png")
resized_image=staff_profile.resize((50,50))
converted_image=ImageTk.PhotoImage(resized_image)
myLabel=Label(editor_frame,image=converted_image, text="EDIT STAFF DATA",font=('Arial','20','bold'),compound='left')

myLabel.grid(row=0,column=0,columnspan=2)

# DATABASES
#create a database or connect to one
conn=sqlite3.connect('staff_details.db')

#create a cursor
'''
cursor class is an instance using which you can invoke methods that execute 
SQLite3 statements, fetch data from the result sets of the queries
'''
c=conn.cursor()
def update():
    '''
    UPDATE Query is used to modify the existing records in a table. 
    You can use WHERE clause with UPDATE query to update selected rows, 
    otherwise all the rows would be updated.
    '''
    #connect to database

    conn=sqlite3.connect('staff_details.db')
    #create cursor
    c=conn.cursor()
    
    #retrieve the row number of data to be updated by using .get() from entry box
    record_id=delete_box.get()

#update the data from the update window into staff_details window
    c.execute("""Update staff_details SET
    first_name=:first,
    last_name=:last,
    age=:age,
    gender=:gender,
    pin=:pin,
    father_name=:father_name,
    phone=:phone,
    address=:address,
    city=:city,
    zipcode=:zipcode
    WHERE oid=:oid""",
    {
        'first':f_name_editor.get(),
        'last':l_name_editor.get(),
        'age':age_editor.get(),
        'gender':gender_editor.get(),
        'pin':pin_editor.get(),
        're_pin':re_pin_editor.get(),
        'father_name':father_name_editor.get(),
        'phone':phone_editor.get(),
        'address':address_editor.get(),
        'city':city_editor.get(),
        'zipcode':zipcode_editor.get(),
        'oid':record_id
    })

  

    conn.commit()
    conn.close()

    #destroying all the data and closing window
    editor.destroy()


def delete():
    '''
    DELETE Query is used to delete the existing records from a table.
    You can use WHERE clause with DELETE query to delete the selected rows, 
    otherwise all the records would be deleted.
    '''
    #connect to database
    conn=sqlite3.connect('staff_details.db')
    
    #create cursor
    c=conn.cursor()

    #delete the unnecessary row which is obtained using .get()
    c.execute("DELETE FROM staff_details WHERE oid="+delete_box.get())

    #inform the staff_details that the data row is deleted
    print("Deleted")

    #messagebox to show when datas are deleted
    messagebox.showinfo("Success","Record has been deleted")

    #clears the delete box
    delete_box.delete(0,END)

    #commit changes
    conn.commit()
    conn.close()


def edit():
    '''
    This block of function is opened when update is clicked in staff_details window
    after required row is determined. 
    If row is not specified, it opens an empty window.
    '''
    #new window editor is created with specific designs,backgrounds

    #global identifier to enable modification 
    global editor

   

    #connect to main database
    conn=sqlite3.connect('staff_details.db')
    c=conn.cursor()

    #SELECT retrieves all data respective to the row in given box with .get()
    record_id=delete_box.get()
    c.execute("SELECT * FROM staff_details WHERE oid="+record_id)
    records=c.fetchall()

#global editors for modification
    global f_name_editor
    global l_name_editor
    global age_editor
    global gender_editor
    global pin_editor
    global re_pin_editor
    global father_name_editor
    global phone_editor
    global address_editor
    global city_editor
    global zipcode_editor

    
    

    #the data to be updated are recorded in 
    # respective attribute noted by index numbers in  database
    for record in records:
        f_name_editor.insert(0,record[0])
        l_name_editor.insert(0,record[1])
        age_editor.insert(0,record[2])
        gender_editor.insert(0,record[3])
        pin_editor.insert(0,record[4])
        re_pin_editor.insert(0,record[5])
        father_name_editor.insert(0,record[6])
        phone_editor.insert(0,record[7])
        address_editor.insert(0,record[8])
        city_editor.insert(0,record[9])
        zipcode_editor.insert(0,record[10])

    #update button for the update dialog box
    edit_btn=Button(editor_frame,text="Update",bg='#046307',fg='white',command=update)
    edit_btn.grid(row=8,column=0,pady=10,padx=10,ipadx=100)



    

    


'''
Labels
'''




# Create textbox labels
f_name_editor_label=Label(editor_frame,text="First Name",borderwidth=2,relief=GROOVE, font=('Arial','11','bold'),width=11, anchor="w",bg='#C04000',fg='white')
f_name_editor_label.grid(row=1,column=0,padx=5,pady=2)

l_name_editor_label=Label(editor_frame,text="Last Name",borderwidth=2,relief=GROOVE, font=('Arial','11','bold'),width=11, anchor="w",bg='#C04000',fg='white')
l_name_editor_label.grid(row=2,column=0,padx=5,pady=2)

age_editor_label=Label(editor_frame,text="Age",borderwidth=2,relief=GROOVE, font=('Arial','11','bold'),width=11, anchor="w",bg='#C04000',fg='white')
age_editor_label.grid(row=3,column=0,padx=5,pady=2)

gender_editor_label=Label(editor_frame,text="Gender",borderwidth=2,relief=GROOVE, font=('Arial','11','bold'),width=11, anchor="w",bg='#C04000',fg='white')
gender_editor_label.grid(row=4,column=0,padx=5,pady=2)

pin_editor_label=Label(editor_frame,text="Pin",borderwidth=2,relief=GROOVE, font=('Arial','11','bold'),width=11, anchor="w",bg='#C04000',fg='white')
pin_editor_label.grid(row=6,column=0,padx=5,pady=2)

re_pin_editor_label=Label(editor_frame,text="Re-pin",borderwidth=2,relief=GROOVE, font=('Arial','11','bold'),width=11, anchor="w",bg='#C04000',fg='white')
re_pin_editor_label.grid(row=7,column=0,padx=5,pady=2)

father_name_editor_label=Label(editor_frame,text="Father Name",borderwidth=2,relief=GROOVE, font=('Arial','11','bold'),width=11, anchor="w",bg='#C04000',fg='white')
father_name_editor_label.grid(row=8,column=0,padx=5,pady=2)

phone_editor_label=Label(editor_frame,text="Phone",borderwidth=2,relief=GROOVE, font=('Arial','11','bold'),width=11, anchor="w",bg='#C04000',fg='white')
phone_editor_label.grid(row=9,column=0,padx=5,pady=2)

address_editor_label=Label(editor_frame,text="Address",borderwidth=2,relief=GROOVE, font=('Arial','11','bold'),width=11, anchor="w",bg='#C04000',fg='white')
address_editor_label.grid(row=10,column=0,padx=5,pady=2)

city_editor_label=Label(editor_frame,text="City",borderwidth=2,relief=GROOVE, font=('Arial','11','bold'),width=11, anchor="w",bg='#C04000',fg='white')
city_editor_label.grid(row=11,column=0,padx=5,pady=2)

zipcode_editor_label=Label(editor_frame,text="zipcode",borderwidth=2,relief=GROOVE, font=('Arial','11','bold'),width=11, anchor="w",bg='#C04000',fg='white')
zipcode_editor_label.grid(row=12,column=0,padx=5,pady=2)

'''
ENTRY
'''
# Create text entries
f_name_editor=Entry(editor_frame,width=32,bg='white')
f_name_editor.grid(row=1,column=1,padx=5)

l_name_editor=Entry(editor_frame,width=32)
l_name_editor.grid(row=2,column=1,padx=5)

age_editor=Entry(editor_frame,width=32)
age_editor.grid(row=3,column=1,padx=5)


#set the Menu initially
gender=StringVar()
gender.set("Gender")

#creating dropdown menu
drop=OptionMenu(editor_frame,gender,"Male","Female","Other")
drop.grid(row=4,column=1,padx=5)

pin_editor=Entry(editor_frame,width=32,show="*")
pin_editor.grid(row=6,column=1,padx=5)

re_pin_editor=Entry(editor_frame,width=32,show="*")
re_pin_editor.grid(row=7,column=1,padx=5)

father_name_editor=Entry(editor_frame,width=32)
father_name_editor.grid(row=8,column=1,padx=5)

phone_editor=Entry(editor_frame,width=32)
phone_editor.grid(row=9,column=1,padx=5)

address_editor=Entry(editor_frame,width=32)
address_editor.grid(row=10,column=1,padx=5)

city_editor=Entry(editor_frame,width=32)
city_editor.grid(row=11,column=1,padx=5)

zipcode_editor=Entry(editor_frame,width=32)
zipcode_editor.grid(row=12,column=1,padx=5)

delete_box_label=Label(editor_frame,text="ID-delete/update",width=15, anchor="w",bg="red",fg='black')
delete_box_label.grid(row=13,column=0,pady=2)

delete_box=Entry(editor_frame,width=32,bg='grey',fg='white')
delete_box.grid(row=13,column=1,pady=2)

# Create delete button
delete_box_btn=Button(editor_frame,text="DELETE",font=('Arial','20','bold'),bg='red',command=delete)
delete_box_btn.grid(row=14,column=0,columnspan=2,pady=1,padx=0,ipadx=120)

# Create update button
edit_box_btn=Button(editor_frame,text="UPDATE",font=('Arial','20','bold'),bg='#046307',fg='white',command=edit)
edit_box_btn.grid(row=15,column=0,columnspan=2,pady=1,padx=10,ipadx=120)


'''FRAME'''
# Create  Back Frame
back_frame = Frame(root,width=50,height=50)
back_frame.place(x=1250,y=640)

#back button
back=Image.open("img/Back.png")
resized_back_image=back.resize((90,90))
converted_back_image=ImageTk.PhotoImage(resized_back_image)

back_button=Button(back_frame,image=converted_back_image, text="BACK",font=('Arial','11','bold'),bg='white',compound='top',pady=10,command=backspace)
back_button.grid(row=0,column=0)
# commit change
conn.commit()

# # close connection
conn.close()

#running the project till it is closed
mainloop()





