import sys, csv

DB = "databases/large.csv"

if len(sys.argv) != 2 and len(sys.argv) != 3:
    sys.exit("Usage: python dna.py [databases] [sequences]")
    sys.exit(1)

database = sys.argv[1] if len(sys.argv) == 3 else DB

with open(database, newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    rows = [dict(row) for row in reader]

for row in rows:
    m = list(row.keys())
    # print(row)
    strs = []
    for dic in m[1:]:
        # print(dic)
        strs.append(dic)
    break
# print(rows)
strdict = dict.fromkeys(strs)
# print(strs)
text = sys.argv[2] if len(sys.argv) == 3 else sys.argv[1]

txt_file = open(text, "r")

if not txt_file:
    print("Could not open {}", format(text))
    txt_file.close()
    sys.exit(1)

read_txt = txt_file.read()
# print(type(read_txt))
# print(read_txt)

def findstr(txt, strs):
    i = txt.find(strs) + len(strs)
    if txt.find(strs) == 0:
        return 1 + findstr(txt[i:], strs)
    else:
        return 0
    
for key in strs:
    m = read_txt.find(key)
    x = 0
    strdict[key] = []
    while True:
        if m == -1:
            break
        y = findstr(read_txt[x:], key)
        strdict[key].append(y)
        x = x + len(key) + m
        m = read_txt[x:].find(key)
print(strdict)

# check = False
# for row in rows:
#     # print(row)
#     for dna in strdict.items():
#         # print(row[dna[0]], end=' ')
#         # print(dna[1])
#         value = 0 if not dna[1] else max(dna[1])
#         if int(row[dna[0]]) == value:
#             check = True
#         else:
#             check = False
#             break
#     if check == True:
#         print(row['name'])
#         break

# if check == False:
#     print("No match")

for dna in strdict.items():
    value = 0 if not dna[1] else max(dna[1])
    print(value)
