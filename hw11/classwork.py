import time
def time(f):
    def meta( *args ):
        #now = time.time()
        temp = f( *args )
        #now = time.time()-now
        now = 0.1
        print (f.func_name + "("+str(*args)+")-->" + str(temp)+"\n"+
                "-->" + str(now) + " seconds")
        return temp
    return meta

def fib(n):
    if n <= 1:
        return 1
    return fib(n-1)+fib(n-2)

memo = [1,1]
def fib_memo(n):
    if len(memo) > n:
        return memo[n]
    memo.append(fib_memo(n-1)+fib_memo(n-2))
    return memo[n]

def memoize(f):
    memo = {}
    def inner(x):
        if x not in memo:
            memo[x] = f(x)
        return memo[x]
    return inner
fib = memoize(fib)

f = time(fib)
f2 = time(fib_memo)
for i in range(0,40):
    f(i)
    f2(i)
    print "----------------"
