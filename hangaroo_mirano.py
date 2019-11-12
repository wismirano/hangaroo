import random
import sys


wordList = [
"numpy", "python", "anaconda", "spyder"
           ]

guess_word = []
secretWord = random.choice(wordList)
length_word = len(secretWord)
alphabet = "abcdefghijklmnopqrstuvwxyz"
letter_storage = []



def beginning():
    print("Hey there! Welcome to Hangaroo!\n")

    while True:
        name = input("Please enter your name!\n").strip()

        if name == '':
            print("Oops! You'll need a name to proceed!")
        else:
            break

beginning()



def newFunc():
    print("What a pleasant name!\n")

    while True:
        gameChoice = input("Ready to play?\n").upper()

        if gameChoice == "YES" or gameChoice == "Y":
            break
        elif gameChoice == "NO" or gameChoice == "N":
            sys.exit("Oh well, that's a shame! Come play next time!")
        else:
            print("Please only answer with a yes or a no!")
            continue

newFunc()



def change():

    for character in secretWord:
        guess_word.append("-")

    print("Let's begin! The word you'll need to guess has", length_word, "characters.")
    print("Clue: They're key words to some of our topics in ECE2112!")
    print("Please note that you can enter only 1 letter from a-z!\n\n")

    print(guess_word)



def guessing():
    guess_taken = 1

    while guess_taken < 10:


        guess = input("Pick a letter:\n").lower()

        if not guess in alphabet:
            print("Enter a letter from a-z only!")
        elif guess in letter_storage:
            print("You've already entered that letter!")
        else: 

            letter_storage.append(guess)
            if guess in secretWord:
                print("You've guessed correctly!")
                for x in range(0, length_word):
                    if secretWord[x] == guess:
                        guess_word[x] = guess
                        print(guess_word)

                if not '-' in guess_word:
                    print("You won! Congratulations!")
                    break
            else:
                print("The letter is not in the word. Try again!")
                guess_taken += 1
                if guess_taken == 10:
                    print(" Sorry, but you lost! The secret word was",         secretWord)


change()
guessing()

print("Game over! Thanks for playing!")