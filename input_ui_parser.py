from sys import argv as cliArgs
from spoti_yt import scrape_spotify
from spoti_yt import get_youtube_url

"""This module verifies the user input before proceeding further saving time.
"""

guide = """
To download a Playlist
sdl https://open.spotify.com/<continues>

eg: 
    sdl https://open.spitify.com/playlist/18EuC3nWTRg10DD35jfZkk
"""

error = """
=_= Check the link and try again
"""

# For colorful output in the terminal rather than colorama or term...

def prRed(skk): 
    print("\033[91m{}\033[00m" .format(skk))

def prGreen(skk): 
    print("\033[92m{}\033[00m" .format(skk)) 


def input_validator(cliArgs):
    """Checks the commandline inputs while presenting the usage + error messages
    in colorful manner.
    """
    if not "open.spotify.com" in cliArgs[1] or not "https://" in cliArgs[1]:
        prRed(error)
        prGreen(guide)
        return 0

    if "playlist" in cliArgs[1]:
        prGreen("^_^ playlist link detected...\n    continuing to web scraping...")
        return 1

    elif "track" in cliArgs[1] or "album" in cliArgs[1]:
        prGreen("\n^_^ Support for tracks and albums Coming Soon! Your " + chr(127775) 
+ "'s on GitHub will motivate me complete it faster :)\n")

        return 0

    else: 
        prRed(error)
        prGreen(guide)
        return 0





if(input_validator(cliArgs)):
    url = cliArgs[1]
    url = url[:url.index("?si=")]

    song_count, pl_name, track_artists_album = scrape_spotify(url)

    # might replace all this with log later
    prGreen("Info")
    prGreen("Playlist name: {0}\nSong Count: {1}\n" .format(pl_name, song_count))
    prGreen("Getting video id from youtube...")

    # search the strings on yotube and store the videoID
    for query in track_artists_album:
        videoID_list = get_youtube_url(query)


