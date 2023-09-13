import youtube_dl

def download_youtube_video(youtube_url, video_filename):

  youtube_url = youtube_url.strip()
  ydl_opts = {'outtmpl': video_filename}

  with youtube_dl.YoutubeDl(ydl_opts) as ydl:
    ydl.download([youtube_url])