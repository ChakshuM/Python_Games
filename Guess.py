import random
import time

chances = 5
random_number = random.randrange(0,100)
print("Guess the number in 5 trials and win a star!!")

while(chances >= 0):


    def temp(guess):
        if guess == random_number:
            print(" * ")
            print("Congratulations, You won. This window will exit in 5 seconds")
            time.sleep(5)
            exit()
        elif guess > random_number:
            if chances-1 == 0:
                pass
            else:
                print("You are left with "+str(chances-1)+" and number you guessed is too high, try again..")
        elif guess< random_number:
            if chances-1 == 0:
                pass
            else:
                print("You are left with "+str(chances-1)+" and number you guessed is too low, try again..")


    if chances >= 1:
        guess = int(input("Try your luck, guess a number between 0 to 100: "))
        temp(guess)
    else:
        print("You Lost. Bye.")
        print("Correct answer was " + str(random_number))
        time.sleep(5)

    chances = chances - 1





