import PySimpleGUI as sg
import datetime
import os

#Funktsioonid

def summa(a, b):
    f = open("summa.txt", "w+")
    
    uf = open("sissekanded.txt", "a+")
    
    try:
        f.write(a + ";" + (b))
        print("Salvestatud")
    except:
        print("Ebaõnnestus")
    f.close()
    f = open("summa.txt", "r")
    
    try:  #kirjutab andmed teise faili säilitamiseks
        andmed = f.readline()
        uf.write(andmed +"\n")
        uf.close()
    except:
        pass
    
def kulud_tulud(a):
    f = open("summa.txt", "r")
    try:
        for i in f:
            n = i.split(";")
            kj = int(n[0]) #kontojääk
        kj += a
        return kj
    except:
        return("Fail on tühi")
    
def kuupäev(k):
    import datetime
    while True: #kuupäev
        päev,kuu,aasta = k.split('.')
        try :
            datetime.datetime(int(aasta),int(kuu),int(päev))
            return(k)
        except ValueError :
            sg.Popup("Kuupäev ei ole sobiv. Sisestage kuupäev formaadis pp.kk.aa")
#            k = input("Kuupäev ei ole sobiv. Sisestage kuupäev formaadis pp.kk.aa: ")
#            k = kuupäev(k)
            return(k)
def tagasta_jääk(a):
    f = open(a, "r")
    if os.stat(a).st_size == 0:
        return("Konto on tühi")
    for i in f:
        summa_kp = i.strip().split(";")
        return summa_kp[0]

        
    
#GUI
    
sg.change_look_and_feel("Reddit")
layout=[[sg.Text("Valige tegevus.")],
        [sg.Button("Uus kontojääk")],
        [sg.Button("Tulude/ kulude sisetamine")],
        [sg.Button("Tagasta kontojääk")],
        [sg.Button("Kustuta sissekanded")],
        [sg.Button("Lõpeta")]]
win1=sg.Window("Window 1").Layout(layout)
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
                 [sg.Text("Summa"), sg.InputText()],
                 [sg.Text("Sisestage kuupäev formaadis pp.kk.aa: "), sg.InputText()],
                  [sg.Button("Salvesta"), sg.Button("Lõpeta")]]
        win2=sg.Window("Window 2").Layout(layout2)
        while True:
            event2,value2=win2.Read()
            if event2 is None or event2==("Lõpeta"):
                win2_active=False
                win2.Close()
                win1.UnHide()
                break
            if event2==("Salvesta"):
                try:
                    k=kuupäev(value2[1])
                    summa(value2[0],k)
                    sg.Popup("Edukalt salvestatud")
                except:
                    sg.Popup("Midagi läks valesti")
         
    if not win2_active and event=="Tulude/ kulude sisetamine":
        win1.Hide()
        win2_active=True
        layout3=[[sg.Text("Tulude/ kulude sisetamine"), sg.InputText()],
                  [sg.Button("Lõpeta")]]
        win3=sg.Window("Window 3").Layout(layout3)
        while True:
            event2,value2=win3.Read()
            if event2 is None or event2==("Lõpeta"):
                win2_active=False
                win3.Close()
                win1.UnHide()
                break
            
    if not win2_active and event=="Tagasta kontojääk":
        win1.Hide()
        win2_active=True
        layout4=[[sg.Text("Teie kontojääk:"), sg.Text((tagasta_jääk("summa.txt")))],
                  [sg.Button("Lõpeta")]]
        win4=sg.Window("Window 4").Layout(layout4)
        while True:
            event2,value2=win4.Read()
            if event2 is None or event2==("Lõpeta"):
                win2_active=False
                win4.Close()
                win1.UnHide()
                break
    if not win2_active and event=="Kustuta sissekanded":
        win1.Hide()
        win2_active=True
        layout5=[[sg.Text("Kas olete kindel, et soovite kustutada kõik sissekanded?")],
                 [sg.Button("Jah"), sg.Button("Ei")]]
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

        
##        sg.change_look_and_feel('Reddit')
#        form2 = sg.FlexForm("Uus kontojääk")
#        layout2=[[sg.Text("Uus kontojääk")],
#                [sg.Text("Sisestage uus kontojääk"), sg.InputText()],
#                [sg.Text("Sisestage kuupäev formaadis pp.kk.aa"), sg.InputText()]
#                 ]
#        window2=sg.Window("Window 2", layout)

#layout = [
#          [sg.Text('Palun sisesta oma selle kuu andmed.')],
#          [sg.Text('Tulud'), sg.InputText()],
#          [sg.Text('Kulud'), sg.InputText()],
#          [sg.Text('Kuupäev'), sg.InputText()],
#          [sg.Submit(), sg.Cancel()]
#         ]
#
#window = sg.Window('Window Title', layout)
#
#while True:
#    event, values = window.read()
#    if event in (None, 'Cancel'):
#        break
#    if values[2]
#    print(values[0], values[1], values[2])
#    
#window.close()
#
#layout =[[sg.Text("Teie tulud:" + values[0])]]