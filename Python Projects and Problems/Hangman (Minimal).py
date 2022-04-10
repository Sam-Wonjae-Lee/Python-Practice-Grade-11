import random

print(
    "\nWelcome to Hangman! This is a game where you try to guess a three letter word. You have six chances to get the answer. If you lose, it's game over.")

words = ["cat", "dog", "sky", "mat", "jug"]
random_num = random.randint(1, len(words))
game_word = words[random_num - 1]
game_word = list(game_word)
user_words = []
num_of_fails = 0

print(game_word)

for i in range(len(game_word)):
    user_words.append("_")
# add "_" three times

while num_of_fails < 6:
    print()
    print(user_words)
    user_input = input("\nEnter a letter: ")

    if user_input in game_word:
        print("\nYou guessed a letter. ")
        index_letter = game_word.index(user_input)
        user_words[index_letter] = game_word[index_letter]

    else:
        print("You did not guess the letter. ")
        num_of_fails += 1
    if game_word == user_words:
        print("You guessed the word!")
        break

    if num_of_fails == 1:
        print('''  +---+
  |   |
  O   |
      |
      |
      |
=========''')

    elif num_of_fails == 2:
        print('''  +---+
  |   |
  O   |
  |   |
      |
      |
=========''')

    elif num_of_fails == 3:
        print('''  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''')

    elif num_of_fails == 4:
        print('''  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''')

    elif num_of_fails == 5:
        print('''  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''')

    elif num_of_fails == 6:
        print('''  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''')
        print("Game Over. Try Again.")







