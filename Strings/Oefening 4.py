word = input("Enter a word: ")
palindrome = ''

for i in word:
    palindrome = i + palindrome
if word.lower() == palindrome.lower():
    print(word, "is a palindrome")
else:
    print(word, "is not a palindrome")
