#40..Write a python program to print odd numbers between 40 and 80 and its squares and cubes?

#For loop

for i in range(40,81):
    if i%2!=0:
        print(i**1,i**2,i**3)

#while loop

i=40
while i<=80:
    if i%2!=0:
         print(i**1,i**2,i**3)
    i=i+1
