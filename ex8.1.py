#8.1 Write a python program to print firdt 20 even numbers except 4,8,12?

#For loop


for i in range(1,21):
    if i%2==0:
        if (i==4)or(i==8)or(i==12):
            continue
        print(i,end=' ')

#while loop

# i=1
# while i<=20:
#     if i%2==0:
#         if (i==4)or(i==8)or(i==12):
#             continue
#     print(i,end=' ')
#     i=i+1

i=1
while i<=20:
    if i%2==0:
       print(i,end=' ')
    i=i+1
    if (i==4)or(i==8)or(i==12):
        i=i+1 
   