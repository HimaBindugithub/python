#26..Write a python program to print sum of Odd Numbers between num1 and num2 where num1>1 num2>2 in reverse order?


#For loop
num1=int(input("Enter first number:"))
num2=int(input("Enter second number:"))  
sum=0  
n=num2
for i in range(num1,num2):
    if i%2!=0:
        if num1>1 or num2>2:
            sum=sum+i
            print(sum,end=' ')
            n=n-1

    
    


#while loop

num1=int(input("Enter first number:"))
num2=int(input("Enter second number:"))    
n=num2
sum=0
while i>=num1:
    if i%2!=0:
        if num1>1 or num2>2:
            sum=sum+i
            print(sum,end=' ')
    i=i-1
     