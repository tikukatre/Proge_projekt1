import PySimpleGUI as sg
import datetime

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
                  [sg.Button("Lõpeta")]]
        win2=sg.Window("Window 2").Layout(layout2)
        while True:
            event2,value2=win2.Read()
            if event2 is None or event2==("Lõpeta"):
                win2_active=False
                win2.Close()
                win1.UnHide()
                break
            
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
        layout4=[[sg.Text("Teie kontojääk:")],
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
        layout5=[[sg.Text("Soovite sissekanded kustutada?")],
                  [sg.Button("Lõpeta")]]
        win5=sg.Window("Window 5").Layout(layout5)
        while True:
            event2,value2=win5.Read()
            if event2 is None or event2==("Lõpeta"):
                win2_active=False
                win5.Close()
                win1.UnHide()
                break

        
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