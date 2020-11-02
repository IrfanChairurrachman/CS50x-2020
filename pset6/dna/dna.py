import sys, csv


DB = "databases/small.csv"

if len(sys.argv) != 2 and len(sys.argv) != 3:
    sys.exit("Usage: python dna.py [databases] [sequences]")
    sys.exit(1)

database = sys.argv[1] if len(sys.argv) == 3 else DB

with open(database, newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        m = list(row.keys())
        strs = []
        for dic in m[1:]:
            strs.append(dic)
            # print(dic)
        break
print(strs)
strdict = dict.fromkeys(strs)
print(strdict)
strdict['AGATC'] = []
strdict['AGATC'].append('moo')
strdict['AGATC'].append('mbe')
print(strdict)
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

# if read_txt.find("AGATC"):
#     print("TRUE")
# i = read_txt.find("AGATC")
# print(read_txt.find("AGATC"))
def findstr(txt, strs):
    i = txt.find(strs) + len(strs)
    if txt.find(strs) == 0:
        return 1 + findstr(txt[i:], strs)
    else:
        return 0
    # return txt
# print(read_txt[56:].find("AGATC"))
m = 'AGATC'
print(read_txt.find(m))
print(findstr(read_txt[55:], m))
for key in strs:
    # m = 0
    strdict[key] = []
    print(key)
#     while True:
#         m = read_txt[m:].find(key)
#         if m == -1:
#             break
#         y = findstr(read_txt[m:], key)
#         strdict[key].append(y)
print(strdict)
