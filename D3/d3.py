from arrayQ import ArrayQ
from linkedQ import LinkedQ
from Node import Node
from Dicthash import DictHash
import sys


d = DictHash()
new_d = DictHash()
q = ArrayQ()
chain = []

#------------------------------#
#  Read file
acceptable_words = set()
with open("word3.txt", 'r') as r:
    line = r.readline()
    while line:
        word = line.strip()
        acceptable_words.add(word)
        line = r.readline()

#------------------------------#
#  makeChildren
# IN: word that will have children, list of acceptable words
# UT: Void (only enqueue the created children)


def makechildren(parent, words):
    parent = parent
    word = list(parent)

    start = 97
    swe = ["å", "ä", "ö"]
    str1 = ""

    for i in range(len(word)):  # each character in parent
        for j in range(26):  # alphabet length
            word[i] = chr(start)

            child = str1.join(word)  # make str of child

            if d.search(child) == None:  # returns none if not already in dict
                # STORE CHILDREN IN DICTHASH, CHILD AS KEY, UNIQUE VALUES,  [CHILD:PARENT]
                d.store(child, parent)

            word = list(parent)

            start += 1

        start = 97

    for i in range(len(word)):
        count = 0
        for j in range(len(swe)):  # add swedish letters
            word[i] = swe[count]

            child = str1.join(word)  # make str of child

            if d.search(child) == None:  # returns none if not already in dict
                # STORE CHILDREN IN DICTHASH, CHILD AS KEY, UNIQUE VALUES,  [CHILD:PARENT]
                d.store(child, parent)

            word = list(parent)

            count += 1

    k = 0  # count the number of children
    new_d.words = {}  # reset each time new children are born

    for child in d.words:
        if d.words[child] == parent:
            if child in words:  # check if child is an acceptable word
                if child != parent:  # remove duplicated as child?
                    new_d.store(child, parent)
                    k += 1

    # print("The number of children for", parent, "are", k)
    # print("gamla ord", d.words)
    # print("nya ord", new_d.words)

    for child in new_d.words:
        node = Node()
        node.child = child
        node.parent = new_d.search(child)
        q.enqueue(node)


#------------------------------#
#  writeChain
# IN: node with solution as child
# UT: Void (only print the way to child from root
def writeChain(node):

    prevNode = Node()
    prevNode.parent = d.search(node.parent)
    prevNode.child = node.parent
    chain.append(prevNode.child)

    # skriv ut kedja i rätt ordning
    if prevNode.child == root:
        k = len(chain)

        print("The way to", solution, "starting with root", root, "is:")
        for i in range(k):
            print(chain[k-1])
            k -= 1
        print(solution)

        return 0

    node = prevNode
    writeChain(prevNode)


#------------------------------#
#  MAIN

if len(sys.argv) < 3:  # check if the length of argument is less than 3
    print("Insert root and solution")
    print("Use the program like this:: \n\t python3",
          sys.argv[0], " [root] [solution]")
    sys.exit()  # exit here if not two inputs

elif len(sys.argv) > 3:  # else if the length of argument is more than 3
    print("Too many inputs")
    print("Exiting program")
    sys.exit()

else:
    if sys.argv[1] == sys.argv[2]:  # check that root is not solution
        print("The root is equal to the solution")
        print("Exiting program")
        sys.exit()

# input has to be words of three characters
if len(sys.argv[1]) != 3 or len(sys.argv[1]) != 3:
    print("Too many characters in at least one of the words")
    sys.exit()

# root
root = sys.argv[1]
# final word
solution = sys.argv[2]

n = Node()
n.child = root
# queue the root
q.enqueue(n)

while not q.isEmpty():  # as long there is a queue
    nextNode = q.dequeue()  # take first node out of queue

    if nextNode.child == solution:  # if node is solution, writechain
        print("We found the solution", nextNode.child)
        writeChain(nextNode)
        break

    else:
        # send in parent-word (child of node) to make children, send in list of acceptable words
        makechildren(nextNode.child, acceptable_words)

if q.isEmpty():
    print("There was no way to", solution)  # if no solution found
