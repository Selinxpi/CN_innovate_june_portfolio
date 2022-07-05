from character import Character

iron_man = Character("Tony Stark", "Iron Man")
iron_man.set_power("Powered Armor")

groot = Character("Groot", "Groot")
groot.set_power("Invulnerable to most Projectiles")

spider_man = Character("Peter Parker","Spiderman")
spider_man.set_power("Web-Slinging")



print(f"{iron_man.name} is {iron_man.super} and his power is {iron_man.power}")
print(f"{groot.name} actual name is {groot.super} and his power is {groot.power}")
print(f"{spider_man.name} is {spider_man.super} and his power is {spider_man.power}")


iron_man.get_power()
groot.get_power()
spider_man.get_power()
