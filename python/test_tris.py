# Tri bulles


# Tri bulles mieux

def tri_bulles_mieux(A):
    Continue = True
    passage = 0
    while Continue == True:
        Continue = False  # it is assumed that there are no more exchanges to be made
        passage += 1
        for beginning in range(0, len(A) - passage):
            if A[beginning] > A[beginning + 1]:
                Continue = True  # we must continue because an exchange has been made
                provisional = A[beginning + 1]
                A[beginning + 1] = A[beginning]
                A[beginning] = provisional
    return A

# Tri Selection

def tri_selection(A):
    for i in range(len(A)):
        for j in range(i + 1, len(A)):
            if A[i] > A[j]:
                A[i], A[j] = A[j], A[i]
    return A

# Tri Insertion

# Avec un tableau déjà trié

print("Tableau déjà trié")
print()
from random import randrange
from time import time
A = [randrange(10, 5001) for i in range(5000)]
for i in A:
    for k in range(5000):
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
A = [randrange(10, 5001) for i in range(5000)]

for i in A:
    for k in range(5000):
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
A = [randrange(10, 5001) for i in range(5000)]

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
