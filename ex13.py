#13.Write a python program to print sum of first 20 even numbers?

#For loop

sum=0
for i in range(1,21):
    if i%2==0:
        sum=sum+i
        print(sum,end=' ')


#while loop

sum=0
i=1
while i<=20:
    if i%2==0:
        sum=sum+i
        print(sum,end=' ')
    i=i+1