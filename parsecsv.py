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
import csv
import sys
import event
import validurl
from config import *


def parseCsv(filename, checkUrl):
    '''
    create a list of events based on the input csv file
    '''
    
    data = csv.reader(open(filename))
    # Read the column names from the first line of the file
    fields = data.next()
    # class for the name of each event
    # print fields
    eventName = EventName(fields)
    eventList = []
    # for each of the event given
    # create a event object for it with the data
    for row in data:
        # Zip together the field names and values
        items = zip(fields, row)
        componentUrl = {}
        # create a dictionary of component name to its url for this event 
        for (name, value) in items:
            if not name.strip()== 'name':
                # Validate the url given
                if checkUrl and not validurl.verifyUrl(value.strip()):
                        print >> sys.stderr, value.strip() + " invalid url"
                        exit(1)
                componentUrl[name.strip()] = value.strip() 
        e = event.Event(eventName(items), componentUrl)
        eventList.append(e)
    return eventList



def varifyFields(fields):
    '''
    verify if all the fields given in in the component list
    '''
    for field in fields:
        if field not in componentList and field != "name":
            print >> sys.stderr, _("Unknow component: " + field + ".")
            exit(1)
    
    

class EventName(object):
    '''
    class to handle the name of the event
    if the event name is given, return the event name
    otherwise automatically generate event name starting from 0
    '''

    def __init__(self, fields):
        self.default = 0
        self.useDefault = 'name' not in fields
    
    def __call__(self, zip):
        if self.useDefault:
            self.default += 1;
            return str(self.default-1)
        else:
            return [i[1] for i in zip if i[0] == "name"][0]
           
    
    
