# TODO
import sys, cs50

# check argv
if len(sys.argv) != 2 or sys.argv[1] not in ['Gryffindor', 'Hufflepuff', 'Ravenclaw', 'Slytherin']:
    sys.exit("Usage: python roster.py [house name] or there's no house name")
    sys.exit(1)

# connect to db
db = cs50.SQL("sqlite:///students.db")
# execute SQL command and store to students list
students = db.execute("SELECT * FROM students WHERE house = (?) order by last, first", sys.argv[1])

for student in students:
    if student['middle'] == None:
        print("{} {}, born {}".format(student['first'], student['last'], student['birth']))
    else:
        print("{} {} {}, born {}".format(student['first'], student['middle'], student['last'], student['birth']))
