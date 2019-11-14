import datetime
def summa(a, b):
    f=open("summa.txt", "w+")
    try:
        f.write(a + ";" + b)
        print("Salvestatud")
    except:
        print("Ebaõnnestus")
    f.close()
    
def kulud_tulud(a,b,c):
    f=open("summa.txt", "r")
    for i in f:
        n=i.split(";")
        kj=int(n[0]) #kontojääk

    kj+=a

    return kj
while True:
    valik=(input("Vali tegevus: (T)äiesti uus kontojääk, (S)isesta tulud/kulud, (L)õpeta: "))
    if valik=="T":#täiesti uue kontojäägi sisestamine faili
        s=input("Sisestage uus kontojääk: ")
    
        while True: #kuupäev
            kuupäev = input("Sisestage kuupäev formaadis pp.kk.aa: ")
            päev,kuu,aasta = kuupäev.split('.')
            isValidDate = True
            try :
                datetime.datetime(int(aasta),int(kuu),int(päev))
                break
            except ValueError :
                isValidDate = False
                print ("Kuupäev ei ole sobiv.")
        summa(s,kuupäev)
        continue
    if valik=="S":
        kt=int(input("Sisestage kulud/tulud: "))
        uus_summa=str(kulud_tulud(kt, kuupäev,s))

        
    if valik=="L":
        break
          
#kt=int(input("Sisestage kulud/tulud: "))
#summa(s,kuupäev)
#uus_summa=str(kulud_tulud(kt, kuupäev,s))
#summa(uus_summa,kuupäev)




    


