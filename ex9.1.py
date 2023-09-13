#9.1 Write a python program to print first 20 even numbers in reverse order except 18, 14,4?

#For loop

# n=20
# for i in range(1,21):
#     if i%2==0:
#         if (i==18)or(i==14)or(i==12):     
#              continue
#         print(n,end=' ')
#         n=n-1

#while loop

# i=20
# while i>=1:
#     if i%2==0:
#         if (i==18)or(i==14)or(i==12):     
#              continue
#     print(i,end=' ')
#     i=i-1       

#while loop
         
i=20
while i>=1:
    if i%2==0:
       print(i,end=' ')
    i=i-1
    if (i==18)or(i==14)or(i==12):
        i=i-1        
   


#for loop

for i in range(20,1,-2):
    if (i==18)or(i==14)or(i==12):     
             continue
    print(i,end=' ')
