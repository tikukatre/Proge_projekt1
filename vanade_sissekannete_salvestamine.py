import datetime
def summa(a, b):
    f=open("summa.txt", "w+")
    
    uf=open("sissekanded.txt", "a+")
    
    try:
        f.write(a + ";" + (b))
        print("Salvestatud")
    except:
        print("Ebaõnnestus")
    f.close()
    f=open("summa.txt", "r")
    try:
        andmed=f.readline()
        uf.write(andmed +"\n")
        uf.close()
    except:
        pass
        
def kulud_tulud(a,b,c):
    f=open("summa.txt", "r")
    for i in f:
        n=i.split(";")
        kj=int(n[0]) #kontojääk

    kj+=a

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




    




