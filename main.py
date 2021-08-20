from Telas import telaInicial, telaDeAviso
from PySimpleGUI import read_all_windows, WIN_CLOSED
from Download import progresso_download, download
from threading import Thread

janela1, janela2 = telaInicial, None

while True:
    janelas, eventos, valores = read_all_windows()
    if eventos == WIN_CLOSED:
        break
    if eventos == 'Baixar':
        url = valores['url']
        if url[:4] != 'http':
            telaDeAviso()
        else:
            Thread(target=progresso_download).start()

            mp4, mp3, mp4emp3 = valores['mp4'], valores['mp3'], valores['mp4emp3']

            if mp4:
                video = download(url=url, mp4=True)
            elif mp3:
                audio = download(url=url, mp4=False, mp3=True)
            elif mp4 and mp3:
                video_audio = download(url=url, mp4=True, mp3=True)
