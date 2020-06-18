
class Node:
    def __init__(self, value):  # initial values
        self.value = value
        self.next = None


class LinkedQ:

    def __init__(self):
        self.first = None
        self.last = None
        self.size = 0

    def enqueue(self, x):
        variable = Node(x)

        if self.isEmpty():  # If list is empty the first and the last variable in queue is the same!
            self.first = variable
            self.last = variable
        else:
            self.last.next = variable
            self.last = variable
        self.size += 1

    def dequeue(self):
        v1 = self.first.value
        self.first = self.first.next
        if self.first == None:
            self.last = None

        self.size -= 1

        return v1

    def isEmpty(self):
        return (self.first == None and self.last == None)

    def size_of(self):
        return self.size

    def remove(self, key):  # send in key, remove the first apperence of key by linking the previous to the next
        temp = self.first  # temporary variable

        if (temp is not None):  # if the linkedQ is not empty(none)
            if (temp.value == key):  # if key is the first element
                self.first = temp.next  # set first to next instead
                temp = None  # set temp to none, return new list
                return

        # search key, track the previous node by saving temp as prev, and increasing temp to next, continue..
        while(temp is not None):
            if temp.value == key:
                break
            prev = temp
            temp = temp.next

        if(temp == None):  # if key wasn't found, when temp is none it is finished
            return

        prev.next = temp.next  # Unlink the node, the previous points at the nodes next

        temp = None  # set tempt to none, break out of while loop


# Prova din kö med följande testfall.
l = LinkedQ()

# Skapa en kö, kolla att den är tom


def check_empty():
    if l.isEmpty():
        print("The linked list is empty")
    else:
        print("The linked list is NOT empty")

# Skapa en kö, lägg till och ta bort ett element, kolla att kön är tom


def add_remove():
    l.enqueue(1)
    l.dequeue()

    if l.isEmpty():
        print("The linked list is empty")
    else:
        print("The linked list is NOT empty")

# Skapa en kö, lägg till tre element


def add_3():
    l.enqueue(1)
    l.enqueue(2)
    l.enqueue(3)

#   Kolla att kön inte är tom


def is_not_empty():
    add_3()
    if l.isEmpty():
        print("The linked list is empty")
    else:
        print("The linked list is NOT empty")


#   Plocka ur de tre elementen ett och ett och kontrollera att det är rätt element som returneras.
def get_elements():
    add_3()

    for x in range(l.size_of()):
        x = l.dequeue()
        print(x)


# Söka efter och ta bort det mittersta elementet i en kö med tre noder
def mid():
    l.enqueue(1)
    l.enqueue(2)
    l.enqueue(3)

    l.remove(2)

    new = []
    while not l.isEmpty():
        value = l.dequeue()
        new.append(value)
    print(new)

# Ta bort första elementet i en kö med en nod


def first():
    l.enqueue(1)
    l.remove(1)

    new = []
    while not l.isEmpty():
        value = l.dequeue()
        new.append(value)
    print(new)


# Försök ta bort ett element som inte finns i en kö med några noder (kön ska förbli oförändrad)
def not_exist():
    l.enqueue(1)
    l.enqueue(2)
    l.enqueue(3)

    l.remove(4)

    new = []
    while not l.isEmpty():
        value = l.dequeue()
        new.append(value)
    print(new)

# Försök ta bort ett  element ur en tom kö (inget ska hända och programmet ska inte krascha)


def empty():
    l.remove(4)

    new = []
    while not l.isEmpty():
        value = l.dequeue()
        new.append(value)
    print(new)
# Ta bort sista elementet i en kö med några noder


def last():
    l.enqueue(1)
    l.enqueue(2)
    l.enqueue(3)

    l.remove(3)

    new = []
    while not l.isEmpty():
        value = l.dequeue()
        new.append(value)
    print(new)


last()
