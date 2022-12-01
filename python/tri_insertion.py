from random import randrange
my_tab = [randrange(101) for i in range(20)]
print(my_tab)

#min_values= (min(my_tab))
#print(min_values)
def tri_insertion(my_tab):
    for i in range (1, len(my_tab)):
        a = my_tab[i]
        b = i-1
        while b >= 0 and my_tab[b] > a: 
            my_tab[b + 1] = my_tab[b] 
            b -= 1
        my_tab[b + 1] = a 
    return my_tab

print(tri_insertion(my_tab)) 
# tab_sorted= []
# import 
# my_tab[0]= min_values
#while
