class Hero:
    def __init__(self, inputName, inputHealth, inputPower):
        self.name = inputName
        self.health = inputHealth
        self.power = inputPower

hero1 = Hero ("radvik", 100, 100)
hero2 = Hero ("komar", 100, 10)
hero3 = Hero ("otong", 50, 10)

print (hero1.__dict__)
print (hero2.__dict__)
print (hero3.__dict__)
