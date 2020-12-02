
import pytube
print("Youtube Video downloader is create by UselessVids")
a=input("enter video url\n")
ytd = pytube.YouTube(a)
print(ytd.title,"\n")
print(ytd.author,"\n")
print("You are Downloading a Audio File")
stream = ytd.streams.get_by_itag("22")
finished = stream.download()
for load in (finished):
    time.sleep(0.1)


print('Download is complete')