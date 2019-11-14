#k = input("Sisestage kuupäev formaadis pp.kk.aa: ")
def kuupäev(k):
    import datetime
    while True: #kuupäev
        päev,kuu,aasta = k.split('.')
        try :
            datetime.datetime(int(aasta),int(kuu),int(päev))
            break
        except ValueError :
            print("Kuupäev ei ole sobiv.")
            break

kuupäev(input("Sisestage kuupäev formaadis pp.kk.aa: "))


