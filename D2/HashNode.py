class HashNode:
    def __init__(self, key, data):
        self.key = key
        self.data = data


class HashTable:
    def __init__(self):
        self.size = 5
        self.hash_table = [None] * self.size

    def hash_func(self, key):

        hashcode = 0
        for c in key:
            hashcode = hashcode*32 + ord(c)
        hashcode = hashcode % len(self.hash_table)

        return hashcode
        # HASHFUNKTIONEN: Addera ascii av alla tecken i stringen -- DÅLIGT då det kan bli dubbelt (samma bokstäver)
        #   Jag använder samma struktur som pythons inbyggda funktion Hash(), tar flr varje bokstav i nyckeln ta *32 och inbygga ord(bokstav)

    def store(self, artist, song):
        node = HashNode(artist, song)
        hash_key = self.hash_func(node.key)

        key_exists = False
        slot = self.hash_table[hash_key]

        # CHECK IF TABLE IS FULL
        count = 0
        for element in self.hash_table:
            if element == None:
                break
            else:
                count += 1
        if count == self.size:
            raise KeyError("THE HASHTABLE IS FULL")

        # STORE AS ONG KEY EXIST
        while not key_exists:

            if slot == None:
                self.hash_table[hash_key] = node
                key_exists = True

            else:
                if slot.key == node.key:
                    # The artist already exist, re-writing")
                    self.hash_table[hash_key] = node
                    key_exists = True

                else:
                    # KROCKHANTERING: jag använder LINEAR PROBING  men har i åtanke att det är risk för clustring, har större hashtabell än antal värden
                    if hash_key == self.size:
                        hash_key = 0
                    else:
                        hash_key = (hash_key+1) % len(self.hash_table)
                        slot = self.hash_table[hash_key]
                    # LÄGG TILL ATT DEN BÖRJAR PÅ 1

    def search(self, key):
        hash_key = self.hash_func(key)
        slot = self.hash_table[hash_key]
        found = False

        # raise keyError om nycklen inte finns (slot==None)
        if slot == None:
            raise KeyError("THE KEY DOES NOT EXIST")

        while not found:
            if slot.key == key:
                found = True

            else:
                hash_key = hash_key+1
                slot = self.hash_table[hash_key]

        return slot.data
