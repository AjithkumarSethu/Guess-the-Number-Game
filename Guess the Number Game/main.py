import random

num = random.randint(1,20)

guess = int(input("Can you guess the number I'm thinking? It's less than 20: "))

while guess != num:
    if guess > num:
        print("Your guess is higher")
    else:
        print("Your guess is lower")
    guess = int(input("Guess again "))

print("You Won!!!")

