#52.Write a program to display alphabets as given below?
#a b c d e f g h i j k l m n o p q r s t u v w x y z

#For loop

for i in range(26):
    print(chr(97+i),end=' ')


#while loop

i=0
while i<26:
    print(chr(97+i),end=' ')
    i=i+1