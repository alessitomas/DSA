class Codec:
    def __init__(self):
        self.counter = 0
        self.BASE_URL = "http://tinyurl.com/"
        self.db = {}
        self.char = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

    # O(M)
    def key_gen(self):
        chars = []
        num = self.counter
        while num > 0:
            chars.append( self.char[num % len(self.char)] )
            num //= len(self.char)
        
        chars.reverse()
        return "".join(chars)

    # O(M)
    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        key = self.key_gen()
        self.db[key] = longUrl
        self.counter += 1
        return self.BASE_URL + key

        
    # T : O(1)
    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        return self.db[shortUrl[len(self.BASE_URL):]]
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))