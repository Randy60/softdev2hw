import time

def pt(z):
    trips = []
    a = 0
    b = 0
    c = 0
    n = 3
    while n <= z:
        a = n
        c = (a*a+1)/2
        b = a*a-c
        if a/1 == a and b/1 == b and c/1 == c:
            i = 1
            while i*c <= z:
                trips.append((a*i,b*i,c*i))
                i+=2
        n+=1
    return trips

import random
def qs(l):
    if len(l) <= 0:
        return l
    pivot = random.choice(l)
    return qs([x for x in l if x < pivot])+[x for x in l if x == pivot]+qs([x for x in l if x > pivot])

def check(l):
    i = 0
    while i < len(l)-1:
        if l[i] > l[i+1]:
            return False
        i+=1
    return True

def bs(l):
    a=0
    while not check(l):
        for x in range(0,len(l)/10):
            for i in range(0,len(l)-2):
                if l[i] > l[i+1]:
                    a=l[i]
                    l[i]=l[i+1]
                    l[i+1]=a
    return l


def timer( f ):
    now = time.time()
    def inner( *arg ):
        return f( *arg )
    now = time.time() - now
    print now
    return inner


lst = []
i = 0
for i in range(20000):
    lst.append(random.randint(0,100000))
#print len(lst)
#closure = timer(bs)
#closure(lst)
#print len(lst)
for i in range(20000):
    lst.append(random.randint(0,100000))
print str(check(lst))+str(len(lst))
k=qs(lst)
print str(check(k))+str(len(k))

#timer(pt)(6)
