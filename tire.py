import math
done = 'no'
while done.lower() != 'yes':
    r = 0
    w = int(input("What is width of the tire in mm? "))
    a = int(input("What is the aspect ratio of the tire? "))
    rord = input("Do you have the tire's radius or diameter? (r/d)")
    if rord == "r":
        rad = int(input("What is the radius of the wheel? "))
        d = rad * 2
    else:
        d = int(input("What is the diameter of the wheel in inches? "))

    pi = math.pi 

    v = float((pi * (w**2) * a) * (w * a + (2540*d)) / 10000000)

    print(f"The volume of the tire is {v}")
    done = input('Are you done? (yes/no)')

car = input('What is the make of this vehicle? ')
from datetime import datetime

today = datetime.now()

with open("volumes.txt", "at") as vol_file:
    print(f"Date:{today} | Vehicle:{car}, Width:{w}, Aspect Ratio:{a}, Volume:{v}", file=vol_file)
    volumes = file=vol_file

print(volumes)
print('Goodbye')