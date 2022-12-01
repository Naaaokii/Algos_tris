from random import randrange
t = [1,3,9,95,6,2,1]
print(t)
def tri_bulles(t):
    echange = 0
    l = len(t)
    for i in range (l-1, 1, -1):
        for j in range(0,i):
            if t[j+1] < t[j]:
                tab = t[j+1]
                t[j+1] = t[j]
                t[j] = tab
                echange+=1
    print(echange)
    return t 
print(tri_bulles(t))

def stat(min, max, step, nbr):
    t = [randrange(min, max, step) for i in range(nbr)]
    return t

print(stat(10,20,5,10))