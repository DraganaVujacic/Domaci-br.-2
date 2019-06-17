def html_izdvoj(html_fajl,tag):
    tag='</'+tag+'>'
    broj_ponavljanja=html_fajl.count(tag)
    x=0
    izdvajanje=[]
    while x < broj_ponavljanja:
        privremeno=html_fajl.partition(tag)[0]#dijelim string na 3 niza
        izdvajanje.append(privremeno[privremeno.rfind('>')+1:])
        html_fajl=html_fajl.partition(tag)[2]
        x+=1
    return izdvajanje

print(html_izdvoj('<h1 fkfkf>AAAAA</h1><h2>BBBBBBB</h2>fffff<h2 djdjdd>OOOOOOOOOOOO</h2>','h2'))


