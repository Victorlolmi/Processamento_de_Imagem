import youtube_dl
import os.path


def download_youtube_video(youtube_url, video_filename):

  youtube_url = youtube_url.strip()
  ydl_opts = {'outtmpl': video_filename}
  with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download([youtube_url])


youtube_url = "https://www.youtube.com/watch?v=tk_vtnRw33M"
video_filename = "Cade_a_chave.mp4"

if os.path.isfile(video_filename) == False:
  download_youtube_video(youtube_url, video_filename)

