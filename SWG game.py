

import random


def game(comp, you):
    if comp == you:
        return None
    elif comp == 's':
        if you =='w':
            return False
        elif you == 'g':
            return True
    elif comp == 'w':
        if you == 'g':
            return False
        elif you == 's':
            return True
    elif comp == 'g':
        if you == 'w':
            return True
        elif you == 's':
            return False
        

print("computer turn: water(w), snake(s), gun(g)")
raNo = random.randint(1,3)
if raNo == 1:
    comp = 's'
elif raNo == 2:
    comp = 'w'
elif raNo == 3:
    comp = 'g'

you = input("your turn: water(w), snake(s), gun(g)?\n")
print(f"computer choose {comp} ")
print(f"you choose {you} ")

a = game(comp, you)
if a == None:
    print("The game is Tie!!!")
elif a:
    print("you win !!!")
else:
    print("You lose!!!")

