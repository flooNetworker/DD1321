import matplotlib.pyplot as plt
from song_L import music
from DictHash import DictHash
import timeit
import sys
import random


from d4_fuctions import mergesort
from d4_fuctions import quicksort
from d4_fuctions import heapsort


d = DictHash()


def readfile(filename, size):
    list_of_songs = []

    # Läs in låtarna från filen, skapa ett objekt för varje rad och spara objekten både
    # open file and read line for line
    with open(filename, 'r') as r:
        line = r.readline()
        if line == "":
            print("List is empty")
            sys.exit()

        lines = 0
        while lines < size:
            line = line.strip()  # take away white space
            word = line.split('\t')
            artist = word[1]
            song = word[2]
            length = word[3]

            m = music(artist, song, length)

            list_of_songs.append(m)
            d.store(m.artist, m.song)

            line = r.readline()
            lines += 1

        return list_of_songs


def sorting(songlist, key):  # från föreläsningarr

    # ("1: Mergesort \n 2:Quicksort \n 3:Heapsort \n")

    mergesort_list = mergesort(songlist)  # min to max
    quicksort_list = quicksort(
        songlist, 0, len(songlist)-1)  # min to max
    heapsort_list = heapsort(songlist)  # max out first

    choice = {'1': mergesort_list, '2': quicksort_list, '3': heapsort_list}

    return choice[key]


def lin_remove(songlist):

    if len(songlist) > 1:
        x = sorting(songlist, '1')
        longest = x[len(x)-1]

        if linsok(songlist, longest.length):
            # print(longest.length, "longest song found, remove the song")
            songlist.remove(longest)
            return songlist


def linsok(songlist, key):

    for element in songlist:
        length = element.length

        if length == key:
            return True

    return False


def test_sort(songlist):

    ms = sorting(songlist, '1')
    qs = sorting(songlist, '2')
    hs = sorting(songlist, '3')

    key = songlist[len(songlist)-1]

    time1 = timeit.timeit(stmt=lambda: linsok(
        ms, key), number=100)
    print("\n The average linear search in MERGESORTED list took",
          round(time1, 4), "seconds\n The time complexitity is O(n)")

    time2 = timeit.timeit(stmt=lambda: linsok(
        qs, key), number=100)
    print("\n The average linear search in QUICKSORTED list took",
          round(time2, 4), "seconds\n The time complexitity is O(n)")

    time3 = timeit.timeit(stmt=lambda: linsok(
        hs, key), number=100)
    print("\n The average linear search in HEAPSORTED list took",
          round(time3, 4), "seconds\n The time complexitity is O(n)")
#--------------------------_#
# MAIN


def method1(songlist, k):
    # Metod 1 – upprepade linjärsökningar
    i = 0
    ny = songlist
    for i in range(k-1):
        if len(ny) > 1:
            ny = lin_remove(ny)

        lin_remove(ny)
        i += 1

    if len(ny) > 1:
        x = sorting(ny, '1')
        longest = x[len(x)-1]
        return longest


def method2(songlist, k):
    # Metod 2 – sortera och plocka ut
    if len(songlist) > 1:

        x = sorting(songlist, '2')

        return x[k-1]


def main():

    filename = "sang_artist_data.txt"
    number = 100
    list_of_songs = readfile(filename, number)

    print("Number of elements in dictionary =", d.size)
    print("Number of elements in array =", len(list_of_songs))
    test_sort(list_of_songs)
    print("\n")

    k = 1

    x = []
    y = []
    ken = []

    while k <= 30:
        time_1 = timeit.timeit(
            stmt=lambda: method1(list_of_songs, k), number=1)
        time_2 = timeit.timeit(
            stmt=lambda: method2(list_of_songs, k), number=1)

        print(k, time_1, time_2)
        ken.append(k)
        x.append(time_1)
        y.append(time_2)

        k += 4

    plt.xlabel('List Length')  # HÄR!!!!
    plt.ylabel('Time Complexity')
    plt.plot(ken, x, label="Method 1")
    plt.plot(ken, y, label="Method 2")
    plt.grid()
    plt.legend()
    plt.show()


main()
