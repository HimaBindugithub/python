#50.Write a program to display alphabets as given below?
#Z Y X W V U T S R Q P O N M L K J I H G F E D C B A

#For loop

n=25
for i in range(26):
    print(chr(65+n),end=' ')
    n=n-1

#while loop

i=25
while i>=0:
    print(chr(65+i),end=' ')
    i=i-1