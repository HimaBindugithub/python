#48.Write a program that asks the user for a positive integer value.
#The program should calculate the sum of all integers from 1 up to the number entered except 4,6,9,11,13.
#For example,if the user enters 20,the loop will find the sum of 1,2,3,4,..20?

#For loop

sum=0
num=int(input("Enter positive number:"))
for num in range(1,21):
    if (num==4)or(num==6)or(num==11)or(num==13):
        continue
    sum=sum+num
    print(sum,end=' ')


#while loop

# sum=0
# i=1
# while i<=20:
#     if (i==4)or(i==6)or(i==11)or(i==13):
#         continue
#     sum=sum+i
#     print(sum,end=' ')
#     i=i+1
    
    

       