import time

time.sleep(1)

print("World Loading...")
time.sleep(1)
print("NYC Buffering...")
time.sleep(1)

print ("You have chosen to be a NYC pigeon.")

time.sleep(2)

def pigeonstart():
  print("It's wayyy too hot outside!")
  time.sleep(2)
  print("You want to drink water to cool off. You spot a fountain being used by a teenager, and a dirty puddle on the ground.")
  time.sleep(2)
  pigeonstart = input("Enter F to drink from the fountain, or P to drink from the puddle: ")
  if pigeonstart == "F":
    print("You fly over to the fountain, and the teenager graciously holds the water for you. Hooray!! You were able to cool off effectively.")
    bread()
  elif pigeonstart == "P":
    print("You fly into the puddle...")
    time.sleep(3)
    print("SPLASH")
    time.sleep(2)
    print("EEEK! The puddle was refreshing, but a toddler jumped into the puddle and made you all wet!")
    bread()

time.sleep(3)

def bread():
  print("After that ordeal, you're very hungry. You spot some bread on the floor next to a lovely family.")
  bread = input("To eat the bread, enter B. To wait on the side and scavenge for other food, enter W: ")
  if bread == "B":
    print("You try to be sneaky and get the bread.")
    time.sleep(1)
    print("*SCREAAAAAM*")
    time.sleep(1)
    print("The angry child has scared you away! You leave with no bread, left hungry.")
    human()
  elif bread == "W":
    print("You wait on the side, and the child spots you. He walks up towards you and drops many breadcrumbs for you to eat. Yay! The waiting tactic was effective. You happily eat your lovely meal.")
    human()

time.sleep(3)

def human():
  print("Perhaps today would be a good day to meet some humans... Oh! You see a kind-looking elder, and a Hunter freshman named Morgan Yi!")
  time.sleep(2)
  human = input("Enter E to fly over to the elder, and M to fly over to Morgan: ")
  if human == "E":
    print("You fly over, and turns out this elder really loves pigeons! She allows you to perch on her arm, and feeds you some seeds on a stick. You live a happy life, and she adopts you to bring you home.")
    ending()
  elif human == "M":
    print("You try and greet Morgan... but she SHRIEKS IN FEAR!!!!")
    time.sleep(2)
    print("You get so startled by the high-pitched scream that you immediately fly away, NEVER to meet a human ever, ever again. You go fly onto your home at the top of a skyscraper, and live there happily ever after.")
    ending()

time.sleep(4)

def ending ():
  again = input("Do you want to play again as a new character? Enter A: ")
  if again == "A":
    import main
    main.start()
  elif again != "A":
    print("Done.")