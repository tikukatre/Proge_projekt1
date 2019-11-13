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