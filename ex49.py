#49.Write a program to display alphabets as given below?
#A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
#For loop

for i in range(26):
    print(chr(65+i),end=' ')

#while loop

i=0
while i<26:
    print(chr(65+i),end=' ')
    i=i+1