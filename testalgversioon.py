import datetime
def summa(a, b):
    f = open("summa.txt", "w+")
    
    uf = open("sissekanded.txt", "a+")
    
    try:
        f.write(a + ";" + (b))
        print("Salvestatud")
    except:
        print("Ebaõnnestus")
    f.close()
    f = open("summa.txt", "r")
    
    try:  #kirjutab andmed teise faili säilitamiseks
        andmed = f.readline()
        uf.write(andmed +"\n")
        uf.close()
    except:
        pass
    
def kulud_tulud(a):
    f = open("summa.txt", "r")
    try:
        for i in f:
            n = i.split(";")
            kj = int(n[0]) #kontojääk
        kj += a
        return kj
    except:
        return("Fail on tühi")
    
def kuupäev(k):
    import datetime
    while True: #kuupäev
        päev,kuu,aasta = k.split('.')
        try :
            datetime.datetime(int(aasta),int(kuu),int(päev))
            return(k)
        except ValueError :
            k = input("Kuupäev ei ole sobiv. Sisestage kuupäev formaadis pp.kk.aa: ")
            k = kuupäev(k)
            return(k)
def tagasta_jääk(a):
    f = open(a, "r")
    for i in f:
        summa_kp = i.strip().split(";")
        return summa_kp[0]
        

while True:
    valik = (input("Vali tegevus: (U)us kontojääk, (S)isesta tulud/kulud, (T)agasta kontojääk, (K)ustuta sissekanded, (L)õpeta: "))
    valik = valik.upper()
    if valik == "U":#täiesti uue kontojäägi sisestamine faili
        s = input("Sisestage uus kontojääk: ")
        k = (kuupäev(input("Sisestage kuupäev formaadis pp.kk.aa: ")))
        summa(s,k)
        continue
    if valik == "S":#tulude ja kulude sisestamine ja arvestamine olemasolevast kontojäägist
        kt = int(input("Sisestage kulud/tulud: "))
        uus_summa = str(kulud_tulud(kt))
        if uus_summa == "Fail on tühi":
            print("Fail on tühi. Sisestage uus kontojääk")
            pass
        else:
            k = kuupäev(input("Sisestage kuupäev formaadis pp.kk.aa: "))
            summa(uus_summa,k) #uus summa ja kuupäev
    if valik == "T":#tagastab kontojäägi
        print(tagasta_jääk("summa.txt"))
    if valik == "K": #Kustutab kõik olemasolevad sissekanded
        while True:
            kinnitus = input("Kas olete kindel, et soovite kustutada kõik sissekanded? (J)ah (E)i: ")
            kinnitus = kinnitus.upper()
            if kinnitus == "J":
                open("sissekanded.txt", "w").close()
                open("summa.txt", "w").close()
                break
            else:
                break
    if valik == "L":#lõpeta 
        break