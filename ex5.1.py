#5.1 Write a python program to print Natural Numbers between 100 1nd 200 in Reverse order except 101,111,121,131,141,151?

#For Loop

# n=200
# for i in range(100,201):
#     if (i==101)or(i==111)or(i==121)or(i==131)or(i==141):
#         continue
#     print(n,end=' ')
#     n=n-1

#while loop

# i=200
# while i>=100:
#     if (i==101)or(i==111)or(i==121)or(i==131)or(i==141):
#         continue
#     print(i,end=' ')
#     i=i-1

#while loop
i=200
while i>=100:
    print(i,end=' ')
    i=i-1
    if (i==101)or(i==111)or(i==121)or(i==131)or(i==141):
        i=i-1 
   
#for loop

for i in range(200,100,-1): 
    if (i==101)or(i==111)or(i==121)or(i==131)or(i==141):
        continue
    print(i,end=' ')
