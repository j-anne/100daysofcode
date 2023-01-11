#Remember to use the random module
#Hint: Remember to import the random module here at the top of the file. 🎲
import random
#Write the rest of your code below this line 👇
rand_num = random.randint(1,10)
if rand_num % 2 == 0:
    print("Heads")
else:
    print("Tails")