from DictHash import DictHash


# create instance of my class DictHash
h = DictHash()

# open file and read line for line
with open("unique_tracks.txt", 'r') as r:
    line = r.readline()
    while line:
        line = line.strip()  # take away white space
        word = line.split('<SEP>')
        artist = word[2]
        song = word[3]

        h.store(artist, song)

        line = r.readline()


#x = input("What artist do you like to search for ")
x = "Yerba Brava"
print("The artist ", x, "has the song/songs =", h[x])


# print(h.artists_and_songs)
# print("klar")

