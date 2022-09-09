# Python Code to Download YouTube PlayList Videos

# Importing Required Modules
from pytube import Playlist

# To Download YouTube PlayList Videos
play_list = Playlist("Play List URL")

# To Check PlayList Title
print("Play List Title: ", play_list.title)

# For Loop to Download All Videos
for video in play_list.videos:
    # To Check Video Title
    print(video.title)
    # To Download Video
    video.streams.get_highest_resolution().download()
