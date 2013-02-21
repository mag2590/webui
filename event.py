import datetime
class Event:
    # stores the dictionary pair of component name and its url address
    comUrl = {}
    name  = ''
    def __init__(self, name, comUrl = None):
        self.name = name
        if comUrl is not None:
            self.comUrl = comUrl

    # add a component and url pair to dictionary
    def addUrl(self, com, url):
        self.comUrl[com] = url
    
    # return data in format to creat html
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

