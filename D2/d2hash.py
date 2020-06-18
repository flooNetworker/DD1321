from HashNode import HashNode
from HashNode import HashTable


table = HashTable()

# open file and read line for line
with open("unique_tracks.txt", 'r') as r:
    line = r.readline()
    while line:
        line = line.strip()  # take away white space
        word = line.split('<SEP>')
        artist = word[2]
        song = word[3]

        table.store(artist, song)

        line = r.readline()


# SEARCH
x = "Yerba Brava"
print("The artist =", x, "has the song/songs =", table.search(x))


#table.search("Post malone")
