import random
from collections import Counter

someWords = '''apple banana mango strawberry 
orange grape pineapple apricot lemon coconut watermelon
cherry papaya berry peach lychee muskmelon'''

someWords = someWords.split(' ')

#randomly choose a word from our someWords LIST
word = random.choice(someWords)

if __name__ == "__main__":
    print("Guess the word1 HINT:The word is a name of a Fruit.")

    for i in word:
        #for printing empty spaces of the word
        print('_', end= '')


    playing = True
    #list for storing the letters guessed by the player
    letterGuessed = ''
    chance = len(word)+2
    flag = 0
    correct= 0
    try:
        while (chance != 0) and flag == 0: #flag is updated when the word is correctly guessed
            print()
            chance -= 1

            try:
                guess = str(input("Enter a  letter to guess: "))
            except:
                print("Enter only a Letter!")
                continue

            #validation for the guess
            if not guess.isalpha():
                print("Enter only  LETTER.")
                continue
            elif len(guess)> 1:
                print("Enter only a single LETTER.")
                continue
            elif guess in letterGuessed:
                print("You have already guessed this LETTER.")
                continue

            #if letter is guessed correctly
            if guess in word:
                k = word.count(guess)#k stores the number of times the letter occurs in word
                for _ in range(k):
                    letterGuessed += guess #the letter added as many times it occurs in the word

            #print the word
            for char in word:
                if char in letterGuessed and(Counter(letterGuessed) != Counter(word)):
                    print(char, end=' ')
                    correct += 1
                #if user has guessed all the letters
                elif (Counter(letterGuessed) == Counter(word)):#once the correct word is guessed the game
                                                               # will end, even if th echances remain
                    print("the Word is:", word)
                    flag = 1
                    print("Congratulations You Won!")
                    break #break out of for loop
                    break

                else:
                    print("_",end=' ')

        #if user uses all chances
        if chance <=0 and (Counter(letterGuessed) != Counter(word)):
            print("Sorry You LOST!!")
            print("the word was: {}", format(word))
            print("Please Try Again...")

    except KeyboardInterrupt:
        print("Bye! Try again..")
        exit()













