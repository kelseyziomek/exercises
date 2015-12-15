#importing arguments
from sys import argv

#assigning arguments
script, filename = argv

#assigning contents of file to variable
txt = open(filename)

#interacting with user
print "here's your file %r:" % filename

#printing the contents of the file
print txt.read()

#asking the user for the file name
print "Type the file name again:"

#assinging user input (file name) to second variable
file_again = raw_input("> ")

#opening the file (second variable)
txt_again = open(file_again)

#printing the contents of the file
print txt_again.read()

txt.close()
txt_again.close()