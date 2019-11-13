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
#    try:
#        kj+=a
#        uus_kontojääk=summa(kj,b)
#        
#    except:
#        summa(c,b)
#        for i in f:
#            n=i.split(";")
#            kj=int(n[0])
    kj+=a
#        uus_kontojääk=summa(kj,b)
#    uus_kontojääk=summa(kj,b)
#    return uus_kontojääk
    return kj

s=input("Sisestage kontojääk: ")

while True: #kuupäev
    kuupäev = input("Sisestage kuupäev formaadis pp.kk.aa:")
    päev,kuu,aasta = kuupäev.split('.')
    isValidDate = True
    try :
        datetime.datetime(int(aasta),int(kuu),int(päev))
        break
    except ValueError :
        isValidDate = False
        print ("Kuupäev ei ole sobiv..")
        
kt=int(input("Sisestage kulud/tulud: "))
summa(s,kuupäev)
uus_summa=str(kulud_tulud(kt, kuupäev,s))
summa(uus_summa,kuupäev)




    


