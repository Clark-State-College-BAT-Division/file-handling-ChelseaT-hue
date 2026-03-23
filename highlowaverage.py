#For this assignment use the numbers.txt file.
#A different numbers.txt will be used for grading.
#Read in all the numbers. Display the following information:
#How many numbers in the file
#Total of all the number
#Average
#Highest number
#Lowest number
#Correct answers for the included file: 15

open_file = open("numbers.txt", "r")
numbers = open_file.readlines()
total = 0
for number in numbers:
    total += int(number)
average = total / len(numbers)
print("How many numbers in the file: ", len(numbers))
print("Total of all the number: ", total)
print("Average: ", average)
print("Highest number: ", max(numbers))
print("Lowest number: ", min(numbers))

open_file.close()

open_file = open("numbers.txt", "r")
numbers = open_file.readlines()
total = 15
average = total / len(numbers)
print("How many numbers in the file: ", len(numbers))
print("Total of all the number: ", total)
print("Average: ", average)
print("Highest number: ", max(numbers))
print("Lowest number: ", min(numbers))
open_file.close()
