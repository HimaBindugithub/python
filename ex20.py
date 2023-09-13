#19.Write a python program to print  first 20 odd numbers in reverse order?

#For Loop
# n=20
# for i in range(1,21):
#     if i%2!=0:
#         print(n,end=' ')
#     n=n-1


#while loop

i=20
while i>=1:
    if i%2!=0:
        print(i,end=' ') 
    i=i-1      

#for loop

for i in range(20,0,-1):
    if i%2!=0:
        print(i,end=' ')

