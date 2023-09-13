#28.Write a python program to print a product of odd numbers between 10 and 20?


#For Loop

product=1
for i in range(10,21):
    if i%2!=0:
        product=product*i
    print(product,end=' ')

#while loop

product=1
i=10
while i<=20:
    if i%2!=0:
        product=product*i
        print(product,end=' ')
    i=i+1

