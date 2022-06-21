from tkinter import *
from tkinter import ttk

root=Tk()
root.title("Menu")
notebook=ttk.Notebook(root)#widget that 
tab1= Frame(notebook) #tab1
tab2= Frame(notebook)#tab2
tab3= Frame(notebook)#tab3
tab4= Frame(notebook)#tab4
tab5= Frame(notebook)#tab5
tab6= Frame(notebook)#tab6
tab7= Frame(notebook)#tab7
tab8= Frame(notebook)#tab8
tab9= Frame(notebook)#tab9
tab10= Frame(notebook)#tab10
notebook.add(tab1,text="Menu")
notebook.add(tab2,text="Order status")
notebook.add(tab3,text="Table")
notebook.add(tab4,text="Members")
notebook.add(tab5,text="Combi")
notebook.add(tab6,text="Premium Burger")
notebook.add(tab7,text="Side Dish")
notebook.add(tab8,text="Beverage")
notebook.add(tab9,text="Desserts")
notebook.add(tab10,text="Other")
notebook.pack()
Label(tab1,text="Hello, this is tab1",width=50,height=25).pack()
Label(tab2,text="Hello, this is tab2",width=50,height=25).pack()
Label(tab3,text="Hello, this is tab3",width=50,height=25).pack()
Label(tab4,text="Hello, this is tab4",width=50,height=25).pack()
Label(tab5,text="Hello, this is tab5",width=50,height=25).pack()
Label(tab6,text="Hello, this is tab6",width=50,height=25).pack()
Label(tab7,text="Hello, this is tab7",width=50,height=25).pack()
Label(tab8,text="Hello, this is tab8",width=50,height=25).pack()
Label(tab9,text="Hello, this is tab9",width=50,height=25).pack()
Label(tab10,text="Hello, this is tab10",width=50,height=25).pack()

button=Button(root, text='Item 1').place(x=100, y=30, width=90, height=45)
button=Button(root, text='Item 1a').place(x=100, y=80, width=90, height=45)
button=Button(root, text='Item 1b').place(x=100, y=150, width=90, height=45)
button=Button(root, text='Item 1c').place(x=100, y=250, width=90, height=45)

button=Button(root, text='Item 2').place(x=250, y=30, width=90, height=45)
button=Button(root, text='Item 2a').place(x=250, y=80, width=90, height=45)
button=Button(root, text='Item 2b').place(x=250, y=150, width=90, height=45)
button=Button(root, text='Item 2c').place(x=250, y=250, width=90, height=45)

button=Button(root, text='Item 3').place(x=400, y=30, width=90, height=45)
button=Button(root, text='Item 3a').place(x=400, y=80, width=90, height=45)
button=Button(root, text='Item 3b').place(x=400, y=150, width=90, height=45)
button=Button(root, text='Item 3c').place(x=400, y=250, width=90, height=45)

root.mainloop()