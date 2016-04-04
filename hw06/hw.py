import math
p1="pass"
p2="password"
p3="Password"
p4="myNoobPass1234"
p5="myNoobPass1234!"
p_list = [p1,p2,p3,p4,p5]


UC_LETTERS="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
LC_LETTERS="qwertyuiopasdfghjklzxcvbnm"
NUMBERS="1234567890"
SYMBOLS=".?!&#,;:-_*"

def password_strength(p):
    strength=0
    U=UC_LETTERS
    L=LC_LETTERS
    N=NUMBERS
    S=SYMBOLS
    if len(p) > 8:
        strength+=1
    for x in p:
        if x in U:
            strength+=1
            U=""
    for x in p:
        if x in L:
            strength+=1
            L=""
    for x in p:
        if x in N:
            strength+=1
            N=""
    for x in p:
        if x in S:
            strength+=1
            S=""
    return strength
def password_boolean(p):
    return password_strength(p) == 5

def p_strength2(p):
    l= [1 if x in UC_LETTERS else
        2 if x in LC_LETTERS else
        3 if x in NUMBERS else
        4 if x in SYMBOLS else 0
        for x in p]
    c1 = len(p) - l.count(1)
    c2 = len(p) - l.count(2)
    c3 = len(p) - l.count(3)
    c4 = len(p) - l.count(4)
    val = math.sqrt(math.pow(c1,2)+math.pow(c2,2)+math.pow(c3,2)+math.pow(c4,2))
    return math.pow(len(p),2)/val

for x in p_list:
    print " "+x+" "+str(password_strength(x))+"/"+str(p_strength2(x))+' '+str(password_boolean(x))+"\n"


#YOUR TASK The First:
#Write a function that uses list comprehension to return whether a password meets a minimum threshold: it contains a mixture of upper- and lowercase letters, and at least one number.


#YOUR TASK The Second:
#Write a function that uses list comprehension to return a password's strength rating. This function should return a low integer for a weak password and a higher integer for a stronger password. (Suggested scale: 1-10)
#Consider these criteria:
#* mixture of upper- and lower-case
#* inclusion of numerals
#* inclusion of these non-alphanumeric chars: . ? ! & # , ; : - _ *

def repeat(x):
    def f(y):
        str = ''
        while y > 0:
            str += x
            y-=1
        return str
    return f

r1 = repeat('hello')
r2 = repeat('goodbye')

print r1(2)
print r2(2)
print repeat('cool')(3)
