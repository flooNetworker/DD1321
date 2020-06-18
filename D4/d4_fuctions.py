from heap import Heap


def linsok(songlist, testartist):

    for element in songlist:
        artist = element.artist

        if artist == testartist:
            return True

    return False


def binsok(songlist, testartist):
    floor = 0
    ceil = len(songlist)-1
    found = False

    while floor <= ceil and not found:
        mid = (floor+ceil)//2
        if songlist[mid].artist == testartist:
            found = True
        else:
            floor = mid + 1

    return found


def testing(songlist, testsong):

    if linsok(songlist, testsong.artist):
        print(testsong.artist, "exists in list")
        return True
    else:
        print(testsong.artist, "not in list")
        return False


# O(n log N)
def mergesort(songlist):
    if len(songlist) > 1:
        mid = len(songlist)//2
        left = songlist[:mid]
        right = songlist[mid:]

        mergesort(left)
        mergesort(right)

        l, r, k = 0, 0, 0

        while l < len(left) and r < len(right):
            if left[l] < right[r]:
                songlist[k] = left[l]
                l += 1
            else:
                songlist[k] = right[r]
                r += 1
            k += 1

        while l < len(left):
            songlist[k] = left[l]
            l += 1
            k += 1

        while r < len(right):
            songlist[k] = right[r]
            r += 1
            k += 1

        return songlist


def partitionera(songlist, v, h, pivot):
    while True:
        v = v + 1
        while songlist[v] < pivot:
            v = v + 1
        h = h - 1
        while h != 0 and songlist[h] > pivot:
            h = h - 1
        songlist[v], songlist[h] = songlist[h], songlist[v]
        if v >= h:
            break
    songlist[v], songlist[h] = songlist[h], songlist[v]
    return v


def quicksort(songlist, floor, ceil):

    mid = (floor+ceil)//2

    # flytta pivot till kanten
    songlist[mid], songlist[ceil] = songlist[ceil], songlist[mid]

    # damerna först med avseende på pivotsonglist
    mid = partitionera(songlist, floor-1, ceil, songlist[ceil])

    # flytta tillbaka pivot
    songlist[mid], songlist[ceil] = songlist[ceil], songlist[mid]

    if mid-floor > 1:
        quicksort(songlist, floor, mid-1)
    if ceil-mid > 1:
        quicksort(songlist, mid+1, ceil)

    return songlist


def heapsort(songlist):

    h = Heap(len(songlist)-1)

    for word in songlist:
        h.put(word, word)

    new = []
    while not h.isEmpty():
        new.append(h.get())

    return new

