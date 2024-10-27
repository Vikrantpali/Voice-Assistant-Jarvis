music = {
    "Illuminati" : "https://youtu.be/tOM-nWPcR4U?si=iGSKyR1o33CQqSFC",
    "AkhiyaanGulaab" : "https://www.youtube.com/watch?v=GvXDq-P1NB8",
    "wolf" : "https://www.youtube.com/watch?v=ThCH0U6aJpU&list=PLnrGi_-oOR6wm0Vi-1OsiLiV5ePSPs9oF&index=21",
    "Skyfall" : "https://www.youtube.com/watch?v=DeumyOzKqgI&pp=ygUHc2t5ZmFsbA%3D%3D"
}

def get_song_link(song_name):
    """Retrieve the URL for a given song name."""
    if song_name in music:
        return music[song_name]
    else:
        raise KeyError(f"Song '{song_name}' not found in the music library.")