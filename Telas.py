import PySimpleGUI as sg


def telaInicial():
    sg.theme('DarkGrey')
    layout = [
        [sg.Text('Por favor digite a URL do vídeo que deseja baixar:')],
        [sg.Text('URL:'), sg.Input(key='url')],
        [sg.Text('Em qual formato deseja baixar?')],
        [sg.Radio('mp4', key='mp4', group_id='opcoes_de_download'),
         sg.Radio('mp3', key='mp3', group_id='opcoes_de_download')],
        [sg.Radio('mp4 e mp3', key='mp4emp3', group_id='opcoes_de_download')],
        [sg.Button('Baixar')],
        [sg.Output(size=(40, 5), font='Arial', text_color='greenyellow',)],
    ]

    return sg.Window('Youtube Downloader', layout=layout)


def telaDeAviso():
    sg.theme('DarkBrown4')
    layout = [
        [sg.Text('Por favor adicione um link(URL) do vídeo que deseja baixar')],
        [sg.Button('OK')]
    ]

    return sg.Window('ERRO', layout=layout)


def telaDownloadConcluido():
    pass