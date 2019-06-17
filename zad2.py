def map_f(myfunction, parametar):
    #return [myfunction(i) for i in parametar]
    a = []       
    for i in parametar:
        a.append(myfunction(i))
    return a

def filter_f(myfunction, parametar):
    a = []       
    for i in parametar:
        a.append(bool(myfunction(i)))
    return a
#return [bool(myfunction(i) for i in parametar]



l = [1,2,3,4]
#l = (1, 2 ,3)
funkc = lambda x: x+2
print(list(filter_f(funkc,l)))
#print(list(map_f(funkc,l)))



