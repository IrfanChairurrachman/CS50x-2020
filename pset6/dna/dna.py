import sys, csv

DB = "databases/large.csv"

if len(sys.argv) != 2 and len(sys.argv) != 3:
    sys.exit("Usage: python dna.py [databases] [sequences]")
    sys.exit(1)

database = sys.argv[1] if len(sys.argv) == 3 else DB

with open(database, newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        m = list(row.keys())
        for dic in m[1:]:
            print(dic)
        break

text = sys.argv[2] if len(sys.argv) == 3 else sys.argv[1]

# print(sys.argv[1])
txt_file = open(text, "r")

if not txt_file:
    print("Could not open {}", format(text))
    txt_file.close()
    sys.exit(1)

read_txt = txt_file.read()
print(type(read_txt))
print(read_txt)

if read_txt.find("AGATC"):
    print("TRUE")
# i = read_txt.find("AGATC")
# print(read_txt.find("AGATC"))
# print(read_txt[56:].find("AGATC"))