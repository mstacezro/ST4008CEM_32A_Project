# import tkinter module to the program
from itertools import product
import profile
from tkinter import*
from tkinter import ttk
from tkinter import font
from tkinter.font import BOLD
from turtle import width
from PIL import Image, ImageTk
import sqlite3
import os
from tkinter import messagebox

conn=sqlite3.connect('CRISTY_RECORD.db')
c=conn.cursor()

# create an application window
root= Tk()

#create the root title for the project
root.title("POS")


#default fullscreen
root.attributes('-fullscreen',True)

def backspace():
    '''This function logouts the active user staff. The result is the inactive status of the user'''
    ask=messagebox.askyesno('Logout','DO YOU WANT TO LOGOUT?')
    if ask==True:
        conn=sqlite3.connect('CRISTY_RECORD.db')
        c=conn.cursor()
        
        c.execute("SELECT * FROM Staff WHERE status='active'")
        if c.fetchall():
            c.execute("UPDATE Staff SET status='inactive'")
            conn.commit()
            messagebox.showinfo('Success','Logout Successfully')
            root.destroy()
            os.system('python staff_login.py')
        conn.commit()
        conn.close()
    else:
        pass

#setting photo as background
def resize_image(event):
    new_width = event.width
    new_height = event.height
    image = copy_of_image.resize((new_width, new_height))
    photo = ImageTk.PhotoImage(image)
    label.config(image = photo)
    label.image = photo #avoid garbage collection

image = Image.open('img/menu_bg.jpg')
copy_of_image = image.copy()
photo = ImageTk.PhotoImage(image)
label = ttk.Label(root, image = photo)
label.bind('<Configure>', resize_image)
label.pack(fill=BOTH, expand = YES)

#defining a string variable 
scvalue=StringVar()
scvalue.set("") #setting initial value of string variable as blank

def setTextInput(text):
    '''THis function inputs the name of the product in the product entry in order box by clicking the item'''
    product_entry.delete(0,"end")
    product_entry.insert(0, text)

def order_add():
    ''''''
    '''
    This function adds order details as data to the bill table
    '''
    global total_amount
    qty=quantity_dropdown.get()
    #connect to the database 
    conn=sqlite3.connect('CRISTY_RECORD.db')

    #create cursor
    c=conn.cursor()

    '''INSERT INTO Statement is used to add new rows of data into a table in the database.'''
    #the values of attributes is obtained by .get() from respective entry box
    try:
        c.execute("SELECT * FROM Product WHERE product_name=? ",(product_entry.get(),))
        
        data=c.fetchall()
        for i in data:
            name=i[0]
            price=i[1]
            total=int(qty)*int(price)
        c.execute("INSERT INTO order_table(product_name,quantity,price,total_price) VALUES(?,?,?,?)",(name,qty,price,total))
        cart_treeview.insert('',END,values=(name,price,qty,total))
        total_amount=0
        c.execute("SELECT * FROM order_table")
        data=c.fetchall()
        for i in data:
            total_amount=total_amount+i[4]
        total_amount_place.config(text='Rs'+(total_amount))
        messagebox.showinfo('Success','Added Successfully')
    except:
        c.execute("SELECT * FROM Product WHERE product_name=? ",(food_dropbox.get(),))
        
        data=c.fetchall()
        if data!=[]:
            for i in data:
                name=i[0]
                price=i[1]
                total=int(qty)*int(price)
        

            c.execute("INSERT INTO order_table(product_name,quantity,price,total_price) VALUES(?,?,?,?)",(name,qty,price,total))
            cart_treeview.insert('',END,values=(name,price,qty,total))
            total_amount=0
            c.execute("SELECT * FROM order_table")
            data=c.fetchall()
            for i in data:
                total_amount=total_amount+i[4]
            total_amount_place.config(text='Rs'+str(total_amount))
            messagebox.showinfo('Success','Added Successfully')
        else:
            messagebox.showinfo('Error','Product Not Found')

   
    '''
    Once you are done with your changes and you want to commit the changes 
    then call .commit() method on connection object 
    '''
    #commit changes
    conn.commit()
    #close connection
    conn.close()

    #clear the text boxes
    product_entry.delete(0,END)

    quantity_dropdown.delete(0,END)

    
def takeaway():
    '''This function is for choosing takeaway as a delivery'''
    global total_amount
    conn=sqlite3.connect('CRISTY_RECORD.db')
    c=conn.cursor()
    c.execute("SELECT * FROM order_table")
    if c.fetchall():
        order_status_tree.delete(*order_status_tree.get_children())
        conn=sqlite3.connect('CRISTY_RECORD.db')
        c=conn.cursor()
        c.execute("INSERT INTO Bill(status,takeaway,bill_total) VALUES('incomplete','Yes',?)",(total_amount,))

        conn.commit()
        c.execute("SELECT * FROM Bill")
        data=c.fetchall()
        for i in data:
            order_status_tree.insert('',END,values=(i[0],i[3],i[4],i[5]))

        c.execute("DELETE FROM order_table")
        conn.commit()
        conn.close()
        cart_treeview.delete(*cart_treeview.get_children())
        total_amount=0
        total_amount_place.config(text='Rs'+str(total_amount))
        messagebox.showinfo('Success','Order Placed Successfully')
    else:
        messagebox.showinfo('Failure','Empty cart')
def Dine_IN():
    '''This function is for choosing dine-in as a delivery'''
    global total_amount
    order_status_tree.delete(*order_status_tree.get_children())
    conn=sqlite3.connect('CRISTY_RECORD.db')
    c=conn.cursor()
    c.execute("INSERT INTO Bill(status,Dine_in,bill_total) VALUES('incomplete','Yes',?)",(total_amount,))

    conn.commit()
    c.execute("SELECT * FROM Bill")
    data=c.fetchall()
    for i in data:
        order_status_tree.insert('',END,values=(i[0],i[3],i[4],i[5]))

    c.execute("DELETE FROM order_table")
    conn.commit()
    conn.close()
    cart_treeview.delete(*cart_treeview.get_children())
    total_amount=0
    total_amount_place.config(text='Rs'+str(total_amount))
    messagebox.showinfo('Success','Order Placed Successfully')

        

'''FRAMES for different sections'''
'''frame for date/time'''


'''frame for date/time/info/logout'''
top_frame = Frame(root,width=900,height=100)
top_frame.place(x=1270,y=10)
# top_frame.place(x=1060,y=10)


# #info button
# manager_info=Image.open("img/information.png")
# resized_info_image=manager_info.resize((90,90))
# converted_info_image=ImageTk.PhotoImage(resized_info_image)

# information=Button(top_frame,image=converted_info_image, text="INFO",font=('Arial','11','bold'),bg='white',compound='top',pady=20,command=NONE)
# information.grid(row=0,column=0)

# #edit button
# manager_edit=Image.open("img/edit.png")
# resized_edit_image=manager_edit.resize((90,90))
# converted_edit_image=ImageTk.PhotoImage(resized_edit_image)

# edit=Button(top_frame,image=converted_edit_image, text="EDIT",font=('Arial','11','bold'),bg='white',compound='top',pady=20,command=NONE)
# edit.grid(row=0,column=1)

#logout button
manager_logout=Image.open("img/logout.png")
resized_logout_image=manager_logout.resize((90,90))
converted_logout_image=ImageTk.PhotoImage(resized_logout_image)

logout=Button(top_frame,image=converted_logout_image, text="LOGOUT",font=('Arial','11','bold'),bg='white',compound='top',pady=20,command=backspace)
logout.grid(row=0,column=2)



'''
Menu frame
'''



""" Frame for order"""
order_frame = Frame(root,width=245,height=600)
order_frame.place(x=655,y=160)

order_label=Label(order_frame, text="ORDERS",font=('Arial','20','bold'),width=16,bg='green')
order_label.grid(row=0,column=0)

product_label=Label(order_frame, text="Product Name",font=('Arial','11','bold'),width=30,bg='grey')
product_label.grid(row=1,column=0,pady=1)

product_entry=Entry(order_frame,textvar=scvalue, width=30)
product_entry.grid(row=2,column=0,pady=1)


quantity_label=Label(order_frame, text="Quantity",font=('Arial','11','bold'),width=30,bg='grey')
quantity_label.grid(row=5,column=0,pady=1)

quantity_list=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
quantity_dropdown=ttk.Combobox(order_frame,values=quantity_list,state='readonly')
quantity_dropdown.current(0)
quantity_dropdown.grid(row=6,column=0,pady=1)


# Create add button
add_box_btn=Button(order_frame,text="ADD",font=('Arial','15','bold'),bg='blue',fg='white',width=16,command=order_add)
add_box_btn.grid(row=9,column=0,pady=1 )



def delete():
    '''THis function deletes a product in ongoing order'''
    global total_amount
    selected_item=cart_treeview.selection()[0]
    item=cart_treeview.item(selected_item)['values'][0]
    conn=sqlite3.connect('CRISTY_RECORD.db')
    c=conn.cursor()
    c.execute("DELETE FROM order_table WHERE product_name=?",(item,))
    conn.commit()
    conn.close()
    cart_treeview.delete(*cart_treeview.get_children())
    conn=sqlite3.connect('CRISTY_RECORD.db')
    c=conn.cursor()
    c.execute("SELECT * FROM order_table")
    data=c.fetchall()
    total_amount=0
    for i in data:
        cart_treeview.insert('',END,values=(i[1],i[3],i[2],i[4]))
        total_amount+=int(i[4])
    total_amount_place.config(text='Rs'+str(total_amount))
    conn.commit()
    conn.close()
    messagebox.showinfo('Success','Deleted Successfully')

# Create delete button
delete_box_btn=Button(order_frame,text="DELETE",font=('Arial','15','bold'),bg='red',width=16,command=delete)
delete_box_btn.grid(row=12,column=0,pady=1)

# Create list
list_food=[]
conn=sqlite3.connect('CRISTY_RECORD.db')
c=conn.cursor()

#dropbox for special foods in product etails
c.execute('SELECT * FROM Product')
data=c.fetchall()
for i in  data:
    list_food.append(i[0])
food_dropbox=ttk.Combobox(order_frame,values=list_food,state='readonly',width=30)
food_dropbox.grid(row=13,column=0)
food_dropbox.set('Special')

#image of order
order_photo=Image.open("img/gui_order.png")
size_order_photo=order_photo.resize((300,300))
converted_order_image=ImageTk.PhotoImage(size_order_photo)

order_photo_label=Label(order_frame,image=converted_order_image)
order_photo_label.grid(row=17,column=0)



def clear():
    '''This functio clears the order bill table'''
    cart_treeview.delete(*cart_treeview.get_children())
    conn=sqlite3.connect('CRISTY_RECORD.db')
    c=conn.cursor()

    c.execute('DELETE FROM order_table')
    messagebox.showinfo('Delete','Deleted Successfully')
    conn.commit()
    conn.close()
# Create clear button
clear_box_btn=Button(order_frame,text="CLEAR",font=('Arial','15','bold'),bg='yellow',fg='red',width=16,command=clear)
clear_box_btn.grid(row=14,column=0,pady=1 )

""" Frame for billing"""
bill_frame = Frame(root,width=600,height=800)
bill_frame.place(x=940,y=160)

columns=('Product','Rate','Quantity','Total')
cart_treeview=ttk.Treeview(bill_frame,columns=columns,show='headings',height=18)

cart_treeview.column('#1',anchor=CENTER,width=150)
cart_treeview.column('# 2',anchor=CENTER,stretch=NO,width=30)
cart_treeview.column('# 3',anchor=CENTER,stretch=NO,width=30)
cart_treeview.column('# 2',anchor=CENTER,stretch=NO,width=50)


# define headings
# cart_treeview.heading('S.N.',text='S.N.')
cart_treeview.heading('Product', text='Product')
cart_treeview.heading('Rate', text='Rate')
cart_treeview.heading('Quantity', text='Qty')
cart_treeview.heading('Total', text='Total')

cart_treeview.place(x=0,y=0)


total_amount_label=Label(bill_frame,text='Total amount :')
total_amount_label.place(x=0,y=400)

total_amount_place=Label(bill_frame,text='Rs '+str(0))
total_amount_place.place(x=200,y=400)

takeaway_btn=Button(bill_frame,text='Takeaway',font=('Arial','15','bold'),bg='#046307',fg='white',width=16,command=takeaway,padx=5,pady=20)
takeaway_btn.place(x=0,y=450)

Dine_IN_btn=Button(bill_frame,text='Dine IN',font=('Arial','15','bold'),bg='#046307',fg='white',width=16,command=Dine_IN, padx=5,pady=20)
Dine_IN_btn.place(x=200,y=450)
'''
TAB frame'''
tab_frame = Frame(root,width=800,height=600)
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


burger1=Image.open("img/BuffBurger.PNG")
resized_burger1=burger1.resize((200,150))
converted_burger1=ImageTk.PhotoImage(resized_burger1)

burger1=Button(burger_tab,image=converted_burger1, text="Buff Burger",font=('Arial','11','bold'),bg='white',compound='top',pady=20,command=lambda:setTextInput('Buff Burger'))
burger1.grid(row=0,column=0,padx=2,pady=1)

burger1_label=Label(burger_tab, text="Rs 200",font=('Arial','11','bold'),width=22,bg='white',pady=20)
burger1_label.grid(row=1,column=0)


burger2=Image.open("img/ChickenBurger.PNG")
resized_burger2=burger2.resize((200,150))
converted_burger2=ImageTk.PhotoImage(resized_burger2)

burger1=Button(burger_tab,image=converted_burger2, text="Chicken Burger",font=('Arial','11','bold'),bg='white',compound='top',pady=20,command=lambda:setTextInput("Chicken Burger"))
burger1.grid(row=0,column=1,padx=2,pady=1)


burger2_label=Label(burger_tab, text="Rs 200",font=('Arial','11','bold'),width=22,bg='white',pady=20)
burger2_label.grid(row=1,column=1)

burger3=Image.open("img/EggBurger.PNG")
resized_burger3=burger3.resize((200,150))
converted_burger3=ImageTk.PhotoImage(resized_burger3)

burger1=Button(burger_tab,image=converted_burger3, text="Egg Burger",font=('Arial','11','bold'),bg='white',compound='top',pady=20,command=lambda:setTextInput("Egg Burger"))
burger1.grid(row=2,column=0,padx=2,pady=1)


burger3_label=Label(burger_tab, text="Rs 150",font=('Arial','11','bold'),width=22,bg='white',pady=20)
burger3_label.grid(row=3,column=0)

burger4=Image.open("img/VeggieBurger.PNG")
resized_burger4=burger4.resize((200,150))
converted_burger4=ImageTk.PhotoImage(resized_burger4)

burger1=Button(burger_tab,image=converted_burger4, text="Fish Burger ",font=('Arial','11','bold'),bg='white',compound='top',pady=20,command=lambda:setTextInput("Fish Burger"))
burger1.grid(row=0,column=2,padx=2,pady=1)

burger4_label=Label(burger_tab, text="Rs 200",font=('Arial','11','bold'),width=22,bg='white',pady=20)
burger4_label.grid(row=1,column=2)

burger5=Image.open("img/VeggieBurger.PNG")
resized_burger5=burger5.resize((200,150))
converted_burger5=ImageTk.PhotoImage(resized_burger5)

burger1=Button(burger_tab,image=converted_burger5, text="Veg Burger",font=('Arial','11','bold'),bg='white',compound='top',pady=20,command=lambda:setTextInput("Veg Burger"))
burger1.grid(row=2,column=1,padx=2,pady=1)

burger5_label=Label(burger_tab, text="Rs 200",font=('Arial','11','bold'),width=22,bg='white',pady=20)
burger5_label.grid(row=3,column=1)

burger6=Image.open("img/PorkBurger.png")
resized_burger6=burger6.resize((200,150))
converted_burger6=ImageTk.PhotoImage(resized_burger6)

burger1=Button(burger_tab,image=converted_burger6, text="Pork Burger",font=('Arial','11','bold'),bg='white',compound='top',pady=20,command=lambda:setTextInput("Pork Burger"))
burger1.grid(row=2,column=2,padx=2,pady=1)

burger6_label=Label(burger_tab, text="Rs 200",font=('Arial','11','bold'),width=22,bg='white',pady=20)
burger6_label.grid(row=3,column=2)

'''SIDE DISHbuttons'''

sideDish1=Image.open("img/Fries.PNG")
resized_sideDish1=sideDish1.resize((200,150))
converted_sideDish1=ImageTk.PhotoImage(resized_sideDish1)

sideDish1=Button(sideDish_tab,image=converted_sideDish1, text="Fries",font=('Arial','11','bold'),bg='white',compound='top',pady=20,command=lambda:setTextInput("Fries"))
sideDish1.grid(row=0,column=0,padx=2,pady=1)

sideDish1_label=Label(sideDish_tab, text="Rs 100",font=('Arial','11','bold'),width=22,bg='white',pady=20)
sideDish1_label.grid(row=1,column=0)

sideDish2=Image.open("img/ChickenWings.png")
resized_sideDish2=sideDish2.resize((200,150))
converted_sideDish2=ImageTk.PhotoImage(resized_sideDish2)

sideDish2=Button(sideDish_tab,image=converted_sideDish2, text="Chicken Wings",font=('Arial','11','bold'),bg='white',compound='top',pady=20,command=lambda:setTextInput("Chicken Wings"))
sideDish2.grid(row=0,column=1,padx=2,pady=1)

sideDish2_label=Label(sideDish_tab, text="Rs 200",font=('Arial','11','bold'),width=22,bg='white',pady=20)
sideDish2_label.grid(row=1,column=1)


sideDish3=Image.open("img/Nuggets.png")
resized_sideDish3=sideDish3.resize((200,150))
converted_sideDish3=ImageTk.PhotoImage(resized_sideDish3)

sideDish3=Button(sideDish_tab,image=converted_sideDish3, text="Nuggets",font=('Arial','11','bold'),bg='white',compound='top',pady=20,command=lambda:setTextInput("Nuggets"))
sideDish3.grid(row=0,column=2,padx=2,pady=1)

sideDish3_label=Label(sideDish_tab, text="Rs 200",font=('Arial','11','bold'),width=22,bg='white',pady=20)
sideDish3_label.grid(row=1,column=2)


sideDish4=Image.open("img/ApplePie.png")
resized_sideDish4=sideDish4.resize((200,150))
converted_sideDish4=ImageTk.PhotoImage(resized_sideDish4)

sideDish4=Button(sideDish_tab,image=converted_sideDish4, text="Apple Pie",font=('Arial','11','bold'),bg='white',compound='top',pady=20,command=lambda:setTextInput("Apple Pie"))
sideDish4.grid(row=2,column=0,padx=2,pady=1)

sideDish4_label=Label(sideDish_tab, text="Rs 100",font=('Arial','11','bold'),width=22,bg='white',pady=20)
sideDish4_label.grid(row=3,column=0)


sideDish5=Image.open("img/BBQ-Wrap.png")
resized_sideDish5=sideDish5.resize((200,150))
converted_sideDish5=ImageTk.PhotoImage(resized_sideDish5)

sideDish5=Button(sideDish_tab,image=converted_sideDish5, text="BBQ Wrap",font=('Arial','11','bold'),bg='white',compound='top',pady=20,command=lambda:setTextInput("BBQ Wrap"))
sideDish5.grid(row=2,column=1,padx=2,pady=1)

sideDish5_label=Label(sideDish_tab, text="Rs 200",font=('Arial','11','bold'),width=22,bg='white',pady=20)
sideDish5_label.grid(row=3,column=1)


sideDish6=Image.open("img/chickenSalad.png")
resized_sideDish6=sideDish6.resize((200,150))
converted_sideDish6=ImageTk.PhotoImage(resized_sideDish6)

sideDish6=Button(sideDish_tab,image=converted_sideDish6, text="Chicken Salad",font=('Arial','11','bold'),bg='white',compound='top',pady=20,command=lambda:setTextInput("Chicken Salad"))
sideDish6.grid(row=2,column=2,padx=2,pady=1)

sideDish1_label=Label(sideDish_tab, text="Rs 200",font=('Arial','11','bold'),width=22,bg='white',pady=20)
sideDish1_label.grid(row=3,column=2)


'''DRINKS DISHbuttons'''

drinks1=Image.open("img/Coke.png")
resized_drinks1=drinks1.resize((200,150))
converted_drinks1=ImageTk.PhotoImage(resized_drinks1)

drinks1=Button(drinks_tab,image=converted_drinks1, text="Coke",font=('Arial','11','bold'),bg='white',compound='top',pady=20,command=lambda:setTextInput("Coke"))
drinks1.grid(row=0,column=0,padx=2,pady=1)

drinks1_label=Label(drinks_tab, text="Rs 100",font=('Arial','11','bold'),width=22,bg='white',pady=20)
drinks1_label.grid(row=1,column=0)


drinks2=Image.open("img/Fanta.png")
resized_drinks2=drinks2.resize((200,150))
converted_drinks2=ImageTk.PhotoImage(resized_drinks2)

drinks2=Button(drinks_tab,image=converted_drinks2, text="Fanta",font=('Arial','11','bold'),bg='white',compound='top',pady=20,command=lambda:setTextInput("Fanta"))
drinks2.grid(row=0,column=1,padx=2,pady=1)

drinks2_label=Label(drinks_tab, text="Rs 100",font=('Arial','11','bold'),width=22,bg='white',pady=20)
drinks2_label.grid(row=1,column=1)

drinks3=Image.open("img/Sprite.png")
resized_drinks3=drinks3.resize((200,150))
converted_drinks3=ImageTk.PhotoImage(resized_drinks3)

drinks3=Button(drinks_tab,image=converted_drinks3, text="Sprite",font=('Arial','11','bold'),bg='white',compound='top',pady=20,command=lambda:setTextInput("Sprite"))
drinks3.grid(row=0,column=2,padx=2,pady=1)

drinks3_label=Label(drinks_tab, text="Rs 100",font=('Arial','11','bold'),width=22,bg='white',pady=20)
drinks3_label.grid(row=1,column=2)

drinks4=Image.open("img/Chocolate-Frappe.png")
resized_drinks4=drinks4.resize((200,150))
converted_drinks4=ImageTk.PhotoImage(resized_drinks4)

drinks4=Button(drinks_tab,image=converted_drinks4, text="Chocolate Frappe",font=('Arial','11','bold'),bg='white',compound='top',pady=20,command=lambda:setTextInput("Chocolate Frappe"))
drinks4.grid(row=2,column=0,padx=2,pady=1)

drinks4_label=Label(drinks_tab, text="Rs 200",font=('Arial','11','bold'),width=22,bg='white',pady=20)
drinks4_label.grid(row=3,column=0)

drinks5=Image.open("img/Chocolate-Oreo-Frappé.png")
resized_drinks5=drinks5.resize((200,150))
converted_drinks5=ImageTk.PhotoImage(resized_drinks5)

drinks5=Button(drinks_tab,image=converted_drinks5, text="Chocolate Oreo Frappe",font=('Arial','11','bold'),bg='white',compound='top',pady=20,command=lambda:setTextInput("Chocolate Oreo Frappe"))
drinks5.grid(row=2,column=1,padx=2,pady=1)

drinks5_label=Label(drinks_tab, text="Rs 200",font=('Arial','11','bold'),width=22,bg='white',pady=20)
drinks5_label.grid(row=3,column=1)

drinks6=Image.open("img/Vanilla-Frappe.png")
resized_drinks6=drinks6.resize((200,150))
converted_drinks6=ImageTk.PhotoImage(resized_drinks6)

drinks6=Button(drinks_tab,image=converted_drinks6, text="Vanilla Frappe",font=('Arial','11','bold'),bg='white',compound='top',pady=20,command=lambda:setTextInput("Vanilla Frappe"))
drinks6.grid(row=2,column=2,padx=2,pady=1)

drinks6_label=Label(drinks_tab, text="Rs 200",font=('Arial','11','bold'),width=22,bg='white',pady=20)
drinks6_label.grid(row=3,column=2)
print(product_entry.get())

'''
Order Status Tab
'''


columns=('Bill ID','Status','Takeaway','Dine In')
order_status_tree=ttk.Treeview(orderStatus_tab,columns=columns,show='headings')
order_status_tree.place(x=50,y=10)
order_status_tree.column("Bill ID",width=100,anchor='center')
order_status_tree.column("Status",width=200,anchor='center')
order_status_tree.column("Takeaway",width=100,anchor='center')
order_status_tree.column("Dine In",width=100,anchor='center')

order_status_tree.heading("Bill ID",text="Bill ID")
order_status_tree.heading("Status",text="Status")
order_status_tree.heading("Takeaway",text="Takeaway")
order_status_tree.heading("Dine In",text="Dine In")


conn=sqlite3.connect('CRISTY_RECORD.db')
c=conn.cursor()
c.execute("SELECT * FROM Bill")
for i in c.fetchall():
    order_status_tree.insert("",END,values=(i[0],i[3],i[4],i[5]))
conn.commit()
conn.close()

def complete_order():
    '''This function marks the order as complete after the food is delivred'''
    selected_item=order_status_tree.selection()[0]
    selected_bill_id=order_status_tree.item(selected_item)['values'][0]
    conn=sqlite3.connect('CRISTY_RECORD.db')
    c=conn.cursor()
    c.execute("UPDATE Bill SET status='Complete' WHERE Bill_ID=?",(selected_bill_id,))
    conn.commit()
    conn.close()
    order_status_tree.delete(*order_status_tree.get_children())
    conn=sqlite3.connect('CRISTY_RECORD.db')
    c=conn.cursor()
    c.execute("SELECT * FROM Bill")
    for i in c.fetchall():
        order_status_tree.insert("",END,values=(i[0],i[3],i[4],i[5]))
    conn.commit()
    conn.close()
    messagebox.showinfo("Success","Order Completed")

complete_order_button=Button(orderStatus_tab,text="Complete Order",font=('Arial','11','bold'),bg='white',command=complete_order)
complete_order_button.place(x=50,y=400)
#call mainloop to keep the window visible
mainloop()