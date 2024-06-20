class PaginaWeb:
    def __init__(self, url):
        self.url = url
        self.siguiente  = None
    def __str__(self):
        return f"url: {self.url}"
    

        
        