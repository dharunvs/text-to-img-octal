import random

def addjunk(a, fake=False):
    n = int(len(a)/(len(a)/5))

    li = list(a)

    s = "4" if fake else "9" 

    for _ in range(n):
        r = random.randint(0, len(a)-1)
        l = li[r:]
        li = li[:r] + [s] + l

    li = "".join(li)

    return((li, n))

def removejunk(a):
    a = list(a)
    a = [num for num in a if num != '9']
    a = "".join(a)
    return a

# print(removejunk("110145154154157157056056040116141141040144150141141040155141163163165"))
# print(addjunk("110145154154157157056056040116141141040144150141141040155141163163165"))