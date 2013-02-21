import sys
import os
import optparse
import csv
import event
import validurl
import parsecsv
import httpTemplate
from config import *
# the version of webui


webuiUsage = """
    Usage: ./webuicml [-oim] [file]
    -o [folder] : output folder for html files
    -i [file]   : input csv file for multiple html page
    -u          : verify input url
   """
   
welcomeMessage = """
    Welcome to webui generator.
    Please choose component you want for your webui for live events.
    """

def chooseComponent(componentName):
    choice = raw_input(componentName + " : (Y/n)\n")
    while (choice.lower() != "y" and choice.lower()!= "n"):
        print "Your input " + choice + "is not a valid input. Please choose between y(yes) or n(no)"
        choice = raw_input(componentName + " : (Y/n)\n")

    if choice.lower() == "y":
        return True
    if choice.lower() == "n":
        return False

def readUrl(componentName):
    url = raw_input('Please input the URL for ' + componentName + '\n')
    return url

def manualMode(opt):
    print welcomeMessage
    eventName = raw_input("name of this event:")
    newEvent = event.Event(eventName)
    for com in componentList:
        if chooseComponent(com):
            url = readUrl(com)
            if opt.verifyUrl:
                if not validurl.verifyUrl(url):
                    print "ERROR: " + url + "is not valid. Abort."
            newEvent.addUrl(com, url)
    return [newEvent]

def csvMode(opt):
    return parsecsv.parseCsv(opt.input, opt.verifyUrl)


# parse the option input by users
def parseargs():
    parser = optparse.OptionParser(version = webuiVersion,
            usage = webuiUsage)
    parser.add_option('-o', '--output',
            dest = 'output', default = 'output/',
            help = 'location to store the output html page.')
    parser.add_option('-i', '--input',
            dest = 'input', default = False,
            help = 'input csv file for multiple html page.If not given, will enter manual mode.')
    parser.add_option('-u', '--url',
            action = 'store_true', dest = 'verifyUrl',
            help = 'check if the given url is valid and exists')
    (option, args) = parser.parse_args()

    if args:
        parser.print_help()
        print >> sys.stderr, _('Unexpected arguments!')
        sys.exit(1)
    return option, args, parser

def main():
    opt, args, parser = parseargs()
    eventList = []
    if not os.path.exists(opt.output):
        os.makedirs(opt.output)
        print "Creating the output directory : " + opt.output
    else:
        print "existing directory"
    if opt.input:
        eventList = csvMode(opt)
        print "has input"
    else:
        eventList = manualMode(opt)
        print "doesn't have input"

    for e in eventList:
        filename = opt.output + '/' + e.name + '.html'
        httpTemplate.createHTMLFile(e, filename)

if __name__ == '__main__':
    sys.exit(main())
