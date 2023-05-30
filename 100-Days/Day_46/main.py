from bs4 import BeautifulSoup
import requests


BILLBOARD_ADDRESS = "https://www.billboard.com/charts/hot-100/2003-01-20"


response = requests.get(BILLBOARD_ADDRESS) 

soup = BeautifulSoup(response.text, "html.parser")
select_song = soup.select("li ul li h3")
song_list=[]
for each_song in select_song:
    song_list.append(each_song.text.strip())
print(song_list)
