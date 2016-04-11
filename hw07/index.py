def inc(x):
    return x+1
def dec(x):
    return x-1
def dub(x):
    return x*2
def hav(x):
    return x/2
f = inc
print f(5)
flist = [inc,dec]
print flist[1](5)

def makeAdder(n):
    def inner(x):
        return x+n
    return inner

add3 = makeAdder(3)
add5 = makeAdder(5)

def make_counter():
    count = [0]
    def inc():
        count[0]+=1
    def dec():
        count[0]-=1
    def reset():
        count[0]=0
    def get():
        return count[0]
    return {'inc':inc, 'dec':dec, 'reset':reset, 'get':get}

c1 = make_counter()
c2 = make_counter()

c1['inc']()
c1['inc']()
c1['inc']()
print c1['get']()

c2['inc']()
print c2['get']()

c1['reset']()
print c1['get']()

import random
def get_name():
    names = ['Aaron', 'Bart', 'Charlie', 'Dick', 'Eugene', 'Frank','Gary']
    return random.choice(names)

def dbl(f):
    name = f()
    return name+" "+name

print dbl(get_name)

get_name = dbl(get_name)

print get_name
