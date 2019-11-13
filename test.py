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

kp=input("Sisestage kuupäev: ")
summa(s,kp)
f=open("summa.txt", "r")
for i in f:
    n=i.split(";")
    kuupäev=n[1]
    print(kuupäev)
#    k=kuupäev.split(".")
#    kup=[] #kuupäevad listi elementidena
#    for j in k:
#        kup.append(j)
#    print(kup)

    


