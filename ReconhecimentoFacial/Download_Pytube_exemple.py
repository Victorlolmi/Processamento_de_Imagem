import subprocess

url = "https://www.youtube.com/watch?v=rBjHYJUrBOg"
#
subprocess.run(["yt-dlp", url])