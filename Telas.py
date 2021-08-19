import PySimpleGUI as sg
import threading
from time import sleep
from tqdm import tqdm
from Download import download


sg.theme('DarkGrey')


def telaInicial():
    layout = [
        [sg.Text('Por favor digite a URL do vídeo que deseja baixar:')],
        [sg.Text('URL:'), sg.Input(key='url')],
        [sg.Text('Em qual formato deseja baixar?')],
        [sg.Checkbox('mp4', key='mp4'), sg.Checkbox('mp3', key='mp3')],
        [sg.Button('Baixar')],
        [sg.Output(size=(40, 5),font='Arial',text_color='greenyellow',)],
    ]

    janela = sg.Window('Youtube Downloader', layout=layout)

    while True:
        eventos, valores = janela.read()
        
        if eventos == sg.WIN_CLOSED:
            break
        if eventos == 'Baixar':
            url = valores['url']
            if url[:4] != 'http':
                telaDeAviso()
            else:
                def progresso_download():
                    for _ in tqdm(range(100), desc="Baixando...",ascii=False, ncols=75,):
                        sleep(0.05)
                    print('Download concluído!')

                threading.Thread(target=progresso_download).start()
                
                mp4, mp3 = valores['mp4'], valores['mp3']
                

                if mp4:
                    video = download(url=url, mp4=True)
                elif mp3:
                    audio = download(url=url, mp4=False, mp3=True)
                elif mp4 and mp3:
                    video_audio = download(url=url, mp4=True, mp3=True)
                
def telaDeAviso():
    pass