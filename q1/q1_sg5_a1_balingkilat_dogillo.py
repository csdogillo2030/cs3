'''
Charlize Sky A. Dogillo
August 27, 2026
'''

print("Welcome to SUPER AWESOME HERO RPG")
print("Featuring Arthur Morgurn from HR (we cannot use the trademark sorry)")
class Arthur:
    def __init__(self, brand, hp = 100):
        self.brand = brand
        self.hp = hp
    def take_damage(self, amount):
        self.hp = self.hp - amount
        print("Arthur took",amount,"damage!")
        print(self.brand,"has",self.hp,"HP left. Morgana has 100 HP left.")

arth = Arthur("Arthur")
amount = 10
arth.take_damage(amount)
