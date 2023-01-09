print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇
first_route = input("Where do you like to go first, left or right? \n")
first_route_lower = first_route.lower()
if first_route == "left":
  print("Wow you just avoided the trap!")
  second_route = input("How do you like to move on to this next route? Do you like to swim or wait? \n")
  second_route_lower = second_route.lower()
  if second_route_lower == "wait":
    print("Three doors has just appear! Good choice!")
    third_route = input("Now, what color of door do you like to choose? Red? Blue? or Yellow? \n")
    third_route_lower = third_route.lower()
    if third_route_lower == "yellow":
      print("Congratulations! You've got the treasure!")
    elif third_route_lower == "red":
      print("Sorry you've gone in to the jungle and got eaten by a huge dinosaur.")
      print("Game over")
    elif third_route_lower == "blue":
      print("Oh man! you almost got it! Now you have to stay on this dungeon for the rest of your life!")
      print("Game over")
  else:
    print("Sorry. You just got eaten by sharks")
    print("Game over")
else:
  print("You fall into a huge hole!")
  print("Game over")
