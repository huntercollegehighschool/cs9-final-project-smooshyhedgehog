import time

from datetime import date 
today = date.today()

time.sleep(2)

def setup():
  print("World Loading...")
  time.sleep(1)
  print("NYC Buffering...")
  time.sleep(1)

print("Hello. You have chosen to be a crusty white dog")
milliename = input("Enter your name: ")

time.sleep(1)

print("Too bad",milliename,".")

time.sleep(1)
print("You were born on:",today,"and adopted by a Korean-American family living in suburban Queens. You have been named Millie.")

time.sleep(1.5)
print("Your owner has been very menacing and wants you to wear an outfit.")
print("")
time.sleep(2)
print("Pick your outfit options! Would you like to wear Christmas attire or a pink hoodie.")

outfit = input("Enter 'C' for Christmas attire, or 'P' for pink hoodie: ")

if outfit == "C":
  print("You have successfully chosen Christmas Outfit.")
  time.sleep(2)
  print("As it is Christmas you are expected to attend you're owner's Christmas party with their relatives.")
  time.sleep(1)
  print("Your owner's little cousins are very loud and annoying all day.")
  time.sleep(1)
  print("Whilst they are eating dinner the younger cousin dangles food to you.")
  time.sleep(1)
  foodchoose=input("Do you 'take the food' or do you 'sniff but don't eat' the food: ")
  if foodchoose== "take the food":
      time.sleep(1.5)
      print("You have chosen to eat the food from the loud cousin")
      time.sleep(1)
      print("The food was very delicious however now you are very stuffed. Your owner takes you out on a walk.")
      walk = input("Type 'leash' to go on the walk: ")
      while walk != "leash":
        print("Not an option. Millie needs exercise!")
        walk = input("Type 'leash' to go on the walk: ")
      if walk == "leash":
        import walk
  if foodchoose == "sniff but don't eat":
    print("You have chosen to sniff but don't eat the food")
    time.sleep(1)
    print("You have become very hungry and see some brown stuff on the floor!")
    time.sleep(1)
    brownstuff = input("Do you 'eat' the brown stuff or 'walk away': ")
    if brownstuff == "eat":
        print("You have eaten the brown substance!")
        time.sleep(0.5)
        print("It tastes kinda weird.")
        time.sleep(3)
        print("Your stomach begins feeling kinda weird.")
        time.sleep(3)
        print("You have died via rat poisoning. Start over on a New Life.")
        import main
    if brownstuff == "walk away":
      print("You have chosen to walk away!")
      time.sleep(1)
      print("Your owner gives you food and you eat it. It is extra delicious. Your owner wants to take you for a walk.")
      walk = input("Type 'leash' to go on the walk: ")
      while walk != "leash":
        print("Not an option. Millie needs exercise!")
        walk = input("Type 'leash' to go on the walk: ")
      if walk == "leash":
        import walk
  elif foodchoose != "take the food" or foodchoose != "sniff but don't eat":
    print ("Not an option!")
    foodchoose=input("Do you 'take the food' or do you 'sniff but don't eat' the food: ")
f
if outfit =="P":
  print("You have chosen to wear the pink hoodie!")
  time.sleep(2)
  print("The pink hoodie is very uncomfortable to put on.")
  bite=input("Do you 'bite' your owner or do you 'tough it out': ")
  if bite == "bite":
    print("OWWWWWWW")
    print("Your owner has been hurt by your bite.")
    time.sleep(1)
    print("You have been tossed outside.")
    time.sleep(5)
    print("Two days has passed. You do not notice a large dark figure flying overhead. Start over on a New Life.")
    time.sleep(1)
    print("You have DIED! You have been eaten by a hawk. Start over on a New Life. ")
    import main
  if bite == "tough it out":
    time.sleep(1.5)
    print("You have chosen to tough it out!")
    time.sleep(1)
    print("You have been given a treat by your owner and posted onto their doggy Instagram!")
    time.sleep(1)
    print("You have been rewarded with a walk!")
elif outfit != "C" and outfit != "P":
  print("Not an outfit option")
  outfit = input("Enter 'C' for Christmas attire, or 'P' for pink hoodie: ")
  walk = input("Type 'leash' to go on the walk: ")
  while walk != "leash":
    print("Not an option. Millie needs exercise!")
    walk = input("Type 'leash' to go on the walk: ")
  if walk == "leash":
    import walk