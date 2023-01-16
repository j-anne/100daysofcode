#Write your code below this line 👇
def prime_checker(number):
    message = "It's a prime number."
    count = 2
    while count < number:
        if number % count == 0:
            message = "It's not a prime number."
        count += 1
    print(message)

#Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)