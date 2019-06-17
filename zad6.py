berza = 'GOOG 300 542.0 B,OGG 20 580.1 d'
sell=0
buy=0
akcija=berza.split(",")
for i in akcija:
    jedna=i.split()
    if jedna[3]=="B":
        buy+=float(jedna[1])*float(jedna[2])
    elif jedna[3]=="S":
        sell+=float(jedna[1])*float(jedna[2])
    else:
        print("Unesite ispravan podatak S ili B")

print("Bay: ",'%.2f'%buy)
print("Sell: ",'%.2f'%sell)
