# Create a rock paper scissors game in Python


# Player should be able to type r, p or s

# Game will print out the results and keep track of wins, losses and ties

# Type q to quit

# Circular heirarchy, both people need to pick at same time, can't see computer choice before you make your own choice


# To build this, we want a REPL - Read, Eval, Print, Loop - core computational idea shows up all over the place. We'lll build a few REPLs, rock paper scissors and adventure game over next couple days

# PYTHON interpreter is a repl - it reads command print("Hello World"), it evaluates it, sends it to print code, it prints out result and loops, starts back here and waits for next command which it can read, eval and print, loop


# Problem right now, clean up repition
# Plan, take evaluation step and generatlize it - define a function that evaluates player move and cpu_move and return results

import random


def eval_moves(player_move, cpu_move):
    winning_moves = {"r": "s", "s": "p", "p": "r"}
# Return -1 for loss, 0 for tie, 1 for win

    if(player_move == cpu_move):
        print("You tie!")
        return 0
    elif(winning_moves[player_move] == cpu_move):
        print("You win!!")
        return 1
    else:
        print("You came close.. try again!!")
        return -1


# 1. Build a REPL - wait fo ruser input, when user types r, p, or s it will eval and compare to computer choice which also picks r, p, or s. Print out results and loop/wait again for new command

choices = ["r", "p", "s"]
wins = 0
losses = 0
ties = 0

# LOOP - gives us an infinte loop which we will break out of at some point
while True:
    # READ
    # We need a prompt , takes our command and prints it out
    print(f"\nWins: {wins}, Losses: {losses}, Ties: {ties}")
    cmd = input("~~> ")
    # EVAL
    # Computer picks r/p/s
    cpu_move = random.choice(choices)
    print(f"CPU picks {cpu_move}")

    if cmd in choices:
        results = eval_moves(cmd, cpu_move)
        if results == 0:
            ties += 1
        elif results == 1:
            wins + -1
        elif results == -1:
            losses += 1
    elif cmd == "q":
        print("Goodbye!")
        break
    else:
        print("I did not understand that command. Please pick r, p, sp or q")

    # if cmd == "r":
    #     if cpu_move == "r":
    #         print("You tie")
    #         ties += 1
    #     elif cpu_move == "p":
    #         print("You lose...")
    #         losses += 1
    #     elif cpu_move == "s":
    #         print("You win!")
    #         wins += 1

    # elif cmd == "p":
    #     if cpu_move == "p":
    #         print("You tie")
    #         ties += 1
    #     elif cpu_move == "s":
    #         losses += 1
    #         print("You lose...")
    #     elif cpu_move == "r":
    #         print("You win!")
    #         wins += 1

    # elif cmd == "s":
    #     if cpu_move == "s":
    #         print("You tie")
    #         ties += 1
    #     elif cpu_move == "r":
    #         losses += 1
    #         print("You lose...")
    #     elif cpu_move == "p":
    #         print("You win!")
    #         wins += 1

    # elif cmd == "q":
    #     print("Goodbye!")
    #     break
    # else:
    #     print(" I did not understand that command. Please pick r, p, s, or q")

    # Compare player's command to cpu command
    # Update results based on win, loss, tie
    if cmd == "q":
        print("Goodbye")
        break  # breaks us out of infinite loop
    # PRINT results and score
    print(f"COMMAND IS {cmd}")
