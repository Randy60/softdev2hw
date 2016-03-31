p="myNoobPass1234"
p2="myNoobPass1234!"
print [x+" " for x in p]

#[x for x in "1234"]    ->  ?


UC_LETTERS="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
LC_LETTERS="qwertyuiopasdfghjklzxcvbnm"
NUMBERS="1234567890"
SYMBOLS=".?!&#,;:-_*"

print password_strength(p)
print password_strength(p2)

def password_strength(p):
    strength=0
    U=UC_LETTERS
    L=LC_LETTERS
    N=NUMBERS
    S=SYMBOLS
    if p.length > 8:
        strength+=1
    for x in p:
        if x in U:
            strength+=1
            U=""
    for x in p:
        if x in L:
            strength+=1
            L=""
    for x in p
        if x in N
            strength+=1
            N=""
    for x in p
        if x in S
            strength+=1
            S=""
    return strength



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
