#18..Write a python program to print product of Even Numbers between num1 and num2 where num1>num2> in reverse order?


#For loop
num1=int(input("Enter first number:"))
num2=int(input("Enter second number:"))  
product=1
n=num2
for i in range(num1,num2):
    if i%2==0:
        if num1>1 or num2>2:
            product=product*i
            print(product,end=' ')
            n=n-1

    
    


#while loop

num1=int(input("Enter first number:"))
num2=int(input("Enter second number:"))    
n=num2
product=1
while i>=num1:
    if i%2==0:
        if num1>1 or num2>2:
            product=product*i
            print(product,end=' ')
    i=i-1
     