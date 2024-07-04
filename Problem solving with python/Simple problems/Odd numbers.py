#Sum all the odd numbers from 0 to 100 and print it to the screen.

i=1
sum=0
while i<=100:
    if i%2 != 0:
        sum=sum+i
    i+=1
    
print(sum)