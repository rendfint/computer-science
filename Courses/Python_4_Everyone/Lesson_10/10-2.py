#Write a program to read through the mbox-short.txt and figure out the
#distribution by hour of the day for each of the messages. You can pull the
#hour out from the 'From ' line by finding the time and then splitting the
#string a second time using a colon.
#From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008
#Once you have accumulated the counts for each hour, print out the counts,
#sorted by hour as shown below.

name = input("Enter file name: ")
if len(name) < 1 : name = "mbox-short.txt"
try :
    text = open(name)
except :
    print("Can't open file", name)

hours = dict()

for line in text :
    if line.startswith("From:") : continue
    if line.startswith("From") :
        words = line.split()
        hour = words[5].split(":")[0]
        hours[hour] = hours.get(hour, 0) + 1

lst = list()

for k, v in hours.items() :
    lst.append( (k,v) )

lst.sort()

for k, v in lst :
    print(k, v)
