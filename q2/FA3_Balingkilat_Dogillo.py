from abc import ABC, abstractmethod

class Sensor(ABC):
    @abstractmethod
    def get_reading(self):
        pass
    
class TempSensor(Sensor):
    def get_reading(self):
        return "24.5°C"

class PHSensor(Sensor):
    def get_reading(self):
        return "7.2 pH (Neutral)"


sensor1 = TempSensor()
sensor2 = PHSensor()

print("--- Lab Inventory System ---")
print(f'[pH Sensor] Reading: {sensor2.get_reading()}')
print(f'[Temperature Sensor] Reading: {sensor1.get_reading()}')
print("")
print("----------------------------")
