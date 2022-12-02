from random import randrange
A = [randrange(0, 20) for i in range(20)]
print(A)
def tri_selection(A):
    compteur = 0
    for i in range(len(A)):
        for j in range(i + 1, len(A)):
            compteur+=1
            if A[i] > A[j]:
                A[i], A[j] = A[j], A[i]
                compteur+=3
    return compteur
print(tri_selection(A))


def stat(min, max, step, nbr):
    for i in range(min, max+1, step):
        moyenne = 0
        for j in range(nbr):
            t= [randrange(100) for i in range(i)]
            moyenne += tri_selection(t)
        moyenne = moyenne/nbr    
        print(i, moyenne)
    return "Calculs finis"
    
print(stat(10,20,5,10))