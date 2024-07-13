# Write a function to make an hour-to-minute converter.
hour,min = input("Enter Hour and minute values: ").split() 
if hour <=12:
    total_min = hour*60+min
    print(total_min)
else:
    total_min= (hour-12)*60+min
    print(total_min)
