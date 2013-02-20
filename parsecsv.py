import csv
import sys
import event
import validurl
from cmlControl import componentList
def csvParser(filename, checkUrl):
    data = csv.reader(open(filename))
    # Read the column names from the first line of the file
    fields = data.next()
    eventList = []
    for row in data:
        # Zip together the field names and values
        items = zip(fields, row)
        comUrl = {}
        # Add the value to our dictionary
        e = event.Event()
        for (name, value) in items:
            if name is not 'name':
                if checkUrl:
                    if not verifyUrl.validUrl(value.strip()):
                        print >> sys.stderr, _(value.strip() + " invalid url")
                        exit(1)
                conUrl[name] = value.strip()
        else:
            eventName = value.strip()
        e = event.Event(conUrl)
        e.name = eventName
        eventList.add(e)
    return eventList

