#Tead in the echo.txt file and display it in the terminal using print()
#This is a guided practice. Either follow the video or your instructor in class.

open_file = open("echo.txt", "r")
echo = open_file.read()
print(echo)
open_file.close()

open_file = open('echo.txt', 'r')
echo = open_file.read()
print(firstLine)
open_file.close()