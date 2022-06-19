# import tkinter module to the program
from tkinter import*
from tkinter import ttk
from tkinter import messagebox

# BUG #add toplevel


# create an application window
root= Tk()
#create the root title for the project
root.title("STAFF REGISTRATION")

#dimension, background color of project
root.geometry("535x700")
root.resizable(0,0)     #nonresizable, for resizable (True,True)
root.config(bg='#3090C7')

#icon 
##NOTE:  root.iconbitmap("*.ico") 


# Create text entries

first_name=Entry(root,width=30,bg='white')
first_name.grid(row=1,column=1,padx=20)

last_name=Entry(root,width=30)
last_name.grid(row=2,column=1)

age=Entry(root,width=30)
age.grid(row=3,column=1)

password=Entry(root,width=30,show="*")
password.grid(row=4,column=1)

re_password=Entry(root,width=30,show="*")
re_password.grid(row=5,column=1)

father_name=Entry(root,width=30)
father_name.grid(row=6,column=1)

phone=Entry(root,width=30)
phone.grid(row=7,column=1)

address=Entry(root,width=30)
address.grid(row=8,column=1)

city=Entry(root,width=30)
city.grid(row=9,column=1)

zipcode=Entry(root,width=30)
zipcode.grid(row=10,column=1)




# Create textbox labels
first_name_label=Label(root,text="First Name",width=25, anchor="w",bg='#C04000',fg='white')
first_name_label.grid(row=1,column=0,padx=20)

last_name_label=Label(root,text="Last Name",width=25, anchor="w",bg='#C04000',fg='white')
last_name_label.grid(row=2,column=0)

age_label=Label(root,text="Age",width=25, anchor="w",bg='#C04000',fg='white')
age_label.grid(row=3,column=0)

password_label=Label(root,text="Password",width=25, anchor="w",bg='#C04000',fg='white')
password_label.grid(row=4,column=0)

re_password_label=Label(root,text="Re-enter Password",width=25, anchor="w",bg='#C04000',fg='white')
re_password_label.grid(row=5,column=0)

father_name_label=Label(root,text="Father Name",width=25, anchor="w",bg='#C04000',fg='white')
father_name_label.grid(row=6,column=0)

phone_label=Label(root,text="Phone Number",width=25, anchor="w",bg='#C04000',fg='white')
phone_label.grid(row=7,column=0)

address_label=Label(root,text="Address",width=25, anchor="w",bg='#C04000',fg='white')
address_label.grid(row=8,column=0)

city_label=Label(root,text="City",width=25, anchor="w",bg='#C04000',fg='white')
city_label.grid(row=9,column=0)

zipcode_label=Label(root,text="zipcode",width=25, anchor="w",bg='#C04000',fg='white')
zipcode_label.grid(row=10,column=0)



# Create submit button    
register_btn=Button(root,text="Register",bg='#046307',fg='white',command=NONE)
register_btn.grid(row=11,column=0,columnspan=2,pady=10,padx=10,ipadx=120)




#running the project till it is closed
mainloop()