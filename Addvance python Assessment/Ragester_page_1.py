from tkinter import *
root=Tk()
root.geometry("700x600")

def data():
    print(f"Name is : {Name.get()}\nContact is : {contact.get()}\nEmail is : {Email.get()}\nGender is : {Gen.get()}\nCity is : {selcton1.get()}\nState is : {selcton2.get()}")

Name=StringVar()
contact=StringVar()
contact.set("+91 ")
Email=StringVar()
Male=IntVar()
Female=IntVar()
Gen=StringVar()
Gen.set("Male")

selcton1=StringVar()
selcton1.set( "Select" )
selcton2=StringVar()
selcton2.set( "Select" )

Button1=StringVar()

root.title("Registration From")

Label1=Label(root,text="Please enter details below",bg="orange",fg="white",font=("time new roman",20,"bold"))
Label1.pack(fill=X)

Label_name=Label(root,text="Name*",font=("time new roman",20,"bold"))
Label_name.place(x=150,y=100)
Entry_name=Entry(bd=2,relief="raised",textvariable=Name)
Entry_name.place(x=320,y=105,width=200,height=30)

Label_contact=Label(root,text="Contact*",font=("time new roman",20,"bold"))
Label_contact.place(x=150,y=150)
Entry_contact=Entry(bd=2,relief="raised",textvariable=contact)
Entry_contact.place(x=320,y=150,width=200,height=30)

Label_Email=Label(root,text="Email*",font=("time new roman",20,"bold"))
Label_Email.place(x=150,y=200)
Entry_Email=Entry(bd=2,relief="raised",textvariable=Email)
Entry_Email.place(x=320,y=200,width=200,height=30)

Label_Gender=Label(root,text="Gender*",font=("time new roman",20,"bold"))
Label_Gender.place(x=150,y=250)
Radio_Male=Radiobutton(root,text="Male",value="Male",font=("time new roman",15,"bold"),variable=Gen)
Radio_Male.place(x=300,y=250,width=100,height=30)
Radio_Female=Radiobutton(root,text="Female",value="Female",font=("time new roman",15,"bold"),variable=Gen)
Radio_Female.place(x=400,y=250,width=150,height=30)

Label_City=Label(root,text="City*",font=("time new roman",20,"bold"))
Label_City.place(x=150,y=300)
options1 = [
    "Select",
    "Surat",
    "Ahemdabad",
    "Vadodra",
    "Vapi",
    "Rajkot",
    "Bhavnagar",
    "Jamnagar"
]

City_Dropdown= OptionMenu( root,selcton1 , *options1)
City_Dropdown.place(x=320,y=300,width=230,height=35)


Label_State=Label(root,text="State*",font=("time new roman",20,"bold"))
Label_State.place(x=150,y=350)
options2 = [
    "Select",
    "Gujarat",
    "Maharast",
    "Pune",
    "Uttar pardesh",
    "Tamilnadu",
    "Karnatak",
    "Bihar"
]
State_Dropdown = OptionMenu( root ,selcton2, *options2)
State_Dropdown.place(x=320,y=350,width=230,height=35)

Ragister_Button=Button(text="Register",font=("time new roman",20),bg="orange",fg="black",bd=5,relief="raised",command=data)
Ragister_Button.place(x=300,y=450,width=180,height=50)





root.mainloop()