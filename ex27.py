#27.Write a python program to print a product of first 20 odd numbers?

#For Loop

product=1
for i in range(1,21):
    if i%2!=0:
        product=product*i
    print(product,end=' ')

#while loop

product=1
i=1
while i<=20:
    if i%2!=0:
        product=product*i
        print(product,end=' ')
    i=i+1

