lista_zanrova=['action','puzzle','adventure','social','fighting']
fil_zanr=lambda x: x in lista_zanrova
pravila=lambda x:2<len(x[0])<50 and 0.99<float(x[1])<10.01 and 1950<int(x[2])<=2019 and 2<len(x[3])<40 and len(x[4])<4
fajl=open('fajligrice.txt','r',newline="")
fajl.seek(0)
fajl_igrice=fajl.readlines()
igrice=[]
for row in fajl_igrice:
    row=row.lower()
    igrica=row.split(';')
    igrica[4]=igrica[4].split()
    igrica[4]=list(filter(fil_zanr,igrica[4]))
    igrice.append(igrica)
fil_igrice=filter(pravila,igrice)
print(list(fil_igrice))

def unos_igrica():
    nastavak=input('Da li želite nastaviti unos igara?').lower()
    if nastavak=='da':
        nova_igrica=input()
        nova_igrica=nova_igrica.lower()
        nova_igrica_lista=nova_igrica.split(';')
        nova_igrica_lista[4]=nova_igrica_lista[4].split()
        nova_igrica_lista[4]=list(filter(fil_zanr,nova_igrica_lista[4]))
        try:
            pravila(nova_igrica)
            if pravila(nova_igrica_lista):
                fajl=open('fajligrice.txt','a',newline="")
                fajl.write('\n')
                fajl.write(nova_igrica)
                unos_igrica()
            else:
                print("Molimo vas unesite ispravne podatke.")
                unos_igrica()
        except Exception:
            print("Molimo vas unesite ispravne podatke.")
            unos_igrica()
    elif nastavak=='ne':
            print("Nastavljamo dalje")
    else:
        print("Unesite DA ili NE")
        unos_igrica()

unos_igrica()

def kreiraj_dict():
    fajl=open('fajligrice.txt','r',newline="")
    fajl.seek(0)
    lista_igara=[]
    for row in fajl_igrice:
        row=row.lower()
        igrica=row.split(';')
        igrica[4]=igrica[4].split()
        igrica[4]=list(filter(fil_zanr,igrica[4]))
        lista_igara.append(igrica)
    fil_igrice=filter(pravila,igrice)
    print(list(fil_igrice))
    lista_atributa=['ime','ocjena','god','izdavac','zanr']
    lista_dict=[]
    for igra in lista_igara:
        igra_dict=dict(zip(lista_atributa,igra))
        lista_dict.append(igra_dict)
    return lista_dict
novo=kreiraj_dict()
def filtriraj_po_imenu(lista_dictionary,val):
    d=[]
    for dictionary in lista_dictionary: 
            d.append(dictionary)
    return d
def filtriraj_po_izdavacu(lista_dictionary,val):
    d=[]
    for dictionary in lista_dictionary: 
        if dictionary['izdavac'].startswith(val):
            d.append(dictionary)
    return d
def filtriraj_po_ocjeni(lista_dictionary,val):
    d=[]
    try:
        val=float(val)
        if 1>val>10:
            print("Unesite ispravno vrijednost.")
        else:
            for dictionary in lista_dictionary: 
                if float(dictionary['ocjena'])>val:
                    d.append(dictionary)
        return d
    except ValueError:
        print("Pogresan tip podatka!")
def filtriraj_po_godini(lista_dictionary,znak,val):
    d=[]
    if znak=='>':
        for dictionary in lista_dictionary:        
            if int(dictionary['god'])>val:
                d.append(dictionary)
    elif znak=='<':
        for dictionary in lista_dictionary:        
            if int(dictionary['god'])<val:
                d.append(dictionary)
    else:
        print("Greška!")
    return d

#print(filtriraj_po_imenu(novo,'M'))
#print(filtriraj_po_izdavacu(novo,'l'))
#print(filtriraj_po_ocjeni(novo,9))
#print(filtriraj_po_ocjeni(novo,3))
print(filtriraj_po_godini(novo,'>',2007))
