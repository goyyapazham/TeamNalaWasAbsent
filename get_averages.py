import sqlite3
import subprocess

#run db_builder
subprocess.call(['python', 'db_builder.py'])

#set up database
db = sqlite3.connect("discobandit.db") 
cur = db.cursor()

#get name & grade from db
cur.execute("SELECT name, mark FROM students, courses WHERE students.id == courses.id")

#set up dictionary, which will be in this format:
'''
{
    <name 1>: [<grade 1>, ...],
    <name 2>: [<grade 1>, ...]
    ...
}
'''
def make_dict():
    d = {}
    for record in cur:
        name = record[0]
        mark = record[1]
        if name in d:
            d[name] += [mark]
        else:
            d[name] = [mark]
    return d

#helper fxn to calculate the average grade given a list of grades
def get_average(L):
    i = len(L)
    s = 0
    for x in L:
        s += x
    return float(s/i)

#new dict form
'''
{
    <name 1>: get_average([<grade 1>, ...]),
    <name 2>: get_average([<grade 1>, ...]),
    ...
}
'''
def refresh_dict(d):
    for key in d:
        d[key] = get_average(d[key])
    return d

#print dict
def print_dict(d):
    for key in d:
        print "%s: %d"%(key, d[key])

#run prgm
print_dict(refresh_dict(make_dict()))
