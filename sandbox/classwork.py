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

def timer( f ):
    now = time.time()
    def inner( *arg ):
        return f( *arg )
    now = time.time() - now
    print "-" + now + " " + str(inner)
    return now

closure = timer('pt')
#closure(6)
timer(pt)(6)
