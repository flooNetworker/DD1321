from array import array
from arrayQFile import ArrayQ
from linkedQFile import LinkedQ


with open("cards.txt") as r:  # open file and read lines, the card order separated by a comma
    cards = r.readline()

cards = cards.split(',')  # make list with comma as separator

a = array('l')  # empty array with floats
for i, x in enumerate(cards):
    a.append(int(cards[i]))  # add every item in cards list to the ARRAY


print("The queue is: ", a)  # show the queue as ARRAY

# q = ArrayQ()   # instance q for class ArrayQ/LinkedQ
q = LinkedQ()

# add from array to queue, SIMULATE THE QUEUE (top of queue is right and bottom is left)
for card in range(len(a)):
    q.enqueue(a[0])
    a.remove(a[0])

deq = []

while not q.isEmpty():
    # FIFO, dequeue the first card and enqueue that card
    q.enqueue(q.dequeue())
    deq.append(q.dequeue())  # save the next card


print("The queue will come out in this order: ", deq)

q.enqueue(10)
print(q.dequeue())

# 7,1,12,2,8,3,11,4,9,5,13,6,10
# börja med det man vill ha i mitten: 7
# sen ta varannat kort räknat i den ordning man vill ha 1,2,3...
# var 3e kort är räknat från näst sista och ner
# var 5e kort är räknat från mitten och upp
# TILLS DE MÖTS
# 3e kort inte är sista för måste läggas sist för att komma upp rätt
#   12 11 13 inte 13 12 11
