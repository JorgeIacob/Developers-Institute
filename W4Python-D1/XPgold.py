#3

print("Hello world\n" * 4, "I love Python\n" * 4)

#This is the result, i don't understand why the first line of "I love Python" appears with extra space
# Hello world
# Hello world
# Hello world
# Hello world
#  I love Python
# I love Python
# I love Python
# I love Python

#4

print ("If you give X, I will return X+XX+XXX+XXXX")
X= input("Give your X: ")
X = int(X)
Y =  X+(X*10)+(X*100)+(X*1000)
print (Y)

