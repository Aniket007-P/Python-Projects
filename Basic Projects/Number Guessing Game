import random
import math

#taking inputs from Player
lower = int(input("Enter Lower Bound: "))
upper = int(input("Enter Upper Bound: "))

#random Number chooosen by Machine
x= random.randint(lower, upper)

#How Much guess Can a player do?
print("\n\tYou Have only",round (math.log(upper - lower +1, 2)), "chance to Guess.")
count = 0

while count<math.log(upper - lower +1, 2):
    count+=1

    guess = int(input("Enter your guessed Number:"))

    if x == guess:
        print("Congratulations you have guessed thr number in", count, "try")
        break
    elif x > guess:
        print("You guessed too small!")
    elif x < guess:
        print("You Guessed too big!")

#If player get out of Guesses.
#then this will print.
if count>=math.log(upper - lower +1, 2):
    print("You Lost!")
    print("The number is:", x)
    print("Better luck Next time!")









