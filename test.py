import datetime
def summa(a, b):
    f=open("summa.txt", "w+")
    try:
        f.write(a + ";" + b)
#        f.close()
        print("Salvestatud")
    except:
        print("Ebaõnnestus")
    f.close()
def kulud_tulud(a):
    f=open("summa.txt", "r")
    for i in f:
        n=i.split(";")
        kj=int(n[0]) #kontojääk
    kj+=a
    return kj
#s=input("Sisestage summa: ")

#while True:
#    kuupäev = input("Sisestage kuupäev formaadis pp.kk.aa:")
#    päev,kuu,aasta = kuupäev.split('.')
#    isValidDate = True
#    try :
#        datetime.datetime(int(aasta),int(kuu),int(päev))
#        break
#    except ValueError :
#        isValidDate = False
#        print ("Kuupäev ei ole sobiv..")
kt=int(input("Sisestage kulud/tulud: "))
print(kulud_tulud(kt))
#summa(s,kuupäev)



    


