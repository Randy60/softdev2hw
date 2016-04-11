import random
def qs(l):
    if len(l) <= 0:
        return l
    pivot = random.choice(l)
    return qs([x for x in l if x < pivot])
    +[x for x in l if x == pivot]
    +qs([x for x in l if x > pivot])

def check(l):
    i = 0
    while i < len(l)-1:
        if l[i] > l[i+1]:
            return False
        i+=1
    return True

l = []
i = 0
for i in range(20000):
    l.append(random.randint(0,100000))

print check(l)
l = qs(l)
print check(l)
