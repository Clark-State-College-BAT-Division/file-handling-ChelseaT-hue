#For this assignment use the words.txt file.
#Read in all the words. Count how many are palindromes, or words that are spelled the same forwads and backwards.
#For example, wow is a paldindrome.
#A different file wile be used for grading.
#Correct answer for this file: 

open_file = open("words.txt", "r")
words = open_file.readlines()
palindrome_count = 0
for word in words:
    word = word.strip()
    if word == word[::-1]:
        palindrome_count += 1
print("Number of palindromes: ", palindrome_count)
open_file.close()

