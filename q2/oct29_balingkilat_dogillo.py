class Warrior:
    def special_move(self):
        print(f"Warrior swings a mighty sword!")

class Mage:
    def special_move(self):
        print(f"Mage casts a powerful spell!")
        
class Archer:
    def special_move(self):
        print(f"Archer shoots a precise arrow!")
        
def perform_move(character):
    character.special_move()
        
Haymitch = Warrior()
Lucy Gray = Mage()
Katniss = Archer()

heroes = [Haymitch, Lucy Gray, Katniss]
for c in heroes:
    perform_move(c)
