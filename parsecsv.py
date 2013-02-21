import csv
import sys
import event
import validurl
from cmlControl import componentList

def parseCsv(filename, checkUrl):
    data = csv.reader(open(filename))
    # Read the column names from the first line of the file
    fields = data.next()
    # class for the name of each event
    # print fields
    eventName = EventName(fields)
    eventList = []
    
    for row in data:
        # Zip together the field names and values
        items = zip(fields, row)
        comUrl = {}        
        for (name, value) in items:
            if not name.strip()== 'name':
                # Validate the url given
                if checkUrl:
                    if not validurl.verifyUrl(value.strip()):
                        print >> sys.stderr, value.strip() + " invalid url"
                        exit(1)
                comUrl[name.strip()] = value.strip() 
        e = event.Event(eventName.getEventName(items), comUrl)
        eventList.append(e)
    return eventList


def varifyFields(fields):
    for f in fields:
        if f not in componentList and f != "name":
            print >> sys.stderr, _("Unknow component: " + f + ".")
            exit(1)
    
    

# if the event name is given, return the event name
# otherwise automatically generate eventmane starting from 0
class EventName:
    default = 0
    useDefault = True
    def __init__(self, fields):
        if "name" in fields:
            self.useDefault = False
            
    def getEventName(self, zip):
        if self.useDefault:
            self.default += 1;
            return str(self.default-1)
        else:
            return [i[1] for i in zip if i[0] == "name"][0]
           
    
    
