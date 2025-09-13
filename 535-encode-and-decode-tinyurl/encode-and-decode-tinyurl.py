class Codec:
    def __init__(self):
        self.counter = 0
        self.BASE_URL = "http://tinyurl.com/"
        self.db = {}
        self.char = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

    # O(log Counter)
    def key_gen(self):
        chars = []
        num = self.counter
        
        if num == 0:
            return self.char[0]
        
        while num > 0:
            chars.append( self.char[num % len(self.char)] )
            num //= len(self.char)
        
        chars.reverse()
        return "".join(chars)

    # O(log Counter)
    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        if not longUrl:
            return 

        key = self.key_gen()
        self.db[key] = longUrl
        self.counter += 1
        return self.BASE_URL + key

        
    # T : O(1)
    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        if not shortUrl.startswith(self.BASE_URL):
            return 

        encoding = shortUrl[len(self.BASE_URL):]
        
        if encoding not in self.db:
            return 
        
        return self.db[encoding]
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))