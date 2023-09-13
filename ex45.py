#45.Write a python program to print Even Numbers between num1 and num2 and its squares and cubes where num1>1 num2>2 in reverse order?



#For loop

num1=int(input("Enter first number:"))
num2=int(input("Enter second number:"))  
n=num2
for i in range(num1,num2):
        if num1>1 or num2>2:
            if i%2==0:
                   print(n**1,n**2,n**3)
            n=n-1
             
           

    
    

#while loop

num1=int(input("Enter first number:"))
num2=int(input("Enter second number:"))    
i=num2
while i>=num1:
        if num1>1 or num2>2:
                if i%2==0:
                        print(i**1,i**2,i**3)
                i=i-1
                
                
        
     