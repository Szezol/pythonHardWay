__author__ = 'Zoltan'

from sys import argv

script, filename = argv,input('what is filename?')

txt = open(filename)

print ("Here's your file %r:" % filename)
print (txt.read())

print ("Type the filename again:")
file_again = input("> ")

txt_again = open(file_again)

print (txt_again.read())
