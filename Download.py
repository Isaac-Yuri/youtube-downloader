from pytube import YouTube

def download(url, mp4=True, mp3=False):
    yt = YouTube(url,)
    
    if mp4:
        return yt.streams.get_by_resolution('720p').download()
    elif mp3:
        return yt.streams.get_audio_only("mp4").download()
    elif mp4 and mp3:
        downloadMp4 = yt.streams.get_by_resolution('720p').download()
        downloadMp3 = yt.streams.get_audio_only("mp4").download()
        return downloadMp4, downloadMp3