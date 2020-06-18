

class Node:
    def __init__(self, key, val=None):
        self.key = key
        self.val = val
        self.right = None
        self.left = None


def rekstore(node, key, newvalue):

    if node == None:
        return Node(key, newvalue)

    if node.key:
        if key < node.key:
            if node.left is None:
                node.left = Node(key, newvalue)
            else:
                rekstore(node.left, key, newvalue)
        elif key > node.key:
            if node.right is None:
                node.right = Node(key, newvalue)
            else:
                rekstore(node.right, key, newvalue)
    else:
        node.key = key
        node.val = newvalue

    return node


def reksearch(node, key):
    if node == None:
        return False

    if node.key == key:
        return node

    if node.key < key:
        return reksearch(node.right, key)

    if node.key > key:
        return reksearch(node.left, key)


def rekwrite(node):

    if node == None:
        return
    rekwrite(node.left)
    print(node.key)
    rekwrite(node.right)


class Bintree:
    def __init__(self):
        self.root = None
        self.size = 0

    def store(self, key, newvalue):
        # Sorterar in newvalue i trädet
        self.root = rekstore(self.root, key, newvalue)
        self.size += 1

    def search(self, key):
        # returnerar value om key finns i trädet, KeyError annars
        if not reksearch(self.root, key):
            raise KeyError('KEY NOT IN BINTREE')

        return reksearch(self.root, key)

    def __contains__(self, key):
        #     # True om key finns i trädet, False annars
        node = reksearch(self.root, key)

        if node:
            return True
        else:
            return False

    def write(self):
        # Skriver ut trädet i inorder
        rekwrite(self.root)
   