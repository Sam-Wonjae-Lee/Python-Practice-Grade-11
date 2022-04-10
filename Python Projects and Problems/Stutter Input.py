def stutter(word):
    word = list(word)
    return ("".join(word[0:2]) + "...") * 2 + " " + ("".join(word) + "?")


user_input = input("Enter a word: ")
print(stutter(user_input))