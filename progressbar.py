import pytube
from pytube import YouTube
from colorama import Fore, Back, Style
import time
from tqdm import tqdm
print(Fore.RED + "Youtube Video downloader is create by Siddharth Rangnani")
a=input("enter video url\n")
ytd = pytube.YouTube(a)
print(ytd.title,"\n")
print(ytd.author,"\n")
print("1 = 720p\n","2 = 360p\n","3 = Download as audio only(recommended for music)\n")
n=int(input("enter the quality"))
if n == 1 :
    print("your video is 720p")
    stream = ytd.streams.get_by_itag("22")
    finished = stream.download()
elif n == 2 :
    print("your video is 480p")
    stream = ytd.streams.get_by_itag("18")
    finished = stream.download()
elif n == 3 :
    print("You are Downloading a Audio File")
    stream = ytd.streams.get_by_itag("251")
    finished = stream.download()
else :
    print("Sorry! Download unable to complete")
for load in tqdm(finished):
    time.sleep(0.1)


print('Download is complete')