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

import datetime
class Event(object):
    '''
    Event class used for each event to store the dictionary pair of component name and its url address. 
    '''
    componentUrl = {}
    name  = ''
    def __init__(self, name, componentUrl = None):
        self.name = name
        if componentUrl is not None:
            self.componentUrl = componentUrl

    def addUrl(self, component, url):
        '''
        add a component and url pair to dictionary
        '''
        self.componentUrl[component] = url
    
    def getHtmlFormat(self):
        '''
        return data in format to creat html
        '''
        data = []
        for component in self.componentUrl.keys():
            d = {}
            d['title'] = component
            d['url'] = self.componentUrl[component]
            d['date'] = str(datetime.date.today())
            d['content']= ''
            data.append(d)
        return data

