import random

name = input("What is your name? ")
print("Hello, " + name + " Welcome to HangMan Game ")

words = ['computer', 'science', 'engineering', 'programming', 'coding', 'python', 'logic', 'hangman', 'deterministic']
word = random.choice(words)

print("Guess the word ")
guesses = ' '
total_guesses = 8
while total_guesses > 0:
    failed = 0
    for char in word:
        if char in guesses:
            print(char, end=" ")
        else:
            print("_", end=" ")
            failed += 1
    if failed == 0:
        print("\n You won!")
        break

    guess = input("\n Guess a word: ")
    guesses += guess
    if guess not in word:
        total_guesses -= 1
        print("Wrong")
        print("You have", + total_guesses, 'more guesses')
        if total_guesses == 0:
            print("You lose")
            print("The word is ", word)
