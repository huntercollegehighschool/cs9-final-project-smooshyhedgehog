#Use of this page is optional. If you use code here, make sure either import page2 or from page2 import * appear on your main.py page.
import time

time.sleep(1)

print("World Loading...")
time.sleep(1)
print("NYC Buffering...")
time.sleep(1)

print ("You have chosen to be a NYC rat.")

time.sleep(2)

def search():
  print("In an effort to look for food, you think of two possible locations you would find some! ")
  time.sleep(1)
  search = input("Enter T to search in trash can, or S to search in the sewer: ")
  if search == "T":
    print("You successfully find some old cheese and a rotten tomato piece! Today is like your lucky day!")
    food()
  elif search == "S":
    print("Gross! You fell into a pile of disgusting, dirty water filled with lots of pollution. You quickly retreat back and look in the trash can, and find old cheese and a rotten tomato piece.")
    food()

time.sleep(2)

def food():
  print("Both of these foods look... not so appetizing but sufficient enough to help you cure your hunger.")
  time.sleep(1)
  food = input("Enter C to eat the cheese, or T to eat the tomato: ")
  if food == "C":
    print("You consume the cheese with a bit of hesitance. Expectedly, it tastes a bit sour. After that large meal, you go to exercise outside! You run around and sneak into Hunter.")
    hunter()
  elif food == "T":
    print("You lick the tomato, but it tastes so bad! You decide that the cheese would be much more delicious, but think of all the other optionns you could have. In hopes of finding leftover lunches and snacks of students, you find yourself in the hunter building")
    hunter()

time.sleep(2)

def hunter():
  print("Yay! You're in a building where you can pick up the food dropped by those clumsy 7th graders. You're in the corner of a classroom, next to a hole in the wall. You notice a delicious POTATO CHIP sitting by a student's foot.")
  time.sleep(1)
  hunter = input("Do you 1: run and try to get the food, or 2: hide in the hole to wait for another opportunity? Enter 1 to run, or 2 to hide in the wall: ")
  if hunter == "1":
    print("You get to the chip, but turns out it was a trick! It's glued to the floor, so while trying to pick it up, a student puts a box over you. The extermination team comes, and you are exterminated from the building. you go live a sad, sad life. You're so exhausted from trying to get the chip.")
    death()
  elif hunter == "2":
    print("You retreat back into the hole, but the sneaky teacher catches you! they block the hole off, and you're trapped. The extermination team comes and you are forced out of the building. Your life is in shambles.")
    death()

time.sleep(2)

def death():
  print("After a long day, you go to rest in the middle of the street...")
  time.sleep(4)
  print("Uh oh...")
  time.sleep(3)
  print("*POW*")
  time.sleep(2)
  print("You have died due to an angry NYC driver. Goodbye.")
  time.sleep(3)
  ending()

def ending ():
  again = input("Do you want to play again as a new character? Enter A: ")
  if again == "A":
    import main
    main.start()
  elif again != "A":
    print("Done.")