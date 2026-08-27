'''
#22 Charlize Sky A. Dogillo
August 27, 2026
'''

#car game
class car:
    def __init__(self, brand, model, battery = 33):
        self.brand = brand
        self.model = model
        self.battery = battery
    def go(self, distance):
        self.battery = self.battery - distance / 25
        print("You travelled",distance,"km")
        print("Your",self.brand,self.model,"has",self.battery,"wH left")
    def charge(self, wH):
        self.battery += wH
        print("You charged your car")
        print("Your",self.brand,self.model,"has",self.battery,"wH left")

brand = input("What is the brand of your car?: ")
model = input("What is the model of your car?: ")
mycar = car("BYD","Seal 5")
while mycar.battery >0:
    action = input("What do you want to do? (go, charge): ")
    if action == "go":
        distance = int(input("How far?: "))
        mycar.go(distance)
    elif action == "charge":
        wH = int(input("How much to charge?: "))
        mycar.charge(wH)
    else:
        print("Invalid action")

print("Your car ran out of battery.")
print("")
print("")
print("______   _                     ")
print("|  ___| (_)                    ")
print("| |_     _   _ __              ")
print("|  _|   | | | '_ \             ")
print("| |     | | | | | |  _   _   _ ")
print("\_|     |_| |_| |_| (_) (_) (_)")
print("                               ")
print("                               ")
print("                                                         _________________________   ")
print("                    /\\      _____          _____       |   |     |     |    | |  \  ")
print("     ,-----,       /  \\____/__|__\_    ___/__|__\___   |___|_____|_____|____|_|___\ ")
print("  ,--'---:---`--, /  |  _     |     `| |      |      `| |                    | |    \ ")
print(" ==(o)-----(o)==J    `(o)-------(o)=   `(o)------(o)'   `--(o)(o)--------------(o)--' ") 
print("`````````````````````````````````````````````````````````````````````````````````````")

