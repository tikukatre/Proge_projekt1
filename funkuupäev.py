#k = input("Sisestage kuupäev formaadis pp.kk.aa: ")
def kuupäev(k):
    import datetime
    while True: #kuupäev
        päev,kuu,aasta = k.split('.')
        try :
            datetime.datetime(int(aasta),int(kuu),int(päev))
            
            return(k)
        except ValueError :
            k=input("Kuupäev ei ole sobiv. Sisestage kuupäev formaadis pp.kk.aa: ")
            k=kuupäev(k)
            return(k)

print(kuupäev(input("Sisestage kuupäev formaadis pp.kk.aa: ")))


