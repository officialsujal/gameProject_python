'''
By running this game it creates new file "highScore.txt" in your directory.
---------------Enjoy the game-------------------------
'''

import random
randNumber = random.randint(1,100)
userGuess = None
guesses = 0
while(userGuess != randNumber):
    userGuess = int(input("Enter your guess: "))
    guesses += 1
    if(userGuess== randNumber):
        print("You guess it right!!!")
    else:
        if(userGuess>randNumber):
            print("your guessed number is wrong!!! think somthing smaller")
        else:
            print("your guessed number is wrong!!! think somthing large")

        
print(f"you guessed the number in {guesses} guesses.")
with open("highScore.txt", "w") as f:
    pass
with open("highScore.txt", "r") as f:
    highScore = f.read()
if highScore=="":
    highScore = 100

if (guesses<int(highScore)):
    print("you just have broken the high score!!!!!")
    with open("highScore.txt", "w" ) as f:
        f.write(str(guesses))
