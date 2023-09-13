#3.Write a python program to print first 20 Natural Numbers in reverse order except 3,6,8,9?

#For loop

# n=20
# for i in range(1,21):
#     if (i==3)or(i==6)or(i==8)or(i==9):
#         continue
#     print(n,end=' ')
#     n=n-1

#while loop  

i=20
while i>=1:
    print(i,end=' ')
    i=i-1
    if (i==3)or(i==6)or(i==8)or(i==9):
        i=i-1 
   
#for loop
    
for i in range(20,0,-1):
    if (i==3)or(i==6)or(i==8)or(i==9):
        continue
    print(i,end=' ')

      