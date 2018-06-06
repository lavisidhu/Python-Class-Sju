word = input("Enter a word: ")
word_check = word.upper()
word_check = ''.join(letter for letter in word_check if letter.isalnum())
temp = word_check[::-1]
if(word_check==temp):
    print(word + " is a Palindrome.")
else:
    print(word + " is not Palindrome.")
