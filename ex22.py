#22.Write a python program to print odd numbers between 100 and 200 in reverse order?


#For Loop

n=200
for i in range(100,201):
    if i%2!=0:
        print(n,end=' ')
    n=n-1


#while loop

i=200
while i>=100:
    if i%2!=0:
        print(i,end=' ')
    i=i-1