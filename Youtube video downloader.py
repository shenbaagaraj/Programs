from pytube import YouTube
link = ("https://youtu.be/stNrkLiMYuw")
video = YouTube(link)
stream = video.streams.get_highest_resolution()
stream.download()