class Song:
    count = 0
    genres = []
    artists = []
    genre_count = {}
    artist_count = {}
    def __init__(self,name, artist, genre):
        self.add_song_to_count()
        self.add_to_genres(genre)
        self.add_to_artists(artist)
        self.add_to_genre_count(genre)
        self.add_to_artist_count(artist)
        self.name = name
        self.artist = artist
        self.genre = genre

    @classmethod
    def add_song_to_count(cls):
        cls.count += 1
        # this is keeping count of how many songs have been created

    @classmethod
    def add_to_genres(cls,genre):
        if genre != cls.genres:
            cls.genres.append(genre)
            # if the genre thats typed in isnt already on the genres list add that genre to the list  

    @classmethod
    def add_to_artists(cls,artist):
        if artist != cls.artists:
            cls.artists.append(artist)
            # if the artis isnt already on the artists list the add that artis onto the list

    @classmethod
    def add_to_genre_count(cls, genre):
        if cls.genre_count.get(genre):
                  cls.genre_count[genre] += 1
        else:
             cls.genre_count[genre] = 1
            #  genre_count is the name of our dict and its keys are the diffrent genres when the .get() is called 
            # its saying to go to the specific key and add all the songs in that genre key and return to us how many songs are in the gerne
            # genre_count={
            #   "rap": ["song1", "song2", "song3"] => 3
            #   r&b: ["song1", "song2"] => 2
            #   "country": ["song1"] => 1
            # }
            # all keys(genre) have atleast one song or else the genre wouldnt be on the dict because the genre wouldnt exict
            # 

    @classmethod
    def add_to_artist_count(cls,artist):
        if cls.artist_count.get(artist):
              cls.artist_count[artist] += 1
        else:
             cls.artist_count[artist] = 1  
              #  artist_count is the name of our dict and its keys are the diffrent artists when the .get() is called 
            # its saying to go to the specific key and add all the songs in that artist key and return to us how many songs they have
            # artist_count={
            #   "Beyonce": ["song1", "song2", "song3"] => 3
            #   "Rihanna": ["song1", "song2"] => 2
            #   "Lil Wayne": ["song1"] => 1
            # }
            # all keys(artist) have atleast one song or else the artist wouldnt be on the dict because the artist wouldnt exict
            #       