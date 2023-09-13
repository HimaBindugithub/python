#9.Write a python program to print first 20 even numbers in reverse order?

#For loop
n=20
for i in range(1,21):
    if n%2==0: 
       print(n,end=' ')  
    n=n-1     

#while loop

i=20
while i>=1:
    if i%2==0:
        print(i,end=' ')
    i=i-1