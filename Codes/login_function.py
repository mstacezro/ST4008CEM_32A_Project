def login():
    conn=sqlite3.connect('RECORD.db')#connect to our database
    c=conn.cursor()
    pin_check=pin.get()#get entry from the respective entry boxes.
    id_check=manager_id.get()
    c.execute("SELECT *From Manager WHERE username :username AND password :password",
              {'pin_check':pin,'id_check':manager_id})
    if c.fetchone():
        mesagebox.showinfo('Success', 'login successful')
        home.destroy()
        os.system('python """ENter file name"""')#The respective file pops up after the login is successful
    else:
        messageox.showinfo('Error','login failed')
        pin.delete(0,END)
        manager_id.delete(0,END)
    
        