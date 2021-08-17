from typing import Text
import PySimpleGUI as sg


sg.theme('DarkGrey')


def telaInicial():
    layout = [
        [sg.Text('Por favor digite a URL do vídeo que deseja baixar:')],
        [sg.Text('URL:'), sg.Input(key='url')],
        [sg.Text('Em qual formato deseja baixar?')],
        [sg.Checkbox('mp4', key='mp4'), sg.Checkbox('mp3', key='mp3')],
        [sg.Button('Baixar')],
        [sg.Output(size=(30, 5),font='Arial',text_color='greenyellow')],
    ]

    janela = sg.Window('Youtube Downloader', layout=layout)

    while True:
        eventos, valores = janela.read()
        
        if eventos == sg.WIN_CLOSED:
            break
        if eventos == 'Baixar':
            mp4, mp3 = valores['mp4'], valores['mp3']
            url = valores['url']
            print(mp3, mp4)
