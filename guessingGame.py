import random

print("Number guessing game")
response = int(input("Enter your guess over here: "))
number = random.randint(1,9)

if(response == number):
        print("Wow you guessed it right")
        print(number)

if(response != number):
     if(response > number):
            print("Your guess was to high. Try again")
     else:
            print("Your guess was too low. Try again") 