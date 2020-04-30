

now = 2020
age = input("What is your birthday? put in this format DD/MM/YYYY: ")
year = age.split("/")[-1]
age = now - int(year)
cipher = int(str(age)[-1])

cake = f""""


       ___{"i"*cipher}__
      |:H:a:p:p:y:|
    __|___________|__
   |^^^^^^^^^^^^^^^^^|
   |:B:i:r:t:h:d:a:y:|
   |                 |
   ~~~~~~~~~~~~~~~~~~~
"""
print(cake)