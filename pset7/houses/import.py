# TODO
import sys, csv, cs50

# connect to database
db = cs50.SQL("sqlite:///students.db")

# check argv
if len(sys.argv) != 2:
    sys.exit("Usage: python import.py [characters.csv]")
    sys.exit(1)

# open csv
with open(sys.argv[1], newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    # iterate each row in csv
    for row in reader:
        # split the name 
        name = row['name'].split()
        # if there's no middle name, then insert None in index 1
        if len(name) == 2:
            name.insert(1, None)
        # execute SQL to insert into students.db
        db.execute("INSERT INTO students(first, middle, last, house, birth) VALUES(?, ?, ?, ?, ?)",
                    name[0], name[1], name[2], row['house'], row['birth'])
        
        
