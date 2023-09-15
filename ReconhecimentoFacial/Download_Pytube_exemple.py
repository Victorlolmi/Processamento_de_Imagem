from pytube import YouTube

url = "https://www.youtube.com/watch?v=dt7puHrnGbc"

try:
    yt = YouTube(url)
    stream = yt.streams.get_highest_resolution()  # Escolhe a melhor resolução disponível
    print(f"Baixando vídeo: {yt.title}")
    stream.download()
    print("Download concluído!")
except Exception as e:
    print(f"Ocorreu um erro: {str(e)}")