
                # Working of ATM Machine

a=10000
d=0
def enter_card():
    print("Name: Mr.John")
    print("Cash available in your account: Rs-",a)

def deposit():
    global d
    d=int(input("Enter Deposit Amount:Rs- "))
    
    print("Cash available in your account: Rs-",a+d)
def withdraw():
    w=int(input("Enter Withdraw Amount:Rs- "))
    x=(a+d)-w
    print("Now cash available: Rs-",x)
    if x<5000:
        print("Low balance")
def exit():
    print("Thank You")      

enter_card()
deposit()
withdraw() 
exit()



