import datetime
kuupäev = input("'Sisestage kuupäev formaadis pp/kk/aa':")
päev,kuu,aasta = kuupäev.split('/')
isValidDate = True
try :
    datetime.datetime(int(aasta),int(kuu),int(päev))
except ValueError :
    isValidDate = False
if(isValidDate) :
    print ("Kuupäev on sobiv..")
else :
    print ("Kuupäev ei ole sobiv..")