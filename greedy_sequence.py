### Adapted from Sam Forman's version ###

import time

def Sidon(n):
    sidonSet = []
    sums = set()
    for i in range(1,n):
        if add(sidonSet, i, sums):
            sidonSet.append(i)
            for num in sidonSet:
                sums.add(i + num)
    print(sidonSet,len(sidonSet))

def add(sidonSet, newNum, sums):
    for num in sidonSet:
        if (newNum + num) in sums:
            return False
    return True
start = time.time()
Sidon(148) # took 496 seconds for me
print(time.time()-start)
