# I can do it more efficient
# I just want to implement my pset1 C code to python

from cs50 import get_float 

# Loop to get input
while True:
    # get input
    dollars = get_float("Change owed: ")
    coins = int(dollars * 100)

    # break loop if condition right
    if coins > 0:
        break

# print(coins)
i = 0

while coins != 0:
    if (coins - 25) >= 0:
        coins = coins - 25
        i += 1
    elif (coins - 10) >= 0:
        coins = coins - 10
        i += 1
    elif (coins - 5) >= 0:
        coins = coins - 5
        i += 1
    elif (coins - 1) >= 0:
        coins = coins - 1
        i += 1

print(i)

