import sys, csv

# define db if not assign in argv
DB = "databases/large.csv"

# return error if assign not correct
if len(sys.argv) != 2 and len(sys.argv) != 3:
    sys.exit("Usage: python dna.py [databases] [sequences]")
    sys.exit(1)

database = sys.argv[1] if len(sys.argv) == 3 else DB

# open csv and store in rows as dict
with open(database, newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    rows = [dict(row) for row in reader]

# store STR in dict
for row in rows:
    m = list(row.keys())
    # print(row)
    strs = []
    for dic in m[1:]:
        # print(dic)
        strs.append(dic)
    break

strdict = dict.fromkeys(strs)

# Open txt file
text = sys.argv[2] if len(sys.argv) == 3 else sys.argv[1]

txt_file = open(text, "r")

if not txt_file:
    print("Could not open {}", format(text))
    txt_file.close()
    sys.exit(1)

read_txt = txt_file.read()

# function to return max sequences
def findstr(txt, strs):
    i = txt.find(strs) + len(strs)
    if txt.find(strs) == 0:
        return 1 + findstr(txt[i:], strs)
    else:
        return 0

# store count str in strdict list
for key in strs:
    x = read_txt.find(key)
    strdict[key] = []
    while True:
        m = read_txt[x:].find(key)
        # if no str left, then break the loop
        if m == -1:
            break
        y = findstr(read_txt[x+m:], key)
        strdict[key].append(y)
        x = x + len(key) + m
# print(strdict)

# check the str in databases
check = False
for row in rows:
    # print(row)
    for dna in strdict.items():
        # print(row[dna[0]], end=' ')
        # print(dna[1])
        value = 0 if not dna[1] else max(dna[1])
        # if always true, then check = True
        if int(row[dna[0]]) == value:
            check = True
        else:
            # if str not match then break and check return to False
            check = False
            break
    # If check always True, then print name, and break
    if check == True:
        print(row['name'])
        break

# if there are no match, then print No match
if check == False:
    print("No match")

# close the txt file
txt_file.close()

# just for check and debug
# for dna in strdict.items():
#     value = 0 if not dna[1] else max(dna[1])
#     print(value)
