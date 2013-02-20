class Event:
    comUrl = {}
    name  = ''
    def __init__(self, comUrl = None):
        if comUrl is not None:
            self.comUrl = comUrl

    def addUrl(self, com, url):
        self.comUrl[com] = url

