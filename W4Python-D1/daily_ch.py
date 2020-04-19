string = input("Give me a string with 10 characters: ")
while len(string) != 10:
    string = input("You have not gave 10 characters. Try again: ")
if len(string) == 10:
    print("The first character of your string is " + string[0], "and the last is " + string[9])

for i in string:
    print (i)


def swap_string(str):
    if len(str) <= 1:
        return str

    mid = str[1:len(str) - 1]
    return str[len(str) - 1] + mid + str[0]
print (swap_string(string))