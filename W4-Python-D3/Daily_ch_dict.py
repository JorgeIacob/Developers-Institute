

key = input("Input the text you want to encrypt ")
def caesar(text):
  textocif = ""
  for ch in text:
    if ch.isalpha():  #isalpha() method returns True if all the characters are alphabet letters (a-z)
      alphabet = ord(ch) + 3  #the ord() function returns the number representing the unicode code of a specified character
      if alphabet > ord('z'):  #and "3" asigns three steps ahead from a letter
        alphabet -= 26
      finalletter = chr(alphabet) # The chr() method returns a string representing a character whose Unicode code point is an integer.
      textocif += finalletter
  print ("The ciphered text is: ", textocif)
  return textocif
caesar(key)

key2 =input("¿What text you want to decrypt? ")
def caesar2(text):
  textocif = ""
  for ch in text:
    if ch.isalpha():
      alphabet = ord(ch) - 3  #here the same process but inverse
      if alphabet < ord('a'):
        alphabet += 26
      finalletter = chr(alphabet)
      textocif += finalletter
  print ("The ciphered text is: ", textocif)
  return textocif
caesar2(key2)
