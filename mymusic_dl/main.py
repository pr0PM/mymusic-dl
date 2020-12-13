from sys import argv as cliArgs

from mymusic_dl.functions import scrape_spotify
from mymusic_dl.functions import get_youtube_url
from mymusic_dl.functions import download_audio

"""This block of code verifies the user input before proceeding further.
"""

guide = """
To download a playlist, try
 $ mymusic_dl https://open.spitify.com/playlist/18EuC3nWTRg10DD35jfZkk

To search a song and download the first result from youtube, try
 $ mymusic_dl -s "ncs top 10"
"""

error = """
=_= Check the link and try again
"""

# For colorful output in the terminal rather than colorama or term...
# why bloat? right
def prRed(skk): 
    print("\033[91m{}\033[00m" .format(skk))

def prGreen(skk): 
    print("\033[92m{}\033[00m" .format(skk)) 



def input_validator(cliArgs):
    """Checks the commandline inputs while presenting the usage + error messages
    in colorful manner.
    """
    if len(cliArgs) < 2:
        prRed("no/invalid input")
        prGreen(guide)
        return 0

#    if not "open.spotify.com" in cliArgs[1] or not "https://" in cliArgs[1]:
#        prRed(error)
#        prGreen(guide)
#        return 0

    if "playlist" in cliArgs[1]:
        prGreen("^_^ playlist link detected...\n    continuing to web scraping...")
        return 1
    elif cliArgs[1] == "-s":
        prGreen("^_^ proceeding to search youtube...\n")
        return 2
    elif "track" in cliArgs[1] or "album" in cliArgs[1]:
        prGreen("\n^_^ Support for tracks and albums Coming Soon! Your " + chr(127775) 
+ "'s on GitHub will motivate me to ship updates faster :)\n")
        return 0
    else: 
        prRed(error)
        prGreen(guide)
        return 0



"""This block is the entrypoint of the program
"""

def mymusic_dl():
    return_val = input_validator(cliArgs)
    
    if(return_val):
        if(return_val == 1):
            url = cliArgs[1]
            # remove the excessive parts from the link
            if "?si=" in url:
                url = url[:url.index("?si=")]

            song_count, pl_name, track_artists_album = scrape_spotify(url)

            # might replace all this with log later
            prGreen("Info")
            prGreen("Playlist name: {0}\nSong Count: {1}\n" .format(pl_name, song_count))
            prGreen("Getting video id from youtube...")

            # search the strings on yotube and store the videoID
            videoID_list = [ get_youtube_url(query) for query in track_artists_album ]

            if None in videoID_list:
                prRed("Something went wrong")
            else:
                prGreen("Here is the list of videoIDs")
                for i in videoID_list:
                    print(i)

            prRed("Starting Downloads . . .")

            for videoID in videoID_list:
                
                # trying error handling here
                try: 
                    download_audio(videoID)
                    prGreen("Download +1 done")
                except Exception: # ya ik it's bad and stuff
                    pass
        
        elif(return_val == 2):
            query = cliArgs[2]
            # get url
            vid_id = get_youtube_url(query)
            # start download retry 3 times if failed
            c = 3
            while c:
                try:
                    download_audio(vid_id)
                    prGreen("Done :)")
                except Exception as e:
                    print(e, "\n Due to error will try", c-1, "times more")
                    c -= 1
                break



if __name__ == '__main__':
    mymusic_dl()
