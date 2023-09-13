#6.Write a python program to print Natural Numbers between num1 and num2 where num1>num2>?

#For loop
num1=int(input("Enter first number:"))
num2=int(input("Enter second number:"))        
for i in range(num1,num2):
    if num1>1 or num2>2:
        print(i)


#while loop

num1=int(input("Enter first number:"))
num2=int(input("Enter second number:"))      
i=num1
while i<=num2:
    if num1>1 or num2>2:
        print(i)
        i=i+1