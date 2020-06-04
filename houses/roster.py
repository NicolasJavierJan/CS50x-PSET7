# TODO
from sys import argv, exit
from cs50 import SQL

# ask for 2 command line arguments (after python)

if len(argv) != 2:
    print("Error. Specify Python program and House")
    exit(1)

db = SQL("sqlite:///students.db")

roster = db.execute("SELECT first, middle, last, birth FROM students WHERE house =? ORDER BY last, first", argv[1])

for row in roster:
    if row['middle'] == None:
        print(row['first'], row['last'] + ", born", row['birth'])
    else:
        print(row['first'], row['middle'], row['last'] + ", born", row['birth'])