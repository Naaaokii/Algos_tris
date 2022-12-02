# Tri bulles

def tri_bulles(t):
    compteur = 0
    l = len(t)
    for i in range (l-1, 1, -1):
        for j in range(0,i):
            compteur+=1
            if t[j+1] < t[j]:
                tab = t[j+1]
                t[j+1] = t[j]
                t[j] = tab
                compteur+=3
    return compteur 

def stat_bulles_trie(min, max, step, nbr):
    for i in range(min, max+1, step):
        moyenne = 0
        for j in range(nbr):
            t = [randrange(100) for i in range(i)]
            for z in t:
                for k in range(i):
                    t[k] = k
            moyenne += tri_bulles(t)
        moyenne = moyenne/nbr    
        print(i, moyenne)
    return "Tri à bulles finis"


def stat_bulles_pas_trie(min, max, step, nbr):
    for i in range(min, max+1, step):
        moyenne = 0
        for j in range(nbr):
            t = [randrange(100) for i in range(i)]
            for z in t:
                for k in range(i):
                    t[k] = k
            t = [num for num in reversed(t)]
            moyenne += tri_bulles(t)
        moyenne = moyenne/nbr    
        print(i, moyenne)
    return "Tri à bulles finis"




# Tri bulles mieux

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


def stat_bulles_mieux_trie(min, max, step, nbr):
    for i in range(min, max+1, step):
        moyenne = 0
        for j in range(nbr):
            t = [randrange(100) for i in range(i)]
            for z in t:
                for k in range(i):
                    t[k] = k
            moyenne += tri_bulles_mieux(t)
        moyenne = moyenne/nbr    
        print(i, moyenne)
    return "Tri à bulles optimisé finis"

def stat_bulles_mieux_pas_trie(min, max, step, nbr):
    for i in range(min, max+1, step):
        moyenne = 0
        for j in range(nbr):
            t = [randrange(100) for i in range(i)]
            for z in t:
                for k in range(i):
                    t[k] = k
            t = [num for num in reversed(t)]
            moyenne += tri_bulles_mieux(t)
        moyenne = moyenne/nbr    
        print(i, moyenne)
    return "Tri à bulles optimisé finis"





# Tri Selection

def tri_selection(A):
    compteur = 0
    for i in range(len(A)):
        for j in range(i + 1, len(A)):
            compteur+=1
            if A[i] > A[j]:
                A[i], A[j] = A[j], A[i]
                compteur+=3
    return compteur

def stat_selection_trie(min, max, step, nbr):
    for i in range(min, max+1, step):
        moyenne = 0
        for j in range(nbr):
            t = [randrange(100) for i in range(i)]
            for z in t:
                for k in range(i):
                    t[k] = k
            moyenne += tri_selection(t)
        moyenne = moyenne/nbr    
        print(i, moyenne)
    return "Tri selection finis"

def stat_selection_pas_trie(min, max, step, nbr):
    for i in range(min, max+1, step):
        moyenne = 0
        for j in range(nbr):
            t = [randrange(100) for i in range(i)]
            for z in t:
                for k in range(i):
                    t[k] = k
            t = [num for num in reversed(t)]
            moyenne += tri_selection(t)
        moyenne = moyenne/nbr    
        print(i, moyenne)
    return "Tri selection finis"




# Tri Insertion

def tri_insertion(my_tab):
    compteur = 0
    for i in range (1, len(my_tab)):
        a = my_tab[i]
        b = i-1
        compteur+=1
        while b >= 0 and my_tab[b] > a: 
            my_tab[b + 1] = my_tab[b] 
            b -= 1
            compteur+=3
        my_tab[b + 1] = a 
    return compteur

def stat_insertion_trie(min, max, step, nbr):
    for i in range(min, max+1, step):
        moyenne = 0
        for j in range(nbr):
            t = [randrange(100) for i in range(i)]
            for z in t:
                for k in range(i):
                    t[k] = k
            moyenne += tri_insertion(t)
        moyenne = moyenne/nbr    
        print(i, moyenne)
    return "Tri insertion finis"

def stat_insertion_pas_trie(min, max, step, nbr):
    for i in range(min, max+1, step):
        moyenne = 0
        for j in range(nbr):
            t = [randrange(100) for i in range(i)]
            for z in t:
                for k in range(i):
                    t[k] = k
            t = [num for num in reversed(t)]
            moyenne += tri_insertion(t)
        moyenne = moyenne/nbr    
        print(i, moyenne)
    return "Tri insertion finis"




# Avec un tableau déjà trié

print("Tableau déjà trié")
print()
from random import randrange
from time import time
A = [randrange(10, 1001) for i in range(1000)]
for i in A:
    for k in range(1000):
        A[k] = k

debut_bulles = time()
tri_bulles(A)
fin_bulles = time()

debut_bulles_mieux = time()
tri_bulles_mieux(A)
fin_bulles_mieux = time()

debut_selection = time()
tri_selection(A)
fin_selection = time()

debut_insertion = time()
tri_insertion(A)
fin_insertion = time()

print("durée du tri_bulles :", fin_bulles - debut_bulles)
print("durée du tri_bulles_mieux :", fin_bulles_mieux - debut_bulles_mieux)
print("durée du tri_selection :", fin_selection - debut_selection)
print("durée du tri_insertion :", fin_insertion - debut_insertion)
print()

# Avec un tableau trié dans le pire des cas
print("tableau dans le pire des cas")
print()
from random import randrange
from time import time
A = [randrange(10, 1001) for i in range(1000)]

for i in A:
    for k in range(1000):
        A[k] = k
AA = [num for num in reversed(A)]

debut_bulles = time()
tri_bulles(AA)
fin_bulles = time()

debut_bulles_mieux = time()
tri_bulles_mieux(AA)
fin_bulles_mieux = time()

debut_selection = time()
tri_selection(AA)
fin_selection = time()

debut_insertion = time()
tri_insertion(AA)
fin_insertion = time()

print("durée du tri_bulles :", fin_bulles - debut_bulles)
print("durée du tri_bulles_mieux :", fin_bulles_mieux - debut_bulles_mieux)
print("durée du tri_selection :", fin_selection - debut_selection)
print("durée du tri_insertion :", fin_insertion - debut_insertion)
print()


# Avec un tableau trié aléatoirement
print("Tableau trié aléatoirement")
print()

from random import randrange
from time import time
A = [randrange(10, 1001) for i in range(1000)]

debut_bulles = time()
tri_bulles(A)
fin_bulles = time()

debut_bulles_mieux = time()
tri_bulles_mieux(A)
fin_bulles_mieux = time()

debut_selection = time()
tri_selection(A)
fin_selection = time()

debut_insertion = time()
tri_insertion(A)
fin_insertion = time()

print("durée du tri_bulles :", fin_bulles - debut_bulles)
print("durée du tri_bulles_mieux :", fin_bulles_mieux - debut_bulles_mieux)
print("durée du tri_selection :", fin_selection - debut_selection)
print("durée du tri_insertion :", fin_insertion - debut_insertion)




# Tests des stats
print()
print()
print("Tableau déjà triés")
print()
print(stat_bulles_trie(10,20,5,10))
print()
print(stat_bulles_mieux_trie(10,20,5,10))
print()
print(stat_selection_trie(10,20,5,10))
print()
print(stat_insertion_trie(10,20,5,10))
print()
print()
print()
print("Tableau pas triés")
print()
print(stat_bulles_pas_trie(10,20,5,10))
print()
print(stat_bulles_mieux_pas_trie(10,20,5,10))
print()
print(stat_selection_pas_trie(10,20,5,10))
print()
print(stat_insertion_pas_trie(10,20,5,10))
