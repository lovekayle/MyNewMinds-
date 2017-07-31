#This is a program to write, capitalize and read the text we write 
import os
file_object = open('aaa.txt', 'w')
file_object.write(("This is a file for us to see if the text can be proformed on the screen.").upper())
file_object.close()
all_the_text = open("aaa.txt").read()
print all_the_text

file_object.write(raw_input("please write something: ").upper())
file_object.close()
all_the_text = open("aaa.txt").read()
print all_the_text
