#!/usr/bin/python
# -*- coding: utf-8 -*-

# freeseer - vga/presentation capture software
#
#  Copyright (C) 2013  Free and Open Source Software Learning Centre
#  http://fosslc.org
#
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program.  If not, see <http://www.gnu.org/licenses/>.

# For support, questions, suggestions or any other inquiries, visit:
# http://wiki.github.com/fosslc/freeseer/

import sys
import os
import optparse
import csv
import event
import validurl
import parsecsv
import httpTemplate
from config import *


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
    '''
    prompt in the terminal to ask user to choose whether a component should be included in html page
    '''
    choice = raw_input(componentName + " : (Y/n)\n")
    return not choice or choice[0].lower() == 'y'

def readUrl(componentName):
    '''
    prompt in the terminal to ask user to give url for a component
    '''
    url = raw_input('Please input the URL for ' + componentName + '\n')
    return url


def manualMode(opt):
    '''
    Handle user input through command line to get url information for a event
    '''
    print welcomeMessage
    eventName = raw_input("name of this event:")
    newEvent = event.Event(eventName)
    # collect information for each commponent for this event
    for com in componentList:
        if chooseComponent(com):
            url = readUrl(com)
            # validate the given url if requested by user
            if opt.verifyUrl:
                if not validurl.verifyUrl(url):
                    print "ERROR: " + url + "is not valid. Abort."
            newEvent.addUrl(com, url)
    return [newEvent]


def csvMode(opt):
    '''
    handler user input through a csv file to get url information for multiple events
    '''
    return parsecsv.parseCsv(opt.input, opt.verifyUrl)



def parseargs():
    '''
    parse the command line option input by users
    '''
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
    return option

def main():
    '''
    main logic for this tool
        read options 
        get data either through csv file or command line input
        generate html file for each event
    '''
    
    # parse the option in this argument
    opt = parseargs()
    eventList = []
    # create the output folder if not already exists
    if not os.path.exists(opt.output):
        os.makedirs(opt.output)
        print "Creating the output directory : " + opt.output
    else:
        print opt.output + " already exists"
        
    # check whether use command line manual input or csv file
    if opt.input:
        eventList = csvMode(opt)
    else:
        eventList = manualMode(opt)

    print "Creating html files..."
    # for each of the event, create a html file and store it to the given location
    for e in eventList:
        filename = opt.output + '/' + e.name + '.html'
        httpTemplate.createHTMLFile(e, filename)
        
if __name__ == '__main__':
    sys.exit(main())
