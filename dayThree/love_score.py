# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

# 100 days Solution
def count_letter(name1, name2):
    combined_name = name1 + name2
    names_lower = combined_name.lower()

    t = names_lower.count("t")
    r = names_lower.count("r")
    u = names_lower.count("u")
    e = names_lower.count("e")
    true = t + r + u + e

    l = names_lower.count("l")
    o = names_lower.count("o")
    v = names_lower.count("v")
    e = names_lower.count("e")
    love = l + o + v + e

    love_score = str(true) + str(love)

    return int(love_score)


# For loop (My version)
def count_letter_for(name1, name2):
    name1_lower = name1.lower()
    name2_lower = name2.lower()
    true = ["t", "r", "u", "e"]
    love = ["l", "o", "v", "e"]
    count_true = 0
    count_love = 0

    for letter in true:
        count_true += name1_lower.count(letter)
        count_true += name2_lower.count(letter)

    for letter in love:
        count_love += name1_lower.count(letter)
        count_love += name2_lower.count(letter)
    
    love_score = count_true * 10 + count_love
    
    return love_score

# Test for both function
love_score_for = count_letter_for(name1, name2)
love_score_sol = count_letter(name1, name2)

# Check score (Same solution for both)
def check_score(love_score):
    if love_score < 10 or love_score > 90:
        print(f"Your score is {love_score}, you go together like coke and mentos.")
    elif love_score >= 40 and love_score <= 50:
        print(f"Your score is {love_score}, you are alright together.")
    else:
        print(f"Your score is {love_score}.")

check_sol = check_score(love_score_sol)
check_for = check_score(love_score_for)

print(check_sol)
print(check_for)