import PySimpleGUI as sg

sg.theme('DarkGrey')

def telaInicial():
    layout = [
        [sg.Text('Por favor digite a URL do vídeo que deseja baixar:')],
        [sg.Text('URL:'), sg.Input(key='url')],
        [sg.Button('Baixar')],
    ]

    janela = sg.Window('Youtube Downloader', layout=layout)

    while True:
        eventos, valores = janela.read()
        
        if eventos == sg.WIN_CLOSED:
            break
        if eventos == 'Baixar':
            url = valores['url']
            print(url)

