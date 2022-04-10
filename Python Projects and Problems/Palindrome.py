def palindrome(num):
    if str(num) == str(num)[::-1]:
        print("It is a palindrome.")
    else:
        print("It is not a palindrome")

palindrome_input = input("Enter an Input: ")

palindrome(palindrome_input)