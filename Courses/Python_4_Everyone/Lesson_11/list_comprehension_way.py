import re
name = input("Enter file name: ")
print( sum( [ int(x) for x in re.findall('[0-9]+',open(name).read()) ] ) )
