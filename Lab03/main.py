seconds = 10000
hours = int(seconds / 3600)
secondsLeft = seconds % 3600
minutes = int(secondsLeft / 60)
MoreSeconds = seconds % 60
Seconds = 1000123
miliseconds = Seconds % 1000




#prints numbers
print("Lab03, 100 Point Version")
print("Staring seconds: ", seconds)
print("Hours: ", hours)
print("Minutes: ", minutes)
print("Seconds: ", MoreSeconds)
print("Miliseconds: ", miliseconds)