from manger import *
def customer_reole():  # function defination
    while True : #user while loop
        print(store)
        user_choice=input("select Your Fruit : ")
        print("Your Fruit selected Apple.")
        if user_choice in store.keys():  #user_choice in store.keys for if statment
            F_qty=int(input("Enter Fruit Quntity : "))
            store[user_choice]["quantity"]-=F_qty  #- to user fruit Qty
            print("Avelable Fruits : ",store[user_choice])
        else:
            print("Fruit not exiesting your stock")
        yn=input("Press Y for yes and N for no : ")
        if yn == 'y':
            continue
        elif yn == 'n':
            break
                     
