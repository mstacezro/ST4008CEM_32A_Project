# import tkinter module to the program
from cgitb import text
from logging import root
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
root1 = Tk()
# create the root title for the project
root1.title("EDIT STAFF DATA")

'''FULLSCREEN'''
# default fullscreen
root1.attributes('-fullscreen', True)


def update_func():
    '''Ths function updates staff data'''

    # f_name_editor1
    conn = sqlite3.connect('CRISTY_RECORD.db')
    c = conn.cursor()
    c.execute("SELECT * FROM Staff WHERE Staff_id=?", (delete_box.get(),))
    if c.fetchall:
        # fetching the data from the database
        data = c.fetchall()
        c.execute("UPDATE Staff SET Status='active' WHERE staff_id=?", (
            delete_box.get()))
        conn.commit()
        for i in data:
            f_name_editor1.insert(0, i[0])
            l_name_editor1.insert(0, i[1])
            age_editor1.insert(0, i[2])
            gender1.set(i[3])
            pin_editor1.insert(0, i[4])
            re_pin_editor1.insert(0, i[4])
            father_name_editor1.insert(0, i[6])
            phone_editor1.insert(0, i[7])
            address_editor1.insert(0, i[8])
            city_editor1.insert(0, i[9])
            zipcode_editor1.insert(0, i[10])

        update_frame.pack(fill='both', expand=1)
        root.forget()
    else:
        messagebox.showinfo("Error", "No record found")

    conn.commit()
    conn.close()


def root_func():

    f_name_editor1.delete(0, END)
    l_name_editor1.delete(0, END)
    age_editor1.delete(0, END)
    pin_editor1.delete(0, END)
    re_pin_editor1.delete(0, END)
    father_name_editor1.delete(0, END)
    phone_editor1.delete(0, END)
    address_editor1.delete(0, END)
    city_editor1.delete(0, END)
    zipcode_editor1.delete(0, END)
    root.pack(fill='both', expand=1)
    update_frame.forget()


root = Frame(root1)
update_frame = Frame(root1)
conn = sqlite3.connect('CRISTY_RECORD.db')
c = conn.cursor()
c.execute("SELECT * FROM Staff WHERE status='active'")
if c.fetchall():
    update_frame.pack(fill='both', expand=1)
else:
    root.pack(fill='both', expand=1)
'''WALLPAPER'''
# setting photo as background


def resize_image(event):
    new_width = event.width
    new_height = event.height
    image = copy_of_image.resize((new_width, new_height))
    photo = ImageTk.PhotoImage(image)
    label.config(image=photo)
    label.image = photo  # avoid garbage collection


image = Image.open('img/edit_bg.jpg')
copy_of_image = image.copy()
photo = ImageTk.PhotoImage(image)
label = ttk.Label(root, image=photo)
label.bind('<Configure>', resize_image)
label.pack(fill=BOTH, expand=YES)


def backspace():
    '''This function return back to the previous page'''
    root.destroy()
    os.system('python staff_login.py')


'''FRAME'''
'''Arrangement by GRID'''
# Create Frame
editor_frame = Frame(root, width=150, height=500,
                     highlightthickness=10, highlightbackground='yellow')
editor_frame.place(x=480, y=250)


'''LABELS'''
# Create textbox labels and image labels
staff_profile = Image.open("img/user_photo.png")
resized_image = staff_profile.resize((50, 50))
converted_image = ImageTk.PhotoImage(resized_image)
myLabel = Label(editor_frame, image=converted_image, text="EDIT STAFF DATA", font=(
    'Arial', '20', 'bold'), compound='left')

myLabel.grid(row=0, column=0, columnspan=2)

# DATABASES
# create a database or connect to one
conn = sqlite3.connect('staff_details.db')

# create a cursor
'''
cursor class is an instance using which you can invoke methods that execute 
SQLite3 statements, fetch data from the result sets of the queries
'''
c = conn.cursor()


def delete():
    '''
    DELETE Query is used to delete the existing records from a table.
    You can use WHERE clause with DELETE query to delete the selected rows, 
    otherwise all the records would be deleted.
    '''
    # connect to database
    conn = sqlite3.connect('CRISTY_RECORD.db')

    # create cursor
    c = conn.cursor()

    # delete the unnecessary row which is obtained using .get()
    c.execute("DELETE FROM Staff WHERE staff_id=?", (delete_box.get(),))

    # inform the staff_details that the data row is deleted
    print("Deleted")

    # messagebox to show when datas are deleted
    messagebox.showinfo("Success", "Record has been deleted")

    # clears the delete box
    delete_box.delete(0, END)

    # commit changes
    conn.commit()
    conn.close()


# def edit():


'''
Labels
'''


# Create textbox labels
f_name_editor_label = Label(editor_frame, text="First Name", borderwidth=2, relief=GROOVE, font=(
    'Arial', '11', 'bold'), width=11, anchor="w", bg='#C04000', fg='white')
f_name_editor_label.grid(row=1, column=0, padx=5, pady=2)

l_name_editor_label = Label(editor_frame, text="Last Name", borderwidth=2, relief=GROOVE, font=(
    'Arial', '11', 'bold'), width=11, anchor="w", bg='#C04000', fg='white')
l_name_editor_label.grid(row=2, column=0, padx=5, pady=2)

age_editor_label = Label(editor_frame, text="Age", borderwidth=2, relief=GROOVE, font=(
    'Arial', '11', 'bold'), width=11, anchor="w", bg='#C04000', fg='white')
age_editor_label.grid(row=3, column=0, padx=5, pady=2)

gender_editor_label = Label(editor_frame, text="Gender", borderwidth=2, relief=GROOVE, font=(
    'Arial', '11', 'bold'), width=11, anchor="w", bg='#C04000', fg='white')
gender_editor_label.grid(row=4, column=0, padx=5, pady=2)

pin_editor_label = Label(editor_frame, text="Pin", borderwidth=2, relief=GROOVE, font=(
    'Arial', '11', 'bold'), width=11, anchor="w", bg='#C04000', fg='white')
pin_editor_label.grid(row=6, column=0, padx=5, pady=2)

re_pin_editor_label = Label(editor_frame, text="Re-pin", borderwidth=2, relief=GROOVE,
                            font=('Arial', '11', 'bold'), width=11, anchor="w", bg='#C04000', fg='white')
re_pin_editor_label.grid(row=7, column=0, padx=5, pady=2)

father_name_editor_label = Label(editor_frame, text="Father Name", borderwidth=2, relief=GROOVE, font=(
    'Arial', '11', 'bold'), width=11, anchor="w", bg='#C04000', fg='white')
father_name_editor_label.grid(row=8, column=0, padx=5, pady=2)

phone_editor_label = Label(editor_frame, text="Phone", borderwidth=2, relief=GROOVE, font=(
    'Arial', '11', 'bold'), width=11, anchor="w", bg='#C04000', fg='white')
phone_editor_label.grid(row=9, column=0, padx=5, pady=2)

address_editor_label = Label(editor_frame, text="Address", borderwidth=2, relief=GROOVE, font=(
    'Arial', '11', 'bold'), width=11, anchor="w", bg='#C04000', fg='white')
address_editor_label.grid(row=10, column=0, padx=5, pady=2)

city_editor_label = Label(editor_frame, text="City", borderwidth=2, relief=GROOVE, font=(
    'Arial', '11', 'bold'), width=11, anchor="w", bg='#C04000', fg='white')
city_editor_label.grid(row=11, column=0, padx=5, pady=2)

zipcode_editor_label = Label(editor_frame, text="zipcode", borderwidth=2, relief=GROOVE, font=(
    'Arial', '11', 'bold'), width=11, anchor="w", bg='#C04000', fg='white')
zipcode_editor_label.grid(row=12, column=0, padx=5, pady=2)

'''
ENTRY
'''
# Create text entries
f_name_editor = Entry(editor_frame, width=32, bg='white')
f_name_editor.grid(row=1, column=1, padx=5)

l_name_editor = Entry(editor_frame, width=32)
l_name_editor.grid(row=2, column=1, padx=5)

age_editor = Entry(editor_frame, width=32)
age_editor.grid(row=3, column=1, padx=5)


# set the Menu initially
gender = StringVar()
gender.set("Gender")

# creating dropdown menu
drop = OptionMenu(editor_frame, gender, "Male", "Female", "Other")
drop.grid(row=4, column=1, padx=5)

pin_editor = Entry(editor_frame, width=32, show="*")
pin_editor.grid(row=6, column=1, padx=5)

re_pin_editor = Entry(editor_frame, width=32, show="*")
re_pin_editor.grid(row=7, column=1, padx=5)

father_name_editor = Entry(editor_frame, width=32)
father_name_editor.grid(row=8, column=1, padx=5)

phone_editor = Entry(editor_frame, width=32)
phone_editor.grid(row=9, column=1, padx=5)

address_editor = Entry(editor_frame, width=32)
address_editor.grid(row=10, column=1, padx=5)

city_editor = Entry(editor_frame, width=32)
city_editor.grid(row=11, column=1, padx=5)

zipcode_editor = Entry(editor_frame, width=32)
zipcode_editor.grid(row=12, column=1, padx=5)


delete_box_label = Label(editor_frame, text="ID-delete/update",
                         width=15, anchor="w", bg="red", fg='black')
delete_box_label.grid(row=13, column=0, pady=2)

delete_box = Entry(editor_frame, width=32, bg='grey', fg='white')
delete_box.grid(row=13, column=1, pady=2)

delete_box_btn = Button(editor_frame, text="DELETE", font=(
    'Arial', '20', 'bold'), bg='red', command=delete)
delete_box_btn.grid(row=14, column=0, columnspan=2, pady=1, padx=0, ipadx=120)


# Create update button
edit_box_btn = Button(editor_frame, text="UPDATE", font=(
    'Arial', '20', 'bold'), bg='#046307', fg='white', command=update_func)
edit_box_btn.grid(row=15, column=0, columnspan=2, pady=1, padx=10, ipadx=120)


'''FRAME'''
# Create  Back Frame
back_frame = Frame(root, width=50, height=50)
back_frame.place(x=1265, y=630)

# back button
back = Image.open("img/Back.png")
resized_back_image = back.resize((90, 90))
converted_back_image = ImageTk.PhotoImage(resized_back_image)

back_button = Button(back_frame, image=converted_back_image, text="BACK", font=(
    'Arial', '11', 'bold'), bg='white', compound='top', pady=10, command=backspace)
back_button.grid(row=0, column=0)

'''
Update Frame
'''

'''WALLPAPER'''
# setting photo as background


def resize_image1(event):
    new_width = event.width
    new_height = event.height
    image = copy_of_image.resize((new_width, new_height))
    photo = ImageTk.PhotoImage(image)
    label.config(image=photo)
    label.image = photo  # avoid garbage collection


image1 = Image.open('img/edit_bg.jpg')
copy_of_imageq = image1.copy()
photo1 = ImageTk.PhotoImage(image1)
label = ttk.Label(update_frame, image=photo1)
label.bind('<Configure>', resize_image)
label.pack(fill=BOTH, expand=YES)


'''FRAME'''
'''Arrangement by GRID'''
# Create Frame
editor_frame1 = Frame(update_frame, width=150, height=500,
                      highlightthickness=10, highlightbackground='yellow')
editor_frame1.place(x=480, y=250)


'''LABELS'''
# Create textbox labels and image labels
staff_profile1 = Image.open("img/user_photo.png")
resized_image1 = staff_profile1.resize((50, 50))
converted_image1 = ImageTk.PhotoImage(resized_image1)
myLabel = Label(editor_frame1, image=converted_image1,
                text="EDIT STAFF DATA", font=('Arial', '20', 'bold'), compound='left')

myLabel.grid(row=0, column=0, columnspan=2)

# DATABASES
# create a database or connect to one
conn = sqlite3.connect('CRISTY_RECORD.db')

# create a cursor
'''
cursor class is an instance using which you can invoke methods that execute 
SQLite3 statements, fetch data from the result sets of the queries
'''
c = conn.cursor()


def edit_update():
    '''This function updates staff data'''
    conn = sqlite3.connect('CRISTY_RECORD.db')
    c = conn.cursor()
    c.execute("UPDATE Staff SET f_name=?,l_name=?,age=?,gender=?,pin=?,father_name=?,phone=?,address=?,city=?,zipcode=? WHERE Status='active'",
              (f_name_editor1.get(), l_name_editor1.get(), age_editor1.get(),gender1.get(),
               pin_editor1.get(), father_name_editor1.get(), phone_editor1.get(),
                address_editor1.get(), city_editor1.get(), zipcode_editor1.get()))
    conn.commit()
    conn.close()
    print("Updated")
    messagebox.showinfo("Success", "Updated Successfully")
    return


def edit_delete():
    '''This function deletes staff data'''
    conn = sqlite3.connect('CRISTY_RECORD.db')
    c = conn.cursor()

    c.execute("DELETE FROM Staff WHERE status='active' ")
    conn.commit()
    conn.close()
    messagebox.showinfo('Success','Deleted Sucessfuuly')


'''
Labels
'''


# Create textbox labels
f_name_editor_label = Label(editor_frame1, text="First Name", borderwidth=2, relief=GROOVE, font=(
    'Arial', '11', 'bold'), width=11, anchor="w", bg='#C04000', fg='white')
f_name_editor_label.grid(row=1, column=0, padx=5, pady=2)

l_name_editor_label = Label(editor_frame1, text="Last Name", borderwidth=2, relief=GROOVE, font=(
    'Arial', '11', 'bold'), width=11, anchor="w", bg='#C04000', fg='white')
l_name_editor_label.grid(row=2, column=0, padx=5, pady=2)

age_editor_label = Label(editor_frame1, text="Age", borderwidth=2, relief=GROOVE, font=(
    'Arial', '11', 'bold'), width=11, anchor="w", bg='#C04000', fg='white')
age_editor_label.grid(row=3, column=0, padx=5, pady=2)

gender_editor_label = Label(editor_frame1, text="Gender", borderwidth=2, relief=GROOVE, font=(
    'Arial', '11', 'bold'), width=11, anchor="w", bg='#C04000', fg='white')
gender_editor_label.grid(row=4, column=0, padx=5, pady=2)

pin_editor_label = Label(editor_frame1, text="Pin", borderwidth=2, relief=GROOVE, font=(
    'Arial', '11', 'bold'), width=11, anchor="w", bg='#C04000', fg='white')
pin_editor_label.grid(row=6, column=0, padx=5, pady=2)

re_pin_editor_label = Label(editor_frame1, text="Re-pin", borderwidth=2, relief=GROOVE,
                            font=('Arial', '11', 'bold'), width=11, anchor="w", bg='#C04000', fg='white')
re_pin_editor_label.grid(row=7, column=0, padx=5, pady=2)

father_name_editor_label = Label(editor_frame1, text="Father Name", borderwidth=2, relief=GROOVE, font=(
    'Arial', '11', 'bold'), width=11, anchor="w", bg='#C04000', fg='white')
father_name_editor_label.grid(row=8, column=0, padx=5, pady=2)

phone_editor_label = Label(editor_frame1, text="Phone", borderwidth=2, relief=GROOVE, font=(
    'Arial', '11', 'bold'), width=11, anchor="w", bg='#C04000', fg='white')
phone_editor_label.grid(row=9, column=0, padx=5, pady=2)

address_editor_label = Label(editor_frame1, text="Address", borderwidth=2, relief=GROOVE, font=(
    'Arial', '11', 'bold'), width=11, anchor="w", bg='#C04000', fg='white')
address_editor_label.grid(row=10, column=0, padx=5, pady=2)

city_editor_label = Label(editor_frame1, text="City", borderwidth=2, relief=GROOVE, font=(
    'Arial', '11', 'bold'), width=11, anchor="w", bg='#C04000', fg='white')
city_editor_label.grid(row=11, column=0, padx=5, pady=2)

zipcode_editor_label = Label(editor_frame1, text="zipcode", borderwidth=2, relief=GROOVE, font=(
    'Arial', '11', 'bold'), width=11, anchor="w", bg='#C04000', fg='white')
zipcode_editor_label.grid(row=12, column=0, padx=5, pady=2)

'''
ENTRY
'''
# Create text entries
f_name_editor1 = Entry(editor_frame1, width=32, bg='white')
f_name_editor1.grid(row=1, column=1, padx=5)

l_name_editor1 = Entry(editor_frame1, width=32)
l_name_editor1.grid(row=2, column=1, padx=5)

age_editor1 = Entry(editor_frame1, width=32)
age_editor1.grid(row=3, column=1, padx=5)

1
# set the Menu initially
gender1 = StringVar()
gender1.set("Gender")

# creating dropdown menu
drop1 = OptionMenu(editor_frame1, gender1, "Male", "Female", "Other")
drop1.grid(row=4, column=1, padx=5)

pin_editor1 = Entry(editor_frame1, width=32, show="*")
pin_editor1.grid(row=6, column=1, padx=5)

re_pin_editor1 = Entry(editor_frame1, width=32, show="*")
re_pin_editor1.grid(row=7, column=1, padx=5)

father_name_editor1 = Entry(editor_frame1, width=32)
father_name_editor1.grid(row=8, column=1, padx=5)

phone_editor1 = Entry(editor_frame1, width=32)
phone_editor1.grid(row=9, column=1, padx=5)

address_editor1 = Entry(editor_frame1, width=32)
address_editor1.grid(row=10, column=1, padx=5)

city_editor1 = Entry(editor_frame1, width=32)
city_editor1.grid(row=11, column=1, padx=5)

zipcode_editor1 = Entry(editor_frame1, width=32)
zipcode_editor1.grid(row=12, column=1, padx=5)


# Create update button
edit_box_btn = Button(editor_frame1, text="UPDATE", font=(
    'Arial', '20', 'bold'), bg='#046307', fg='white', command=edit_update)
edit_box_btn.grid(row=15, column=0, columnspan=2, pady=1, padx=10, ipadx=120)

del_box_btn = Button(editor_frame1, text="DELETE", font=(
    'Arial', '20', 'bold'), bg='#046307', fg='white', command=edit_delete)
del_box_btn.grid(row=16, column=0, columnspan=2, pady=1, padx=10, ipadx=120)

'''FRAME'''
# Create  Back Frame
back_frame = Frame(update_frame, width=50, height=50)
back_frame.place(x=1265, y=630)

# back button
back1 = Image.open("img/Back.png")
resized_back_image1 = back1.resize((90, 90))
converted_back_image1 = ImageTk.PhotoImage(resized_back_image1)

back_button = Button(back_frame, image=converted_back_image1, text="BACK", font=(
    'Arial', '11', 'bold'), bg='white', compound='top', pady=10, command=root_func)
back_button.grid(row=0, column=0)


conn = sqlite3.connect('CRISTY_RECORD.db')
c = conn.cursor()
c.execute("SELECT * FROM Staff WHERE status='active'")
if c.fetchall:
    # fetching the data from the database
    data = c.fetchall()
    for i in data:
        f_name_editor1.insert(0, i[0])
        l_name_editor1.insert(0, i[1])
        age_editor1.insert(0, i[2])
        gender1.set(i[3])
        pin_editor1.insert(0, i[4])
        re_pin_editor1.insert(0, i[4])
        father_name_editor1.insert(0, i[6])
        phone_editor1.insert(0, i[7])
        address_editor1.insert(0, i[8])
        city_editor1.insert(0, i[9])
        zipcode_editor1.insert(0, i[10])


# commit change
conn.commit()

# # close connection
conn.close()

# running the project till it is closed
mainloop()
