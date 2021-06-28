# 1-You are given a string and you have to swap cases i.e. to convert uppercase to
# lowercase and vice-versa

def swapcase(str1):
   new_string = ""   
   for character in str1:
       if character.isupper():
           new_string += character.lower()
       else:
           new_string += character.upper()           
   return new_string
string=input("Enter The String:")
print(swapcase(string))