# this is comment
# and comments 
# can be 
# big

import random

print("This is Anastasija file")

hello= "Good Afternoon"
print(hello)

print("This is a string for displaying characters")
print("1234") #string
print(1234+1)  #int -whole numb.
print(12.34) #float
print(True) #boolean        
print(False) #boolean
print(None)   #none-blank/null data

#Week1 DAY 2
#methods
print(len(hello))
print(hello[1])
print(hello[-1])
print(hello.upper())

print("HELLO".lower())
print("hello EVERYONE. THIS is INNOVATE. :)".capitalize())
print("This quick brown fox fox fox fox fox".count("fox"))
print("This quick brown fox".find("T"))
print("The quick brown fox".replace("fox","frog"))
print("The quick brown fox".strip("The quick"))

#Liberaries (import random on the top)
print(random.random())  
print(random.uniform(1, 10)) #float
print(random.randint(1, 10)) #int


#Variables
my_name = "Anastasija"
my_age = 30
student = True
print(my_name ,my_age ,student)
print("Hello my name is", my_name)
print("I am", my_age)

print("Hello my name is {} and I am {} years old".format(my_name,my_age))
print(f"Hello my name is {my_name} and I am {my_age} years old") #<---best practise

fav_drink="coffee"
print(fav_drink)
print("my favorite drink is", fav_drink)
print("{}'s favorite drink is {}".format(my_name,fav_drink))

son_name="Timur"
son_age="6"
fav_colour="blue"
print("my son name is {}, he is {}, his favorite colour is {}".format(son_name, son_age, fav_colour))


#Arithmetic Operators for calculation "+","-","*","**","/","%"
print(8 + 2)
print(10 -2)
print(5 * 3)
print(5 ** 2)
print(12 / 3)
print(15 % 3)
print(16 % 3)

i=10
print(i)
m=i+2
print(m)
x=100
print(x)
g=x+20
print(g)
z=m+g
print(z)

#Assignment Operator "="
balance = 100
print(balance)
amount = 20
balance = amount+balance
print(balance)
#or
balance += amount
print(balance)

#input
input_name = input("Enter your name please: \n")
print(input_name)

# If else with input
music=input("What music is plaing now? \n")
if music == "classical":
    print("NO,NO,NO! Please NO!!!")
    print("Turn it off")
elif music == "no music":
    print("hmmmm....Turn it on please")
else:
    print("Good I like it")

#If else without input
music = "classical"
if music == "classical":
    print("NO,NO,NO! Please NO!!!")
    print("Turn it off")
elif music == "no music":
    print("hmmmm....Turn it on please")
else:
    print("Good I like it")

#comparison operators "== Equal" "!= Not Equal"
num = 30
num2 = 60
if num > num2:
    print(f"{num} is bigger")
elif num2 > num:
    print(f"{num2} is bigger")
else:
    print("EQUALS")

age = 16
country = "UK"
if age >= 18 and country == "UK":
    print("Yes I can serve you!")
elif age >=18 and country !="UK":
    print("Where are you from?")
else:
    print("You aren't old enough. Sorry.")

#Functions
def light_switch():
    print("Switching the lights")
light_switch()
light_switch()
light_switch()

#my cashmachine
pin_number= 31014
accnum=9999

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

fav_songs = [
    "Placebo - Happy Birthday in the Sky",
    "Korn - ADIDAS",
    "Rammstein - Mein Herz Brennt"
]
print(fav_songs)
print(fav_songs[1])
print(len(fav_songs))

fav_songs.append("Static-X - So") #+
print(fav_songs)

fav_songs.pop() #remove last 
print(fav_songs)

fav_songs.pop(0) #remove one you want to remove
print(fav_songs)
