from random import randrange
A = [randrange(0, 20) for i in range(20)]
print(A)
def tri_selection(A):
    for i in range(len(A)):
        for j in range(i + 1, len(A)):
            if A[i] > A[j]:
                A[i], A[j] = A[j], A[i]
    return A
print(tri_selection(A))


