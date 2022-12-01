from random import randrange
A = [randrange(1, 21) for i in range(20)]

def tri_bulles_mieux(T):
    Continue = True
    passage = 0
    while Continue == True:
        Continue = False  # it is assumed that there are no more exchanges to be made
        passage += 1
        for beginning in range(0, len(T) - passage):
            if T[beginning] > T[beginning + 1]:
                Continue = True  # we must continue because an exchange has been made
                provisional = T[beginning + 1]
                T[beginning + 1] = T[beginning]
                T[beginning] = provisional
    return T

print(tri_bulles_mieux(A))