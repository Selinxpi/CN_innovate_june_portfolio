####DICTIONARY####

my_cat = {
    "name":"Zosim",
    "colour":"Grey",
    "mood":"Playful"
}
my_cat["mood"] = "hungry" #update

print(f'My cat {my_cat["name"]} is very {my_cat["mood"]} today')
print(my_cat.keys()) 
x = my_cat.keys()
my_cat["age"] = 2
print(x) #dict_keys(['name', 'colour', 'mood', 'age'])

print(my_cat.values()) #dict_values(['Zosim', 'Grey', 'hungry'])
print(my_cat.items()) #dict_items([('name', 'Zosim'), ('colour', 'Grey'), ('mood', 'hungry')])

print(my_cat.get("mood"))
print(my_cat.get("legs","This key doesn't exist"))

print(my_cat.keys()) #dict_keys(['name', 'colour', 'mood', 'age'])
print(list(my_cat.keys())) #['name', 'colour', 'mood', 'age']

for i in my_cat.keys():
    print(i)

my_cat.update({"legs":"4"}) #to update 
my_cat.update({"name":"Zosja"}) #to replace
print(my_cat)

my_cat.pop("mood") #delete
print(my_cat)

my_list = ["yes","no","no","yes","yes","yes","yes","yes","no"]
y = my_list.count("yes")
my_list.append("yes")
print(y)
