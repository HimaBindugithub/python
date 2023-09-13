#19.Write a python program to print  first 20 odd numbers?

# For Loop

for i in range(1,21):
    if i%2!=0:
        print(i,end=' ')


#while loop

i=1
while i<=20:
    if i%2!=0:
        print(i,end=' ') 
    i=i+1       