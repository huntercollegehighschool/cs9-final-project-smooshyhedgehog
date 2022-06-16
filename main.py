"""
Kate Mao and Morgan Yi:
NYC Animals: A Day in the Life
"""
#https://livebook.manning.com/book/get-programming/chapter-15/

#Write the main part of your program here. Use of the other pages is optional.

import time

def start():
  print("Hello!")
time.sleep(1)
print("Welcome to the day in the life of NYC Animals")
time.sleep(2)
print("Please pick an animal to live as! Are you a 'pigeon', 'rat', or a 'crusty white dog'.")
time.sleep(1)
animal = input("Enter your respective animal name: ")
 
if animal == "pigeon":
 import pigeon
 pigeon.pigeonstart()
elif animal == "rat":
  import rat
  rat.search()
elif animal == "crusty white dog":
  import millie
  millie.setup()
elif animal != "pigeon" or "rat" or "crusty white dog": 
 print("Not a known NYC animal! Please enter 'pigeon', 'rat', or 'crusty white dog'.")