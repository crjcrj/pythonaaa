from typing import List
import random
def randlist(a):
    randlist = []
    for i in range(a):
        res = random.randint(1, 100)
        randlist.append(res)
    return randlist
