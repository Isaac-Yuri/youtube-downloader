from pytube import YouTube
from tqdm import tqdm
from time import sleep


def download_yt(url, mp4=True, mp3=False):
    yt = YouTube(url,)

    if mp4:
        return yt.streams.get_by_resolution('720p').download()
    elif mp3:
        return yt.streams.get_audio_only("mp4").download()
    elif mp4 and mp3:
        downloadMp4 = yt.streams.get_by_resolution('720p').download()
        downloadMp3 = yt.streams.get_audio_only("mp4").download()
        return downloadMp4, downloadMp3


def progresso_download():
    for _ in tqdm(range(100), desc="Baixando...", ascii=False, ncols=75,):
        sleep(0.05)
    print('Download concluído!')
