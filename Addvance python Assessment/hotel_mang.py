from Check_in import *
from tkinter import *
root=Tk()

root.geometry("600x500")
# f1=Frame(root,bg="gray",borderwidth=5)
# f1.pack()

l1=Label(root,text="WELCOME",bg="grey",fg="black",font=("bold",35),padx=655)
l1.grid(row=0)

b1=Button(root,text="1.Check In",borderwidth=3,bg="grey",fg="black",padx=140,pady=10,font=("robot",25,"bold"),command=fun1)
b1.place(x=500,y=80,height=100)

b1=Button(root,text="2.Show Guest List",borderwidth=3,bg="grey",fg="black",padx=80,pady=10,font=("robot",25,"bold"))
b1.place(x=500,y=210,height=100)

b1=Button(root,text="3.Check Out",borderwidth=3,bg="grey",fg="black",padx=125,pady=10,font=("robot",25,"bold"))
b1.place(x=500,y=340,height=100)

b1=Button(root,text="4.Get Info Of Any Guest",borderwidth=3,bg="grey",fg="black",padx=35,pady=10,font=("robot",25,"bold"))
b1.place(x=500,y=470,height=100)

b1=Button(root,text="5.Exit",borderwidth=3,bg="grey",fg="black",padx=176,pady=10,font=("robot",25,"bold"))
b1.place(x=500,y=600,height=100)

L2=Label(root,text="HOTEL MANAGMENT",fg="black",font=("time new roman",37,"bold"))
L2.place(x=1010,y=80,height=100)

L2=Label(root,text="PYTHON TKINTER",fg="black",font=("time new roman",37,"bold"))
L2.place(x=1040,y=210,height=100)

L2=Label(root,text="GUI",fg="black",font=("time new roman",150,"bold"))
L2.place(x=1060,y=340,height=200)

root=mainloop()