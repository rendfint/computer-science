#Write a program that prompts for a file name, then opens that file and reads
#through the file, looking for lines of the form: X-DSPAM-Confidence: 0.8475
#Count these lines and extract the floating point values from each of the lines
#and compute the average of those values and produce an output as shown below.
#Do not use the sum() function or a variable named sum in your solution. You
#can download the sample data at http://www.py4e.com/code3/mbox-short.txt when
#you are testing below enter mbox-short.txt as the file name.

file_input = input("Enter full filename: ")
try :
    file_open = open(file_input)
except :
    print("Can't open file ", file_input + "\nMake sure to input a valid filename.")
    quit()

count = 0
confidence_spam = 0.0

for line in file_open :
    line = line.rstrip()
    if line.startswith("X-DSPAM-Confidence:") :
        pos = line.find(":")
        number = line[pos + 1:]
        number = number.lstrip()
        number = float(number)

        confidence_spam = confidence_spam + number
        count = count + 1

    else :
        continue

average_confidence_spam = confidence_spam / count

print("Average spam confidence:", average_confidence_spam)
