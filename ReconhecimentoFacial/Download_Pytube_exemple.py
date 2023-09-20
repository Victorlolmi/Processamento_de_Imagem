import subprocess

url = "https://www.youtube.com/watch?v=rKnt7bBQf_Y"
#
subprocess.run(["youtube-dlc", url])