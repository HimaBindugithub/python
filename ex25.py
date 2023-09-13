#25.Write a python program to print sum of odd numbers between 100 and 200?

#For loop

sum=0
for i in range(100,201):
    if i%2!=0:
        sum=sum+i
        print(sum,end=' ')
    


#while loop

sum=0
i=1
while i<=20:
    if i%2!=0:
        sum=sum+i
        print(sum,end=' ')
    i=i+1
    
