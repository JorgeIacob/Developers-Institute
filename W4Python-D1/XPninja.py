#1

# 3 <= 3 < 9
#true
# 3 == 3 == 3
#true
# bool(0)
#false
# bool(5 == "5")
#false
# bool(4 == 4) == bool("4" == "4")
# true
# bool(bool(None))
#false
# x = (1 == True)

x = (1 == True)
y = (1 == False)
a = True + 4
b = False + 10

print("x is", x)
print("y is", y)
print("a:", a)
print("b:", b)

# x is True
# y is False
# a: 5
# b: 10

#2
a = 60
b = 50
if a > b:
    print("hello world")

#3


x = int(input("Give me a month of the year and I will say you which season is "))
if 2 < x < 6:
    print("It's spring")
elif 5 < x < 9:
    print("It's summer")
elif 8 < x < 12:
    print("It's autumn")
elif x == 12 or x < 3:
    print("It's winter")

