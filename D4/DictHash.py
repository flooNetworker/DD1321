class DictHash:
    # make dictionary w. key=artist och value=song
    def __init__(self):
        self.artists_and_songs = {}
        self.size = 0
        #self.songs = []

    # store data as value with key, IN=DATA=song
    def store(self, key, data):

        # if key in self.artists_and_songs:
            # self.songs.append(self.artists_and_songs[key])
            # self.songs.append(data)
            # self.artists_and_songs[key] = self.songs

       # else:
        self.artists_and_songs[key] = data
        self.size += 1

    # search for the key in my dictionary
    def search(self, key):
        return self.artists_and_songs[key]

    # to be able to write h[key]
    def __getitem__(self, key):
        return self.search(key)
