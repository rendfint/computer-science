import sqlite3
import re

conn = sqlite3.connect("emaildb.sqlite")
cur = conn.cursor()

cur.execute("DROP TABLE IF EXISTS Counts")
cur.execute("CREATE TABLE Counts (org TEXT, count INTEGER)")

filename = input("Enter file name: ")
if len(filename) < 1 :
    filename = "mbox-short.txt"

fhandle = open(filename)

for line in fhandle :
    if not line.startswith("From: ") : continue
    org = re.findall("(?<=@).+", line)
    cur.execute("SELECT count FROM Counts where org = ? ", (org[0],))
    row = cur.fetchone()
    if row is None :
        cur.execute("INSERT INTO Counts (org, count) VALUES (?, 1)", (org[0],))
    else :
        cur.execute("UPDATE Counts SET count = count + 1 WHERE org = ?", (org[0],))

conn.commit()

sqlquery = "SELECT org, count FROM Counts ORDER BY count DESC LIMIT 10"

for row in cur.execute(sqlquery) :
    print(row[0], row[1])