from random import randrange
A = [randrange(1, 21) for i in range(20)]

def tri_bulles_mieux(T):
    Continue = True
    passage = 0
    compteur = 0
    while Continue == True:
        Continue = False  # it is assumed that there are no more exchanges to be made
        passage += 1
        for beginning in range(0, len(T) - passage):
            compteur += 1
            if T[beginning] > T[beginning + 1]:
                Continue = True  # we must continue because an exchange has been made
                provisional = T[beginning + 1]
                T[beginning + 1] = T[beginning]
                T[beginning] = provisional
                compteur += 3
    return compteur

def stat(min, max, step, nbr):
    for i in range(min, max+1, step):
        moyenne = 0
        for j in range(nbr):
            t= [randrange(100) for i in range(i)]
            moyenne += tri_bulles_mieux(t)
        moyenne = moyenne/nbr    
        print(i, moyenne)
    return "Calculs finis"
    
print(stat(10,20,5,10))