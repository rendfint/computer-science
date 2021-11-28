#Write a program to read through the mbox-short.txt and figure out who has
#sent the greatest number of mail messages. The program looks for 'From '
#lines and takes the second word of those lines as the person who sent the
#mail. The program creates a Python dictionary that maps the sender's mail
#address to a count of the number of times they appear in the file. After the
#dictionary is produced, the program reads through the dictionary using a
#maximum loop to find the most prolific committer.

f_input = input("Enter full file name: ")
if len(f_input) < 1 : f_input = "mbox-short.txt"
file = open(f_input)

count = dict()

for line in file :
    if line.startswith("From:") : continue
    if line.startswith("From") :
        line_words = line.split()
        count[line_words[1]] = count.get(line_words[1], 0) + 1

biggest_sender = None
biggest_sended = None

for email, sended in count.items() :
    if biggest_sender is None and biggest_sended is None :
        biggest_sender = email
        biggest_sended = sended
    elif biggest_sended < sended :
        biggest_sender = email
        biggest_sended = sended

print(biggest_sender, biggest_sended)
