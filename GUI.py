import PySimpleGUI as sg
sg.change_look_and_feel('Reddit')
# Very basic form.  Return values as a list
form = sg.FlexForm('Simple data entry form')  # begin with a blank form

layout = [
          [sg.Text('Palun sisesta oma selle kuu andmed.')],
          [sg.Text('Tulud'), sg.InputText()],
          [sg.Text('Kulud'), sg.InputText()],
          [sg.Text('Kuupäev'), sg.InputText()],
          [sg.Submit(), sg.Cancel()]
         ]

window = sg.Window('Window Title', layout)
while True:
    event, values = window.read()
    print(values[0], values[1], values[2])
    if event in (None, 'Cancel'):
        break
window.close()

