#36.Write a python program to print Natural Numbers between 40 and 80 and its squares and cubes in reverse order?


#For loop

n=80
for i in range(40,81):
    print(n**1,n**2,n**3)
    n=n-1


#while loop    

i=80
while i>=40:
    print(i**1,i**2,i**3)
    i=i-1

