import PySimpleGUI as sg
import datetime
import os

#Funktsioonid

def summa(a, b):
    f = open("summa.txt", "w+")
    
    uf = open("sissekanded.txt", "a+")
    try:
        a=int(a)
        try:
            f.write(str(a) + ";" + (b))
            sg.Popup("Salvestatud")
        except:
            sg.Popup("Ebaõnnestus")
        f.close()
        f = open("summa.txt", "r")
        
        try:  #kirjutab andmed teise faili säilitamiseks
            andmed = f.readline()
            uf.write(andmed +"\n")
            uf.close()
        except:
            pass
    except ValueError:
        a=sg.PopupGetText("Palun sisestage kontojääk arvuna.","")
        summa(a,b)


    
def kulud_tulud(a):
    f = open("summa.txt", "r")
    try:
        for i in f:
            n = i.split(";")
            kj = int(n[0]) 
        kj += a
        return kj
    except:
        return("Fail on tühi")
    
def kuupäev(k):
    try :
        päev,kuu,aasta = k.split('.')
        datetime.datetime(int(aasta),int(kuu),int(päev))
        print(k)
        return(k)
    except ValueError:
        k=sg.PopupGetText("Kuupäev ei ole sobiv.Sisesta kuupäev vormis pp.kk.aa", "")
        return(kuupäev(k))

def tagasta_jääk(a):
    f = open(a, "r")
    if os.stat(a).st_size == 0:
        return("Konto on tühi")
    for i in f:
        summa_kp = i.strip().split(";")
        return summa_kp[0]
    
def otsi(kp):
    f =open("sissekanded.txt", "r")
    for i in f:
        if kp in i:
            i=i.strip().split(";")
            sg.Popup("Teie kontojääk sellel kuupäeval: " +i[0])
            return(i[0])
        else:
            sg.Popup("Antud kuupäeva ei leitud")
            break

           
#GUI
    
sg.change_look_and_feel("LightTeal")
layout=[[sg.Text("Valige tegevus.", size=(50,4))],
        [sg.Button("Uus kontojääk", size=(50,4))],
        [sg.Button("Tulude/ kulude sisetamine", size=(50,4))],
        [sg.Button("Tagasta kontojääk", size=(50,4))],
        [sg.Button("Otsi kuupäeva järgi", size=(50,4))],
        [sg.Button("Kustuta sissekanded", size=(50,4))],
        [sg.Button("Lõpeta", size=(50,4))]]

win1=sg.Window("Rahakalkulaator").Layout(layout)
win2_active=False
while True:

    event, value =win1.Read()
    if event is None or event=="Lõpeta":
        win1.Close()
        break
    
    if not win2_active and event=="Uus kontojääk":
        win1.Hide()
        win2_active=True
        layout2=[[sg.Text("Uus sissekanne")],
                 [sg.Text("Summa", size=(20,2)), sg.InputText()],
                 [sg.Text("Sisestage kuupäev formaadis pp.kk.aa: ", size=(20,2)), sg.InputText()],
                  [sg.Text("",size=(20,1)),sg.Button("Salvesta", size=(15,1)), sg.Button("Tagasi", size=(15,1))]]
        win2=sg.Window("Uus kontojääk").Layout(layout2)
        while True:
            event2,value2=win2.Read()
            if event2 is None or event2==("Tagasi"):
                win2_active=False
                win2.Close()
                win1.UnHide()
                break

            if event2==("Salvesta"):
                k=kuupäev(value2[1])
                summa=summa((value2[0]),k)
                win2_active=False
                win2.Close()
                win1.UnHide()
                break
       
    if not win2_active and event=="Tulude/ kulude sisetamine":
        win1.Hide()
        win2_active=True
        layout3=[[sg.Text("Tulude/ kulude sisetamine", size=(20,2)), sg.InputText()],
                 [sg.Text("Sisestage kuupäev formaadis pp.kk.aa: ", size=(20,2)), sg.InputText()],
                  [sg.Button("Salvesta"),sg.Button("Tagasi")]]
        win3=sg.Window("Tulud ja kulud").Layout(layout3)
        while True:
            event2,value2=win3.Read()
            if event2 is None or event2==("Tagasi"):
                win2_active=False
                win3.Close()
                win1.UnHide()
                break
            if event2=="Salvesta":
                kt=int(value2[0])
                uus_summa = str(kulud_tulud(kt))
                if uus_summa == "Fail on tühi":
                    sg.Popup("Fail on tühi. Sisestage uus kontojääk")
                    pass
                else:
                    kp=kuupäev(value2[1])
                    summa(uus_summa,kp)
                          
    if not win2_active and event=="Tagasta kontojääk":
        win1.Hide()
        win2_active=True
        layout4=[[sg.Text("Teie kontojääk:", size=(20,2)), sg.Text((tagasta_jääk("summa.txt")), size=(20,2))],
                  [sg.Text("", size=(20,2)),sg.Button("Tagasi")]]
        win4=sg.Window("Praegune kontojääk").Layout(layout4)
        while True:
            event2,value2=win4.Read()
            if event2 is None or event2==("Tagasi"):
                win2_active=False
                win4.Close()
                win1.UnHide()
                break
    if not win2_active and event=="Otsi kuupäeva järgi":
        win1.Hide()
        win2_active=True
        layout4=[[sg.Text("Sisetage kuupäev, mille sissekannet soovite näha:", size=(20,2)), sg.InputText()],
                  [sg.Text("", size=(20,2)),sg.Button("Otsi"), sg.Button("Tagasi")]]
        win4=sg.Window("Praegune kontojääk").Layout(layout4)
        while True:
            event2,value2=win4.Read()
            if event2 is None or event2==("Tagasi"):
                win2_active=False
                win4.Close()
                win1.UnHide()
                break
            if event2=="Otsi":
                otsi(value2[0])
                
    if not win2_active and event=="Kustuta sissekanded":
        win1.Hide()
        win2_active=True
        layout5=[[sg.Text("Kas olete kindel, et soovite kustutada kõik sissekanded?")],
                 [sg.Text("", size=(15,1)),sg.Button("Jah", size=(15,1)), sg.Button("Ei", size=(15,1))]]
        win5=sg.Window("Sissekannete kustutamine").Layout(layout5)
        while True:
            event2,value2=win5.Read()
            if event2 is None or event2==("Ei"):
                win2_active=False
                win5.Close()
                win1.UnHide()
                break
            if event2=="Jah":
                try:
                    open("sissekanded.txt", "w").close()
                    open("summa.txt", "w").close()
                    sg.Popup("Edukalt kustutatud")
                    win5.Close()
                    win1.UnHide()
                except:
                    sg.Popup("Midagi läks valesti")
                    win5.Close()
                    win1.UnHide() 

        
