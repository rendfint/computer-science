#Open the file romeo.txt and read it line by line. For each line, split the
#line into a list of words using the split() method. The program should build
#a list of words. For each word on each line check to see if the word is
#already in the list and if not append it to the list. When the program
#completes, sort and print the resulting words in alphabetical order.
#You can download the sample data at http://www.py4e.com/code3/romeo.txt

f_input = input("Enter full filename: ")
try :
    file = open(f_input)
except :
    print("Can't open the file", f_input, "\nMake sure the filename and extension are correct")
    quit()

words = list()

for line in file :
    line_words = line.split()
    for word in line_words :
        if word in words : continue
        else : words.append(word)

words.sort()
print(words)
