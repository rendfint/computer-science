#In this assignment you will read through and parse a file with text and
#numbers. You will extract all the numbers in the file and compute the sum of
#the numbers.

import re

name = input("Enter file name: ")
if len(name) < 1 : name = "regex_sum_42.txt"

try :
    handle = open(name)
except :
    print("Can't open file", name)
    print("Make sure to enter a valid file name")
    quit()

sum = 0

for line in handle :
    if not re.search('([0-9]+)', line) : continue
    numbers = re.findall('([0-9]+)', line)
    for number in numbers :
        number = int(number)
        sum = sum + number

print(sum)
