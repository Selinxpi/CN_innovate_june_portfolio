# #1
# cn = "Welcome to Code Nation"
# cn_len = len(cn)
# def check_lengh():
#     if cn_len % 2==0:
#         print("Length of the {} is {} and it is even.".format(cn,cn_len))
#     else:
#         print("Lengh of the {} is {} and it is odd.".format(cn,cn_len))

# cn2 = "Welcome to Code Nation"
# length2 = len(cn2)
# if (length2 % 2) == 0:
#     print("EVEN")
# else:
#     print("ODD.")

# #2
# albet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u", "v", "w","x","y","z"]
# for i in albet:
#     print(i)
# num = int(input("Enter a number from 1 - 26 to see the corresponding letter: \n"))
# num -= 1
# print(albet[num])


# ###########DAY3####Activity 1#####34
# def yourinput():
#     num = input("Please input a number. \n")
#     try:
#         print(int(num))
#         print(type(int(num)))
#     except:
#         print("Try again.")
#         yourinput()
# yourinput()

# ##My activity###
# def add_up():
#     num1 = input("What is the first number you'd like to add up? \n")
#     num2 = input("What is the second number you'd like to add up? \n")
    
#     try:
#         print(f"{num1} + {num2} is {(int(num1) + int(num2))}!")
#     except:
#         print("\n ERROR: please input only numerical values. \n")
#         print("**************************** \n")
#         add_up()
# add_up()

####Activity2####

# countries = {
#     "United Kingdom":"London",
#     "France":"Paris",
#     "Germany":"Berlin",
#     "Spain":"Madrid",
#     "Italy":"Rome"
# }
###1-method
# print(countries)
# countries["Latvia"]="Riga"
# countries["Netherlands"]="Amsterdam"

###2-method
# countries.update({"Latvia":"Riga"})
# countries.update({"Netherlands":"Amsterdam"})
# for k, v in countries.items():
#     print(k + ":" + v)
# countries.update({"United Kingdom":"English","France":"French","Germany":"German","Spain":"Spanish","Italy":"Italian","Latvia":"Latvian","Netherlands":"Dutch"})
# for k, v in countries.items(): # I prefer .items method more because it looks more organized
#     print(k + ":" + v)


# ####Activity2####

fav_songs=[{
    "Artist":"Placebo",
    "song_name":"Happy Birthday in the Sky",
    "genre":"Alternative Rock(Glam Rock)",
    "release_year":"2022"
},
{
    "Artist":"Korn",
    "song_name":"ADIDAS",
    "genre":"Alternative Metal(nu metal)",
    "release_year":"1996"
},
{
    "Artist":"Rammstein",
    "song_name":"Mein Herz Brennt",
    "genre":"industrial metal",
    "release_year":"2011"
}]
for i in fav_songs:
    print(i)
    print("\n")

fav_songs.append(
    {"Artist":"Static-X",
    "song_name":"So",
    "genre":" Industrial metal",
    "release_year":"2003"})
for i in fav_songs:
    print(i)
    print("\n")

fav_songs.pop(1) #delete

for i in fav_songs:
    print(i)
    print("\n")




