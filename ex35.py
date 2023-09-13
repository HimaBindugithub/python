#35.Write a python program to print  first 20 Odd Numbers and its squares and cubes in reverse order?


#For loop

# n=20
# for i in range(1,21):
#     if i%2!=0:
#         print(n*1,n**2,n**3)
#     n=n-1
  
    

#while loop

i=20
while i>=1:
    if i%2!=0:
        print(i**1,i**2,i**3)
    i=i-1

    
#for loop

for i in range(20,0,-1):
    if i%2!=0:
        print(i*1,i**2,i**3)

