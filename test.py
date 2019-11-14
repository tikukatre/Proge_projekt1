import datetime
def summa(a, b):
    f=open("summa.txt", "w+")
    try:
        f.write(a + ";" + b)
        print("Salvestatud")
    except:
        print("Ebaõnnestus")
    f.close()
    
def kulud_tulud(a):
    f=open("summa.txt", "r")
    try:
        for i in f:
            n=i.split(";")
            kj=int(n[0]) #kontojääk
        kj+=a
        return kj
    except:
        return("Fail on tühi")
    
def kuupäev(k):
    import datetime
    while True: #kuupäev
        päev,kuu,aasta = k.split('.')
        try :
            datetime.datetime(int(aasta),int(kuu),int(päev))
            break
        except ValueError :
#            print("Kuupäev ei ole sobiv.")
            k=input("Kuupäev ei ole sobiv. Sisestage kuupäev formaadis pp.kk.aa: ")
            kuupäev(k)
            break
        
#    return kj
while True:
    valik=(input("Vali tegevus: (T)äiesti uus kontojääk, (S)isesta tulud/kulud, (L)õpeta: "))
    valik=valik.upper()
    if valik=="T":#täiesti uue kontojäägi sisestamine faili
        s=input("Sisestage uus kontojääk: ")
        kuupäev(input("Sisestage kuupäev formaadis pp.kk.aa: "))
        summa(s,str(kuupäev))
        continue
    if valik=="S":
        kt=int(input("Sisestage kulud/tulud: "))
        uus_summa=str(kulud_tulud(kt))
        if uus_summa== "Fail on tühi":
            print("Fail on tühi. Sisestage uus kontojääk")
            pass
        else:
            kuupäev(input("Sisestage kuupäev formaadis pp.kk.aa: "))
            summa(uus_summa,str(kuupäev))
#        summa(uus_summa,kuupäev)
        
    if valik=="L":
        break
          
#kt=int(input("Sisestage kulud/tulud: "))
#summa(s,kuupäev)
#uus_summa=str(kulud_tulud(kt, kuupäev,s))
#summa(uus_summa,kuupäev)




    


