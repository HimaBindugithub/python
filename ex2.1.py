#2.1.Write a python program to print 20 Natural Numbers except 4,7,9?

#For Loop

for i in range(1,21):
    if (i==4)or(i==7)or(i==9):
         continue
    print(i,end=' ')


#while loop
    
i=1
while i<=20:
    print(i,end=' ')
    i=i+1
    if (i==4)or(i==7)or(i==9):
        i=i+1 
   
    



