# #0
#
# basket = ["Banana", "Apples", "Oranges", "Blueberries"]
#
# basket.remove("Banana")
# basket.remove("Blueberries")
# basket.append("Kiwi")
# basket.insert(0,"Apples")
# basket.count("Apples")
# basket.clear()
# print(basket)
#
# #1
#
# my_fav_numbers = {12, 4, 8, 7, 11}
# my_fav_numbers.add(3)
# my_fav_numbers.add(9)
# friend_fav_numbers = {5, 6, 2, 1}
# our_fav_numbers = my_fav_numbers.union(friend_fav_numbers)
# print(our_fav_numbers)
#
# #2
#
# my_fav_numbers = (12, 4, 8, 7, 11)
# conv = list (my_fav_numbers)
# conv.append(3)
# conv.append(9)
# my_fav_numbers = tuple(conv)
# friend_fav_numbers = (5, 6, 2, 1)
# our_fav_numbers = my_fav_numbers + friend_fav_numbers
# print(our_fav_numbers)

# 3

# for i in range(5,100,5): # using range function to generate numbers and dividing each number by 10 to get float number
#     print(i/10)
#
# #4
#
# quit = False
# i = 1
# toppings = []
# while i < 6:
#     topping = input("Choose a topping for your pizza. You can add until 5: ")
#     if topping == "quit":
#         print("Your order is in progress")
#         break
#     else:
#         toppings.append(topping)
#         print("Your pizza contains :" )
#         print(toppings)
#     i +=1

# 5

#
# age = int(input("What's your age? "))
# for i in range (3,12):
#     if age <= 3:
#         print("Your entry is free")
#         break
#     elif 3 < age <= 12:
#         print("Your ticket costs $12")
#         break
#     elif age >12:
#         print("Your ticket costs $15")
#         break

# 6: four ways to make this exercise, for grasp the methods
#

# lista = ["Chen", "Nir", "Oz", "Gil"]
# for i in range (len(lista)):  #using range function
#     print(lista[-i-1])
#
# lista = ["Chen", "Nir", "Oz", "Gil"]
# for i in lista[::-1]:   #using list negative access
#     print(i)


# lista = ["Chen", "Nir", "Oz", "Gil"]
# while lista:                            #using while and pop method
#     print(lista.pop(-1))        # flow -1 stops in 0. if the way is positive from 0, it's out of range

# lista = ["Chen", "Nir", "Oz", "Gil"]
# length = len(list)
# i = 0
# # Iterating using while loop
# while i < length:
#     print(list[-i-1])
#     i += 1

# 7

# for i in range (3,12):
#     if age <= 3:
#         print("It's free for the kid")
#         break
#     elif 3 < age <= 12:
#         print("Costs $12")
#         break
#     elif age >12:
#         print("Costs $15")
#         break

# 8

# nums = [2, 3, 6, 7, 8]
# for i in nums:
#     if i %2 == 0:
#         print(i)
#         i = + 1

# 9

# kidsNum: int = 5
# kidsNumReq: int = 0
# kidsList: list = []
#
# while kidsNum:  #while loop that runs within 5 iterations
#     kidsNumReq = kidsNumReq + 1   #requests runs ahead until 5
#     kidsNum = kidsNum - 1  #the numbers of kids decreasing to 0, when no need more than 5
#     name = str(input("What's your name? "))
#     age = int(input("And your age? "))
#     if age < 16:
#         print("Sorry," + name + " this movie is restricted above 16")
#     elif age > 21:
#         print("Sorry," + name + " this movie is restricted above 16 under 21")
#     else:
#         print("Hello," + name + " you can enter the movie")
#         kidsList.append({'name': name, 'age': age})  #adds inputs to a list
#
# print('\nPurchase Summary of entered group\n')
# print('Number of requests to entry:' + kidsNumReq.__str__() + '\n')   # __str__ permits concatenation
# print('Number of purchased tickets:' + len(kidsList).__str__() + '\n')
# print('List of entered users:' + kidsList.__str__() + '\n')

#10 This time you have a list of users, and you want to remove every user that is below 16 years old.
#Write a program that ask every user their age, and if they are less than 16 years old, remove them from the list.
#At the end, print the final list.


kidsNum: int = 5
kidsNumReq: int = 0
kidsList: list = []

while kidsNum:  #while loop that runs within 5 iterations
    kidsNumReq = kidsNumReq + 1   #requests runs ahead until 5
    kidsNum = kidsNum - 1  #the numbers of kids decreasing to 0, when no need more than 5
    name = str(input("What's your name? "))
    age = int(input("And your age? "))
    if age < 16:
        print("Sorry," + name + " this movie is restricted above 16")
    else:
        print("Hello," + name + " you can enter the movie")
        kidsList.append({'name': name, 'age': age})  #removes inputs to a list

print('\nPurchase Summary of entered group\n')
print('Number of requests to entry:' + kidsNumReq.__str__() + '\n')   # __str__ permits concatenation
print('Number of purchased tickets:' + len(kidsList).__str__() + '\n')
print('List of entered users:' + kidsList.__str__() + '\n')