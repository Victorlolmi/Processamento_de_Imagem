import subprocess

url = "https://www.youtube.com/watch?v=vLgPDS5vn2g"

subprocess.run(["youtube-dlc", url])