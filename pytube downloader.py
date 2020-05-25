from pytube import YouTube
import urllib3
http = urllib3.PoolManager()
#input string as url
urlstring = str(input())
r = http.request('GET', urlstring)
yt = YouTube(r)
print(yt.title)