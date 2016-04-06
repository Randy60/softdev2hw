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

print pt(0)
print pt(6)
print pt(25)

def pt2(z):
    trips = []
    for a in range (1,z+1):
        for b in range (a,z+1):
            for c in range (b,z+1):
                if a*a + b*b == c*c:
                    trips.append((a,b,c))
    return trips

print " "
print pt2(0)
print pt2(6)
print pt2(25)

def pt3(z):
    return [(a,b,c)
        for a in range (1,z+1)
        for b in range (a+1,z+1)
        for c in range (b+1,z+1)
        if a*a + b*b == c*c
    ]

print " "
print pt3(0)
print pt3(6)
print pt3(25)

import random
def qs(l):
    return[
    
    ]
