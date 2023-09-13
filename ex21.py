#21.Write a python program to print odd numbers between 100 and 200?

#For Loop

for i in range(100,201):
    if i%2!=0:
        print(i,end=' ')


#while loop

i=100
while i<=200:
    if i%2!=0:
        print(i,end=' ')
    i=i+1