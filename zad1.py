import random
elementi=list(range(1,11))
i=0
lista=[]
while (i<5):
    a=random.choice(elementi)
    elementi.remove(a)
    a=(a,random.choice(elementi))
    elementi.remove(a[1])
    lista.append(a)
    i+=1
print(lista)
