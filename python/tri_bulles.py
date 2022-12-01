from random import randrange
t = [1,3,9,95,6,2,1]
print(t)
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
print(tri_bulles(t))

def stat(min, max, step, nbr):
    for i in range(min, max+1, step):
        moyenne = 0
        for j in range(nbr):
            t= [randrange(100) for i in range(i)]
            moyenne += tri_bulles(t)
        moyenne = moyenne/nbr    
        print(i, moyenne)
    return "Calculs finis"
    
print(stat(10,20,5,10))
