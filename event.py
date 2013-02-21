class Event:
    comUrl = {}
    filename = ""
    name  = ''
    def __init__(self, name, comUrl = None):
        self.name = name
        if comUrl is not None:
            self.comUrl = comUrl

    def addUrl(self, com, url):
        self.comUrl[com] = url

