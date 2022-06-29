# #python level up
import random
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

#########Week1###Day3##################

light = False
def light_switch():
    global light
    if light:
        print("Whoa! It's bright in here")
        light = False
    else:
        print("Who turned out the lights?")
        light = True
light_switch()
light_switch()
light_switch()
light_switch()

#This is the list
even_nums = [2,4,6,8,10]
even_nums.append(12)
even_nums.insert(0,0)
print(even_nums)

#This is a tuple. It cannot be changed via method...
# odd_nums = (1,3,5,7,9)
# odd_nums.append(11) #<----this would not work on the tuple
# print(odd_nums)

fav_songs = [
    "Placebo - Happy Birthday in the Sky",
    "Korn - ADIDAS",
    "Rammstein - Mein Herz Brennt"
]
print(fav_songs[1:3:1]) #[start:stop:step]
#print(fav_songs[::]) goes through all list
test = "maxam"
if test == test[::-1]:
    print(f"Yes! {test} is a palindrome")
else:
    print("It is not a palindrome")

num=random.randint(1,50)
while num%2==0:
    print("Even number!")
    num=random.randint(1,50)
#if the number is odd, the while loop will never ever run
print("An odd number!")
######################################################
while True:
    num=random.randint(1,50)
    print(num)
    if num%2==0:
        print("Even number!")
        continue
    else:
        print("An odd number!")
        break
#this while loop will always initialise. It mihght go straight to the else/break - but it will have started


