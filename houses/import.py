# TODO
from cs50 import SQL
import csv
from sys import argv, exit

db = SQL("sqlite:///students.db")

# ask for 2 command line arguments (after python)

if len(argv) != 2:
    print("Error. Specify Python program and CSV File")
    exit(1)

# open CSV File

file = open(argv[1], "r")
reader = csv.DictReader(file)

# insert csv file into the database

for row in reader:
    name = row['name'].split()
    if len(name) == 3:
        db.execute("INSERT INTO students (first, middle, last, house, birth) VALUES (?, ?, ?, ?, ?)",
                   name[0], name[1], name[2], row['house'], row['birth'])
    if len(name) == 2:
        db.execute("INSERT INTO students (first, middle, last, house, birth) VALUES (?, ?, ?, ?, ?)",
                   name[0], None, name[1], row['house'], row['birth'])

