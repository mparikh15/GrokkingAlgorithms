import random

list2 = []
lenOfList = 5

def numGen():
    for i in range(lenOfList):
        list2.append(random.randint(0, 1000))

    return list2


def seeAns():
    x = raw_input("See set? ").upper()
    if "YES" in x:
        print input
    else:
        pass

def binary(alist, item):
    low = 0
    high = len(alist) - 1
    found = False

    while low <= high and not found:
        guess = (low + high) // 2
        if alist[guess] == item:
            found = True

        else:
            if item > alist[guess]:
                low = guess + 1
            else:
                high = guess - 1

    return found

input = sorted(numGen())
seeAns()

x = raw_input("Please enter a number to search for : "  )
x = int(x)

print binary(input, x)