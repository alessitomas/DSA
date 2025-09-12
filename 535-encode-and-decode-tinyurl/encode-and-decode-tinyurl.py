class Codec:
    def __init__(self):
        self.START = ord("a")
        self.end = ord("z")
        self.mappings = [self.START]
        self.BASE_URL = "http://tinyurl.com/"
        self.db = {}


    def key_gen(self):
        key_mappings = []
        
        for n in self.mappings:
            key_mappings.append(chr(n))

        self.update_key()

        return "".join(key_mappings)

    def update_key(self):
        for i, n in enumerate(self.mappings):
            if n < self.end:
                self.mappings[i] += 1
                return
        
        self.mappings = [self.start] * (len(self.mappings) + 1)



    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        key = self.key_gen()
        self.db[key] = longUrl
        return self.BASE_URL + key

        

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        return self.db[shortUrl[len(self.BASE_URL):]]
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))