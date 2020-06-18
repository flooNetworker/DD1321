class DictHash:
    def __init__(self):
        self.words = {}

    def store(self, key, data):
        self.words[key] = data

    # search for the key in my dictionary
    def search(self, key):
        if key in self.words:
            return self.words[key]
        else:
            return None

    # to be able to write h[key]

    def __getitem__(self, key):
        return self.search(key)
