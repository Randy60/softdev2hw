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

for x in p_list:
    print " "+x+" "+str(password_strength(x))+" "+str(password_boolean(x))+"\n"
#[ x for x in p if x in UC_LETTERS ]   ->  ?

#[ 1 for x in p if x in UC_LETTERS ]   ->  ?

#[ 1 if x in UC_LETTERS else 0 for x in p ]  ->  ?



#YOUR TASK The First:
#Write a function that uses list comprehension to return whether a password meets a minimum threshold: it contains a mixture of upper- and lowercase letters, and at least one number.


#YOUR TASK The Second:
#Write a function that uses list comprehension to return a password's strength rating. This function should return a low integer for a weak password and a higher integer for a stronger password. (Suggested scale: 1-10)
#Consider these criteria:
#* mixture of upper- and lower-case
#* inclusion of numerals
#* inclusion of these non-alphanumeric chars: . ? ! & # , ; : - _ *
