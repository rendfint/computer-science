import re
import sqlite3
from sqlite3 import Error
import xml.etree.ElementTree as ET

conn = None

try :
    conn = sqlite3.connect("trackdb.sqlite")
    cur = conn.cursor()
    print("Succesfully connected to database.\n")
except Error as e:
    print("Can't connect to database. Error:", e,"\n")

cur.execute("DROP TABLE IF EXISTS Artist")
cur.execute("DROP TABLE IF EXISTS Genre")
cur.execute("DROP TABLE IF EXISTS Album")
cur.execute("DROP TABLE IF EXISTS Track")
print("Database cleaned successfully.\n")

cur.execute("""
    CREATE TABLE Artist (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        name TEXT UNIQUE
        )
    """)
print("Artist table created successfully.")

cur.execute("""
     CREATE TABLE Genre (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        name TEXT UNIQUE
        )
    """)
print("Genre table created successfully.")

cur.execute("""
    CREATE TABLE Album (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        title TEXT UNIQUE,
        artist_id INTEGER
        )
    """)
print("Album table created successfully.")

cur.execute("""
    CREATE TABLE Track (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        title TEXT UNIQUE,
        album_id INTEGER,
        genre_id INTEGER,
        len INTEGER,
        rating INTEGER,
        count INTEGER
        )
    """)
print("Track table created successfully.\n")

file = input("Enter iTunes library file: ")
if len(file) < 1 : file = "Library.xml"

try :
    tree = ET.parse(file)
    print("File accessed:", file, "\n")
except :
    print("Can't find file:", file,"\n")
    quit()

root = tree.getroot()

tracks = root.findall("dict/dict/dict")

def get_data (key, dict) :
    found = False
    for data in dict :
        if found is True :
            return data.text
            break
        if data.tag == "key" and data.text == key :
            found = True
    return None

lst = list()
for child in tracks :
    if get_data("Track ID", child) is None : continue

    track = get_data("Name", child)
    if track is None : continue
    artist = get_data("Artist", child)
    if artist is None : continue
    album = get_data("Album", child)
    if album is None : continue
    genre = get_data("Genre", child)
    if genre is None : continue
    length = get_data("Total Time", child)
    rating = get_data("Rating", child)
    count = get_data("Play Count", child)

    cur.execute("INSERT OR IGNORE INTO Artist (name) VALUES (?) ", (artist,))
    cur.execute("SELECT id FROM Artist WHERE name = ?", (artist, ))
    artist_id = cur.fetchone()[0]

    cur.execute("INSERT OR IGNORE INTO Genre (name) VALUES (?)", (genre,))
    cur.execute("SELECT id FROM Genre WHERE name = ?", (genre,))
    genre_id = cur.fetchone()[0]

    cur.execute("INSERT OR IGNORE INTO Album (title, artist_id) VALUES (?,?)", (album, artist_id,))
    cur.execute("SELECT id FROM Album WHERE title = ?", (album,))
    album_id = cur.fetchone()[0]

    cur.execute("INSERT OR IGNORE INTO Track (title, album_id, genre_id, len, rating, count) VALUES (?,?,?,?,?,?)", (track, album_id, genre_id, length, rating, count,))

conn.commit()

cur.execute("""SELECT Track.title, Artist.name, Album.title, Genre.name 
    FROM Track JOIN Genre JOIN Album JOIN Artist 
    ON Track.genre_id = Genre.ID and Track.album_id = Album.id 
        AND Album.artist_id = Artist.id
    ORDER BY Artist.name LIMIT 3""")

threeitems = cur.fetchall()
print(threeitems)