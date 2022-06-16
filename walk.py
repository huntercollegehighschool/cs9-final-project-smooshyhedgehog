import time
time.sleep(1.5)
print("")
print("You are taking a walk")
time.sleep(1)
print("The weather is very nice!")
time.sleep(3)
print("CRONCH")
time.sleep(.5)
print("Your head whips around and you see a squirrel crunching on an acorn!")
acorn= input("Do you 'run' to catch the squirrel or 'resist' the temptation: ")
if acorn == "run":
  print("You dash over to the squirrel to try to catch it. You break away from your leash. You run and run and run until you can't see your owner anymore")
  time.sleep(1)
  print("Suddenly you cannot find the squirrel and you are now in a clearing amongst some trees.")
  time.sleep(2)
  print("SQUAWK")
  print("You have DIED! You have been eaten by a hawk. Start over on a New Life. ")
  import main
if acorn == "resist":
  print("You have chosen to resist the temptation of chasing the squirrel.")
  time.sleep(2)
  print("You have been a very good dog! You will live a long and healthy life filled with treats, cuddles, and squirrels!")
  time.sleep(1)
  print("Play again on a New Life!")
  import main

    