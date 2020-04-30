import random
import re
from functools import reduce

#
# 1

#
# rand = [random.randint(10, 20) for x in range(10, 20)]
# print(rand)
#

# my_list1 = [i for i in range(3, 30) if i % 3 == 0]
# print(my_list1)
#

# def check (num):
#     return (len(nums)% num==0)
#
# nums = [1,2,3,4,5,6,7,8,9,10]  #length 10, with this the numbers are divisible by
# my_list = list(filter(check, nums))
# print(my_list)
#
#
# def check_bigger(item):
#     return item > 12
#
# numbers = [13,14,3,6]  #return numbers bigger tan 12
# my_list2 = list(filter(check_bigger, numbers))
# print(my_list2)
#

# my_list4 = [x**2 for x in range(0,6)] # square
# print(my_list4)

# a = [1, 2, 3, 3, 3, 4, 5, 5]
# dup = []
# for each in a:
#   if each not in dup: #automatically adds different numbers because they only "are not" in the new list
#     dup.append(each)
# print(dup)

# 2

# users = ["Mickey", "Minnie", "Donald", "Ariel", "Pluto"]
# french_words = ["Bonjour", "Au revoir", "Bienvenue", "A bientôt"]
#
# len_users = dict(zip(users, range(len(users))))  # convert list to dictionary
# print(len_users)
#
# len_users_invert = {v: k for k, v in len_users.items()}  # value to key inversion
# print(len_users_invert)
#
# alphabetical = sorted(users)
# alphabetical = dict(zip(alphabetical, range(len(alphabetical))))  # Alphabetical order
# print(alphabetical)
#
# trans = ["Hello", "Goodbye", "Welcome", "See you soon"]
# result = dict(zip(french_words, trans))  # concatenates for effect "translated"
# print(result)
#
# for letter in len_users:
#     if re.search('i', letter):  # obtains words with 'i'
#         print(letter)
#
# for letter in len_users:
#     if re.match('M|P', letter):  # obtains words with M and P
#         print(letter)
#
#
# def find_and_unite(words: list):
#     list_words_res: list = []
#     for word in words:
#         list_words_res.append(''.join(sorted(set(word), key=word.index))) #removes duplicate letters
#
#     return list_words_res
#
#
# # users = ["Mickey", "Minnie", "Donald", "Ariel", "Pluto"]
# print(find_and_unite(users))
#
# original_dict= len_users
# new_dict={}
# for k,v in original_dict.items():
#     dict_element={k:v}
#     dict_element.update(new_dict) #reverses order
#     new_dict=dict_element
#
# print(new_dict)

#3



#1 Capitalize all of the pet names and print the list
my_pets = ['sisi', 'bibi', 'titi', 'carla']
my_pets = [name.capitalize() for name in my_pets] #['Sisi', 'Bibi', 'Titi', 'Carla']
print(my_pets)

#2 Zip the 2 lists into a list of tuples, but sort the numbers from lowest to highest.
my_strings = ['a', 'b', 'c', 'd', 'e']
my_numbers = [5, 4, 3, 2, 1]
data1 = list(zip(my_numbers,my_strings))
data1.sort()
data2 = list(zip(my_numbers, my_strings)) #[(1, 'e'), (2, 'd'), (3, 'c'), (4, 'b'), (5, 'a')]
data2.sort()
print(data2)

#3 Filter the scores that pass over 50%
scores = [73, 20, 65, 19, 76, 100, 88]
print([i for i in scores if i < 50]) # [20, 19]

#4 Bonus : Combine all of the numbers that are in a list on this file using reduce (my_numbers and scores). What is the total?
product = reduce((lambda x, y: x + y), my_numbers+scores)
print(product) #456