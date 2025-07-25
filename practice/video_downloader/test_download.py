from pytubefix import YouTube
from pytubefix.cli import on_progress
url = "https://www.youtube.com/watch?v=NfmHGoY8AcU&list=RDNfmHGoY8AcU&start_radio=1&ab_channel=AlemdarMusic"
yt = YouTube(url, on_progress_callback=on_progress)
ys = yt.streams.get_highest_resolution()
ys.download()