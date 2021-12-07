import json
import sqlite3

conn = None

try :
    print("\nConnecting to database.")
    conn = sqlite3.connect("roster.sqlite")
    cur = conn.cursor()
    print("Succesfully connected to database.\n")
except Error as e:
    print("Can't connect to database. Error:", e,"\n")

print("Deleting database data.")
cur.executescript("""
        DROP TABLE IF EXISTS User;
        DROP TABLE IF EXISTS Course;
        DROP TABLE IF EXISTS Member;
    """)
print("Data successfully deleted.\n")

print("Creating new tables.")
cur.executescript("""
    CREATE TABLE User (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        name TEXT UNIQUE);
    CREATE TABLE Course (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        title TEXT UNIQUE);
    CREATE TABLE Member (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        user_id INTEGER,
        course_id INTEGER,
        role INTEGER);
    """)
print("Tables successfully created.\n")

filename = input("Enter JSON file name: \n>")
if len(filename) < 1 : filename = "roster_data.json" 

print("\nLoading file", filename)
fhandle = open(filename)
json_data = json.loads(fhandle.read())
print(filename, "loaded successfully.\n")

print("Adding file data to database.")
for user in json_data :
    name = user[0]
    course = user[1]
    role = user[2]

    cur.execute("INSERT OR IGNORE INTO User (name) VALUES (?)", (name,))
    cur.execute("SELECT id FROM User WHERE name = ?", (name,))
    user_id = cur.fetchone()[0]

    cur.execute("INSERT OR IGNORE INTO Course (title) VALUES (?)", (course,))
    cur.execute("SELECT id FROM Course WHERE title = ?", (course,))
    course_id = cur.fetchone()[0]

    cur.execute("INSERT OR IGNORE INTO Member (user_id, course_id, role) VALUES (?,?,?)", (user_id, course_id, role))

conn.commit()
print("Data successfully added to database.\n")