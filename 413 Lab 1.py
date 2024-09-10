import time
import random


def createList(n, m):
    templist = []
    for i in range(n):
        randint = random.randint(0, m)
        templist.append(randint)
    return templist


# EXERCISE 1:

def findDupeIndex(list):
    dictDupes = {}
    for i in range(len(list)):
        if list[i] in dictDupes:
            print(f"DUPE FOUND AT INDEX {i}!")
            break
        else:
            dictDupes[list[i]] = 1


list = createList(1000, 5000)
start = time.time()
findDupeIndex(list)
end = time.time()
print(f"Time taken: {end - start}\n")

# EXERCISE 2:
print("\nITERATIVE MIN/MAX\n\n")


def findMinMax(list):
    if len(list) > 0:
        min, max = list[0], list[0]
        for i in range(len(list)):
            if list[i] < min:
                min = list[i]
            if list[i] > max:
                max = list[i]
        print(f"MIN: {min} MAX: {max}")


list = createList(2500, 100000)
start = time.time()
findMinMax(list)
end = time.time()
print(f"Time taken: {end - start}\n")

list = createList(5000, 100000)
start = time.time()
findMinMax(list)
end = time.time()
print(f"Time taken: {end - start}\n")

# EXERCISE 3:
print("\nDIVIDE AND CONQUER MIN/MAX\n\n")


def divide(s):
    if len(s) <= 1:
        return (s[0], s[0])
    else:
        mid = len(s) // 2
        LMin, LMax = divide(s[:mid])
        RMin, RMax = divide(s[mid:])
        min = LMin
        max = LMax
        if (RMin < LMin):
            min = RMin
        if (RMax > LMax):
            max = RMax
        return [min, max]


def findMinMaxDAC(list):
    min, max = divide(list)
    print(f"MIN: {min} MAX: {max}")


list = createList(2500, 100000)
start = time.time()
findMinMaxDAC(list)
end = time.time()
print(f"Time taken: {end - start}\n")

list = createList(5000, 100000)
start = time.time()
findMinMaxDAC(list)
end = time.time()
print(f"Time taken: {end - start}\n")

