def func55(state1, state2):
    if state1 == state2:
        return 1, 1
    elif state1 == "rock" and state2 == "scissors":
        return 1, 0
    elif state1 == "rock" and state2 == "paper":
        return 0, 1
    elif state1 == "scissors" and state2 == "rock":
        return 0, 1
    elif state1 == "scissors" and state2 == "paper":
        return 1, 0
    elif state1 == "paper" and state2 == "rock":
        return 1, 0
    elif state1 == "paper" and state2 == "scissors":
        return 0, 1
    else:
        return 0, 0

import random
def func5():
    compChoice = random.choice(["rock", "scissors", "paper"])
    you = input('Your turn, choice("rock", "scissors", "paper"): ')

    y, c = func55(you, compChoice)

    if y and c:
        print("nobody`s")
    elif not(y or c):
        print("something goes wrong")
    elif y:
        print("You won. You have chosen %s and comp have chosen %s" % (you, compChoice))
    else:
        print("You lost. You have chosen %s and comp have chosen %s" % (you, compChoice))


func5()