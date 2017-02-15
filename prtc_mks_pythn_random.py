#Write a program that chooses a random integer between 0 and 100 (inclusive).
#Then ask the user to guess what number has been chosen. Each time the user enters a guess, 
#the program indicates whether the user guessed correctly (and exits), or if the guess was too high or too low

import random
answer = random.randint(0,100)
guess = int(input("Guess a no. [0,100]"))

while True:
    if guess == answer :
        print("Right! ur guess is {0}".format(guess))
        break
    elif guess < answer:
        print("Your guess is {0} LOW! ".format(guess))
    elif guess > answer:
        print("Your guess is {0} HIGH!".format(guess)) 
