

base = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','y','z']
count = len(base)

dic = {}

for i in range (0,count):
    keyVal1 = base[i]
    keyVal2 = base[count-1-i]

    dic[keyVal1] = keyVal2


print(dic)


