from person import Person

anastasija = Person ("Anastasija")
print(anastasija)

anastasija = Person ("Anastasija", 30, "168cm")

timur = Person ("Timur", 7, "133cm")

irina = Person ("Irina", 49, "164cm")

irina.set_hair("Black,short")
print(irina.hair)