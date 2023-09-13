#4.1.Write a python program to print Natural Numbers between 100 and 200 except 100,120,130,140,150,160,170?

#For loop

for i in range(100,201):
    if (i==100)or(i==120)or(i==130)or(i==140)or(i==150)or(i==160)or(i==170):
        continue
    print(i,end=' ')


#while loop

# i=100
# while i<=200:
#     if (i==100)or(i==120)or(i==130)or(i==140)or(i==150)or(i==160)or(i==170):
#          continue
#     print(i,end=' ')
#     i=i+1
    

i=100
while i<=200:
    print(i,end=' ')
    i=i+1
    if (i==101)or(i==120)or(i==130)or(i==140)or(i==150)or(i==160)or(i==170):
        i=i+1 
   
    