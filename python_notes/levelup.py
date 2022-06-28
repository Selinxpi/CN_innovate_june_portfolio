#python level up

print(int(5.6))
print(type(int("54")))

#my cashmachine
pin_number = 31014
accnum = 9999

accnum=int(input("Enter Accnum: \n"))
pin_number=int(input("Enter pin: \n"))
amount=int(input("Enter amount: \n"))

balance= 4000
def cash_machine():
    global pin_number
    global balance
    global accnum

new_balance=balance-amount

if pin_number==31014 and accnum==9999 and amount<=balance:
    print("Your balance was {} ".format(balance))
    print("Amount you want to withdrawl: {}".format(amount))
    print("You balance NOW: {} ".format(new_balance))
elif amount>=balance:
    print("Chech the balance please!")
else:
    print("Wrong pin or accnum ,try 1 more time: ")

#####
print("What is my name?")
name = input()
if name:
    print(f"Welcome {name} to Innovate!")
else:
    print("You did not submit a name!")

##Entry list
allowed=["Gaz","Timur","Anastasija","Sam","Elina"]
name1=input("What is your name?\n")
while name1 not in allowed:
    print("Your name isn't on the list")
    print("Try again")
    name1=input("What is your name?")
print("Please come in!")