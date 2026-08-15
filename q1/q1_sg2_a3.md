#22 Charlize Sky A. Dogillo

9 - Balingkilat

August 15, 2026


```hi ignore me pls
import time

time.sleep(0.5)

print("Hello!")

zodiac= ["(Rat (鼠 / Shǔ)", "Ox (牛 / Niú)", "Tiger (虎 / Hǔ)", "Rabbit (兔 / Tù)", "Dragon (龙 / Lóng)", "Snake (蛇 / Shé)", "Horse (马 / Mǎ)", "Goat (羊 / Yáng)", "Monkey (猴 / Hóu)", "Rooster (鸡 / Jī)", "Dog (狗 / Gǒu)", "Pig (猪 / Zhū)"]

year= int(input("Enter your birth year: "))

if year<= 1899:
    
    time.sleep(0.5)
    
    print("Invalid Year, it should not be earlier than 1900.")

else:
    
    x= (year - 2020) % 12
    
    time.sleep(0.5)
    
    print("Your Chinese Zodiac sign is: ", zodiac[x])
    
time.sleep(1)

print("Goodbye!")

time.sleep(2)
```
![Output](q1/images/q1_sg2_a3.png)

[Python](q1/q1_sg2_a3.py)
