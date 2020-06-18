import matplotlib.pyplot as plt
from song import music
from DictHash import DictHash
import timeit
import sys
import random

from d4_fuctions import linsok
from d4_fuctions import binsok
from d4_fuctions import testing
from d4_fuctions import mergesort
from d4_fuctions import quicksort
from d4_fuctions import partitionera
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
            word = line.split('<SEP>')
            artist = word[2]
            song = word[3]

            m = music(artist, song)

            list_of_songs.append(m)
            d.store(m.artist, m.song)

            line = r.readline()
            lines += 1

        return list_of_songs


def lin_osorted(songlist):
    # Söker efter nästsista  elementet med linjärsökning i osorterade listor.

    print("\nTesting LINEAR search for an artist in an UNSORTED list:")

    second_last = songlist[len(songlist)-2]
    testsong = music(second_last.artist, second_last.song)
    print("Second to last artist is =", testsong.artist)

    if testing(songlist, testsong):
        linjtid = timeit.timeit(stmt=lambda: linsok(
            songlist, testsong.artist), number=100)
        print("The linear search took", round(linjtid, 4),
              "seconds \n The time complexitity is O(n)")



def lin_sorted(songlist):
    # Söker efter nästsista elementet med linjärsökning i sorterade listor.

    print("\nTesting LINEAR search for an artist in a SORTED list:")

    second_last = songlist[len(songlist)-2]
    testsong = music(second_last.artist, second_last.song)
    print("Second to last artist is =", testsong.artist)

    if testing(songlist, testsong):

        sorted_list = sorting(songlist)
        linjtid = timeit.timeit(stmt=lambda: linsok(
            sorted_list, testsong.artist), number=100)
    print("The linear search took", round(linjtid, 4),
          "seconds \n The time complexitity is O(n)")


def sorting(songlist):  # från föreläsningarr

    #("1: Mergesort \n 2:Quicksort \n 3:Heapsort \n")

    mergesort_list = mergesort(songlist)  # min to max
    quicksort_list = quicksort(
        songlist, 0, len(songlist)-1)  # min to max
    heapsort_list = heapsort(songlist)  # max out first

    choice = {'1': mergesort_list, '2': quicksort_list, '3': heapsort_list}
    return choice['1']


def lin_time(songlist):
    # Söker med linjärsökning efter element i en osorterad lista, redovisa genomsnittssökningen. Sök 1000 olika slumpade element/index och redovisa genomsnittet.

    number = 1000
    index = []
    print("\nTesting LINEAR search for an averagely generated artist in a UNSORTED list over random set of indexes:\n")
    print("Number of random searches = ", number)

    for i in range(number):
        index.append(random.randint(0, len(songlist)))

    index_avg = sum(index)//number
    print("The average search is on index = ", index_avg)

    s = songlist[index_avg]
    t = music(s.artist, s.song)

    avg_time = timeit.timeit(stmt=lambda: linsok(
        songlist, t.artist), number=100)
    print("\n The average linear search in an unsorted list took",
          round(avg_time, 4), "seconds\n The time complexitity is O(n)")

    elements = []
    times = []

    # INDEX = [1000 st random index mellan 0 och len(songlist)] sök efter 1000st random artister

    for i in range(1, 10):
        a = number * i

        search = songlist[index[i]]
        testsong = music(search.artist, search.song)

        linjtid = timeit.timeit(stmt=lambda: linsok(
            songlist, testsong.artist), number=100)
        times.append(linjtid)

        print(a, "Elements was found by linear search in", linjtid)
        elements.append(a)

    # GRAFEN SKA VISA HUR MÅNGA ELEMENT SOM SKA SORTERAS OCH HUR LÅNG TID DET TOG FÖR VARJE SÖKNING, EX) DET TOG 1 SEK ATT SORETERA 100 ELEMENT
    # FÖR DETTA FÖR N ANTAL VARV FÖR ATT FÅ EN KURVA
    # 1000 Elements Sorted by HeapSort in  0.023797415087301488
    # 2000 Elements Sorted by HeapSort in  0.053856713614550245

    return (elements, times)


def bin_time(songlist):
    # Söker med binärsökning i sorterade listor, du kan kopiera binärsökningskoden från bok, nät eller föreläsningsanteckningar.
    number = 1000
    index = []

    print("\nTesting BINARY search for an averagely generated artist in a SORTED list over random set of indexes: \n")
    print("Number of random searches = ", number)

    for i in range(number):
        index.append(random.randint(0, len(songlist)))

    index_avg = sum(index)//number
    print("The average search is on index = ", index_avg)

    s = songlist[index_avg]
    t = music(s.artist, s.song)

    avg_time = timeit.timeit(stmt=lambda: binsok(
        songlist, t.artist), number=100)
    print("\n The average binary search in a sorted list took",
          round(avg_time, 4), "seconds \n The time complexitity is O(log2n)")

    elements = []
    times = []

    for i in range(1, 10):
        a = number * i

        search = songlist[index[i]]
        testsong = music(search.artist, search.song)

        sorted_list = sorting(songlist)

        bintid = timeit.timeit(stmt=lambda: binsok(
            sorted_list, testsong.artist), number=100)
        times.append(bintid)

        print(a, "Elements was found by binary search in", bintid)
        elements.append(a)

    return (elements, times)


def compare_plot(songlist):

    x = lin_time(songlist)
    y = bin_time(songlist)

    plt.xlabel('List Length')  # HÄR!!!!
    plt.ylabel('Time Complexity')
    plt.plot(x[0], x[1], label="Linear search unsorted list")
    plt.plot(y[0], y[1], label="Binary search sorted list")
    plt.grid()
    plt.legend()
    plt.show()


def choice(songlist, key):

    if key == '1':
        lin_osorted(songlist)
    elif key == '2':
        lin_sorted(songlist)
    elif key == '3':
        lin_time(songlist)
    else:
        bin_time(songlist)

#--------------------------_#
# MAIN


def main():

    filename = "unique_tracks.txt"
    number = sys.argv[1]
    list_of_songs = readfile(filename, int(number))

    print("Number of elements in dictionary =", d.size)
    print("Number of elements in array =", len(list_of_songs))
    print("\n")

    key = input(
        "What do you want to do? press corresponding choice:\n 1: Linear search unsorted list \n 2: Linear search sorted list \n 3: Linear search unsorted list for 1000 random elements \n 4: Binary search sorted list for 1000 random elements \n 5: Compare linear and binary plot \n")

    if key == '1' or key == '2' or key == '3' or key == '4':
        choice(list_of_songs, key)
        sys.exit()
    elif key == '5':
        compare_plot(list_of_songs)
        sys.exit()

    else:
        print("Wrong input")
        sys.exit()


if len(sys.argv) < 2:  # check if the length of argument is less than 2
    print("Insert number of readings")
    print("Use the program like this:: \n\t python3",
          sys.argv[0], " [number]")
    sys.exit()  # exit here if not two inputs

elif len(sys.argv) > 2:  # else if the length of argument is more than 2
    print("Too many inputs")
    print("Exiting program")
    sys.exit()

main()
