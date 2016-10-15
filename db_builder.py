import sqlite3   #enable control of an sqlite database
import csv       #facilitates CSV I/O

f="discobandit.db"

db = sqlite3.connect(f) #open if f exists, otherwise create
c = db.cursor()    #facilitate db ops

#==========================================================
#INSERT YOUR POPULATE CODE IN THIS ZONE
#...perhaps by beginning with these examples...

q = "CREATE TABLE students (name TEXT, age INTEGER, id INTEGER)"
c.execute(q)
with open('peeps.csv') as csvfile:
    pdata = csv.DictReader(csvfile)
    for row in pdata:
        q = "INSERT INTO students VALUES (\'%s\', %d, %d)" % (row['name'], int(row['age']), int(row['id']))
        c.execute(q)   

q = "CREATE TABLE courses (code TEXT, mark INTEGER, id INTEGER)"
c.execute(q)
with open('courses.csv') as csvfile:
    cdata = csv.DictReader(csvfile)
    for row in cdata:
        q = "INSERT INTO courses VALUES (\'%s\', %d, %d)" % (row['code'], int(row['mark']), int(row['id']))
        c.execute(q)

#==========================================================
db.commit() #save changes
db.close()  #close database

