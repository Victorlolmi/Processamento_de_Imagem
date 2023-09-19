from pytube import YouTube
from pytube import Playlist
import moviepy.editor as mp
import re
import os

def download_video():
    link = 'https://www.youtube.com/watch?v=vLgPDS5vn2g'
    path = 'D:\Desktop\Documents\GitHub\Processamento_de_Imagem\ReconhecimentoFacial\download'
    yt = YouTube(link)
    #Fazer o dowload
    yt = yt.streams.filter(only_audio=True).first().download(path)
    print("Download Completo")

download_video()