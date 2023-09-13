#44.Write a python program to print Even Numbers between num1 and num2 and its squares and cubes where num1>1 num2>2?


#For loop

num1=int(input("Enter first number:"))
num2=int(input("Enter second number:"))  

for i in range(num1,num2):
        if num1>1 or num2>2:
            if i%2==0:
                   print(i**1,i**2,i**3)
             
           

    
    

#while loop

num1=int(input("Enter first number:"))
num2=int(input("Enter second number:"))    
i=num1
while i<=num2:
        if num1>1 or num2>2:
                if i%2==0:
                        print(i**1,i**2,i**3)
                i=i+1
                
                
        
     