import requests
from bs4 import BeautifulSoup
import youtube_dl

"""All the cool stuff happens here
"""
# constant  stuff
YOUTUBE_SEARCH_BASE = "https://www.youtube.com/results?search_query="
BASE_URL = "https://youtube.com/"
codec = 'm4a'

# Options for youtube dl
ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': codec,    # might input in commandline if mp3 demanded
        }],                             # m4a is pretty dope
    }


def scrape_spotify(url):
    """Get the search term for youtube search to extract the 
    videoID and download the song using youtube-dl
    """
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # get the track count
    song_count = int(soup.find('meta', property="music:song_count")["content"])

    # get the playlist name
    pl_name = soup.find('meta', property="og:title")["content"]

    # track name
    track_name = [i.get_text() for i in soup.find_all('span', class_="track-name")]

    # artists + album 
    artists_album = [" ".join((x.get_text()).replace("•",",").split()) \
                    for x in soup.find_all('span', class_="artists-albums")]

    # combine the lists track_name + artists_album 
    track_artists_album = list(map(lambda x, y: x+" "+y, track_name, artists_album))

    return song_count, pl_name, track_artists_album
    


def get_youtube_url(search_term):
    """Returns a videoID for the search term.
    One search is done at a time and results are returned.
    """
    # get the search results
    res = str(requests.get(YOUTUBE_SEARCH_BASE + search_term).content)
    
    videoID = None
    # extract the yummy stuff from the soup
    try:
        videoID = res[res.find("/watch?v="):res.find("/watch?v=")+20]
    except Exception:
        videoID = None
    # don't know what to catch here, i just think it will be easier to get none
    # rather than something unexpected

    return videoID




def download_audio(videoID):
    """
    will download the audio with hardcoded options
    """
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
# just a remider can also be provided with a list of links 
        ydl.download([BASE_URL+videoID])
