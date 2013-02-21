import datetime
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
    
    def getHtmlFormat(self):
        data = []
        for com in self.comUrl.keys():
            d = {}
            d['title'] = com
            d['url'] = self.comUrl[com]
            d['date'] = str(datetime.date.today())
            d['content']= ''
            data.append(d)
        return data

