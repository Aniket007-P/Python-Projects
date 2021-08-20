#library that we use to choose random
#word from list of words
import random

#here the game will ask name of Player.
name= input("Enter Your name: ")
print("Good Luck! ", name)

words = ['rainbow', 'computer', 'science', 'programming',
         'python', 'mathematics', 'player', 'condition',
         'reverse', 'water', 'board', 'geeks']

#this function will choose a random word
#from the list of words
word = random.choice(words)

print("Guess the character: ")
guesses=''

#any number turns can be used here
#turns user got
turns = 12

while turns > 0:
    #counts the number of times a user fails
    failed = 0

    #taking one charcter input
    # of a word at a time
    for char in word:
        #comparing that character
        # with the character in guess
        if char in guesses:
            print(char)
        else:
            print("_")
            #for every failure 1 will
            # be incremented in failed
            failed+=1

    if failed == 0:
        #user will win the game if failed ==0
        # and the output will be printed
        print("You Win")
        print("The word is: ", word)
        break
    #if user has guessed wrong then
    # it will ask again to enter a input
    guess = input("Guess a character:")

    #every input character will
    # be stored n guesses everytime
    guesses += guess

    if guess not in word:
        turns-=1
        #if character is not in
        #word then it will pring Wrong
        print("wrong")

        #will print remaining number of turns
        print("You have ",+turns ,"guesses left")

    #if player's all guesses becomes wrong and
    # turns = 0 then the player will loose the game
    if turns ==0:
        print("You LOSE!")

