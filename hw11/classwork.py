import time

def timer(f):
    name = f.func_name
    def inner( *args ):
        now = time.time()
        temp = f( *args )
        now = int(time.time()-now)
        print (name + "("+str(*args)+")-->" + str(temp)+"\n"+
                "-->" + str(now) + " seconds")+"\n"+"----------------"
        return temp
    return inner

def fib(n):
    if n < 2:
        return 1
    return fib(n-1)+fib(n-2)

def memoize(f):
    memo = {}
    def inner(x):
        if x not in memo:
            memo[x] = f(x)
        return memo[x]
    return inner

f = timer(fib)
for i in range(1,40):
    f(i)
fib = memoize(fib)
#for i in range(1,5):
#    f(i)
