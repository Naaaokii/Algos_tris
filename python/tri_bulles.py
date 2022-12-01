from random import randrange
t = [randrange(0, 10) for i in range(10)]
print(t)
def tri_bulles(t):
    l = len(t)
    for i in range (l-1, 1, -1):
        for j in range(0,i):
            if t[j+1] < t[j]:
                tab = t[j+1]
                t[j+1] = t[j]
                t[j] = tab
    return t 
print(tri_bulles(t))