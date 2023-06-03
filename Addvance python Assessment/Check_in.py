    

from tkinter import *
def fun1():

    root=Tk()

    root.geometry("700x600")

    bg_color="#F5F5F5"

    root.title("Hotel Mangement System")
    list1=Listbox(root,height = 0,width = 100,bg = "white",activestyle = 'dotbox',font = "Helvetica",fg = "yellow")
    list1.pack(side=TOP,pady=3)

    label=Label(list1,text="    YOU CLICKED ON       :      CHECK IN    ",font=("Bahnschrift SemiBold",35,"bold"),pady=10)
    label.pack()


    list2=Listbox(root,height = 10,width = 50,bg = "#F5F5F5",activestyle = 'dotbox',font = "Helvetica")
    list2.pack(pady=3)

    l1=Label(list2,text="ENTER YOUR NAME           :",font=("Bahnschrift SemiBold",15,"bold"),pady=8,padx=50)
    l1.grid(row=0,column=0)

    e1=Entry(list2,bd=1,relief="raised",bg="#F5F5F5")
    e1.grid(row=0,column=1,ipady=9,ipadx=133)

    b1=Button(list2,text="OK",bd=1,relief="raised")
    b1.grid(row=0,column=2,padx=50)

    l1=Label(list2,text="ENTER YOUR ADDRESS     :",font=("Bahnschrift SemiBold",15,"bold"),pady=8,padx=50)
    l1.grid(row=1,column=0)

    e1=Entry(list2,bd=1,relief="raised",bg="#F5F5F5")
    e1.grid(row=1,column=1,ipady=9,ipadx=133)

    b1=Button(list2,text="OK",bd=1,relief="raised")
    b1.grid(row=1,column=2,padx=50)

    l1=Label(list2,text="ENTER YOUR NUMBER      :",font=("Bahnschrift SemiBold",15,"bold"),pady=8,padx=50)
    l1.grid(row=2,column=0)

    e1=Entry(list2,bd=1,relief="raised",bg="#F5F5F5")
    e1.grid(row=2,column=1,ipady=9,ipadx=133)

    b1=Button(list2,text="OK",bd=1,relief="raised")
    b1.grid(row=2,column=2,padx=50)

    l1=Label(list2,text="NUMBER OF DAYS             :",font=("Bahnschrift SemiBold",15,"bold"),pady=8,padx=50)
    l1.grid(row=3,column=0)

    e1=Entry(list2,bd=1,relief="raised",bg="#F5F5F5")
    e1.grid(row=3,column=1,ipady=9,ipadx=133)

    b1=Button(list2,text="OK",bd=1,relief="raised")
    b1.grid(row=3,column=2,padx=50)

    L2=Label(list2,text="CHOOES YOUR ROOM",font=("Bahnschrift SemiBold",15,"bold"),bg="#F5F5F5",pady=15)
    L2.grid(row=4,column=1)

    c1=Checkbutton(list2,text="DELUXE",font=("Bahnschrift SemiBold",15,"bold"))
    c1.grid(row=5,column=0)

    c1=Checkbutton(list2,text="FULL DELUXE",font=("Bahnschrift SemiBold",15,"bold"))
    c1.grid(row=6,column=0)

    c1=Checkbutton(list2,text="GENERAL",font=("Bahnschrift SemiBold",15,"bold"))
    c1.grid(row=5,column=1)

    c1=Checkbutton(list2,text="JOINT",font=("Bahnschrift SemiBold",15,"bold"))
    c1.grid(row=6,column=1)

    L3=Label(list2,text="CHOOSE PAYMENT METHOD",font=("Bahnschrift SemiBold",15,"bold"),bg="#F5F5F5",pady=15)
    L3.grid(row=7,column=1)

    c1=Checkbutton(list2,text="BY CASH",font=("Bahnschrift SemiBold",15,"bold"))
    c1.grid(row=8,column=0)

    c1=Checkbutton(list2,text="BY CREDIT/DEBIT CARD",font=("Bahnschrift SemiBold",15,"bold"))
    c1.grid(row=8,column=1)

    B2=Button(list2,text="SUBMIT",font=("Bahnschrift SemiBold",15,"bold"),padx=0,pady=10)
    B2.place(x=725,y=280)

    list3=Listbox(root,height = 6,width = 78,bg = "#F5F5F5",activestyle = 'dotbox',font = "Helvetica")
    list3.insert(1,"name has been inputed")
    list3.insert(2,"address has been inputed")
    list3.insert(3,"invalid input please input a valid mobile number")
    list3.insert(4,"mobile number has been inputed")
    list3.pack(pady=3)


    root.mainloop()