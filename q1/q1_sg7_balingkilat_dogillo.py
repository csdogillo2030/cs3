'''
Charlize Sky A. Dogillo
September 17, 2026
'''

class Glassware:
    def __init__(self, material="Glass"):
        self.material = material
    def display_info(self):
        print(f"Material: {self.material}")


class Beaker(Glassware):
    def __init__(self, capacity):
        super().__init__()
        self.capacity = capacity
    def display_info(self):
        print(f"Beaker - Capacity: {self.capacity} mL, Material: {self.material}")


class Tray:
    def __init__(self):
      #NOTE TO SKY FROM SKY: yo uh where did you get the beaker amounts..
        self.beakers = [
            Beaker(100),
            Beaker(150),
            Beaker(200),
            Beaker(250),
            Beaker(300)
        ]
    def display_beakers(self):
        print("Tray contains 5 Beakers:")
        for beaker in self.beakers:
            beaker.display_info()


tray = Tray()
tray.display_beakers()
del tray

