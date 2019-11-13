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
s=input("Sisestage summa: ")

while True:
    kuupäev = input("Sisestage kuupäev formaadis pp/kk/aa:")
    päev,kuu,aasta = kuupäev.split('/')
    isValidDate = True
    try :
        datetime.datetime(int(aasta),int(kuu),int(päev))
        break
    except ValueError :
        isValidDate = False
        print ("Kuupäev ei ole sobiv..")
summa(s,kuupäev)


    


