import time
timestamp=int(time.strftime('%H'))
print(timestamp)
if(timestamp<12):
    print("Goodmorning sir")
elif (timestamp>=12 and timestamp<=13):
    print("Good afternoon sir")
elif (timestamp>13 and timestamp<=19):
    print("Good evening sir")
else:
    print("Good night sir")
print("road")
''' i am adding here comments'''
print("rajkumar")