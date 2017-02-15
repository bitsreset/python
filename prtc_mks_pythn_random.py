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
