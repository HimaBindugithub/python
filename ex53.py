#53.Write a program to display alphabets as given below?
#z y x w v u t s r q p o n m l k j i h g f e d c b  a

#For loop

n=25
for i in range(26):
    print(chr(97+n),end=' ')
    n=n-1

#while loop

i=25
while i>=0:
    print(chr(97+i),end=' ')
    i=i-1