################################################################################
# break_replace.py
# Author: Ming-Cee Yee
# Created: 2014-09-01
# Description: Replaces all line breaks with a whitespace.
# References:
# https://docs.python.org/3.3/contents.html
# http://stackoverflow.com/questions/275018/how-can-i-remove-chomp-a-newline-in-python
################################################################################

file_in = input("What file do you want to open? : ")

# opens `file_in`
f_in = open(file_in, 'r')
f_out = open("results.txt", 'w')

for line in f_in:
	print(line.strip(), end=" ", file=f_out)

f_in.close()
f_out.close()