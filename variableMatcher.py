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
import parsecsv
import validurl
import fileinput

"""
This function is used to replace the variables specified in the editor with their
corresponding contents from the csv file.

"""
def replaceVarWithContents(savedtemplate,csvfile):
    f=open(savedtemplate,'r+')
    templateString=f.read()
    fields=[]
    mycsv=list(csv.reader(open(csvfile,'r+'),delimiter=','))
    fields=mycsv[0]
    #print len(fields)
    for i in xrange(0,len(mycsv)):
        for j in xrange(1, len(fields)):
            if(mycsv[i][0]+"."+mycsv[0][j] in templateString):
                templateString=templateString.replace(mycsv[i][0]+"."+mycsv[0][j], mycsv[i][j])

    f.close()
    f=open(savedtemplate,'w+')
    f.write(templateString)

    print templateString

def main():
    replaceVarWithContents('index_test.html','test1.csv')

main()
