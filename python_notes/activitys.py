#1
cn = "Welcome to Code Nation"
cn_len = len(cn)
def check_lengh():
    if cn_len % 2==0:
        print("Length of the {} is {} and it is even.".format(cn,cn_len))
    else:
        print("Lengh of the {} is {} and it is odd.".format(cn,cn_len))

cn2 = "Welcome to Code Nation"
length2 = len(cn2)
if (length2 % 2) == 0:
    print("EVEN")
else:
    print("ODD.")

#2
albet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u", "v", "w","x","y","z"]
for i in albet:
    print(i)
num = int(input("Enter a number from 1 - 26 to see the corresponding letter: \n"))
num -= 1
print(albet[num])