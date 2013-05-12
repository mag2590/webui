import datetime
import jinja2
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



# NOTE: in this template there is no data relating to specific posts.
# There are only references to data structures passed in from your main code
page_template = jinja2.Template('''
    
    <div align="center">
     
    {% block blog_posts %}
        <!-- links/targets for the side menu to jump to a post -->
        <head>
        <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
        <title>WebUI HomePage</title>
        <link rel="stylesheet" href="template.css" type="text/css" />
        </head>
        <body>
        <h1>Welcome to Freeseer online portal</h1>
        {% for post in posts1 %}
          <li><a href="{{ post.url }}">{{post.title}}-{{post.content}} 
                                       </a></li>
          
          
          <iframe src="{{post.url}}" width="500" height="200" style="float:left"></iframe>
          
        {% endfor %}
        {% for post in posts2 %}
          <li><a href="{{ post.url }}">{{post.title}}-{{post.content}} 
                                       </a></li>
          
          
          <iframe src="{{post.url}}" width="500" height="200" style="float:right"></iframe>
          
        {% endfor %}
        
        {% for post in posts3 %}
          <li><a href="{{ post.url }}">{{post.title}}-{{post.content}} 
                                       </a></li>
          
          
          <iframe src="{{post.url}}" width="500" height="200" style="float:center"></iframe>
          
        {% endfor %}
    {% endblock %}
    </div>
    
    {% block content %}
        <div id="post">
            <h1>{{ current.title }}</h1>
            <h2>{{ current.date }}</h2>
            <p>{{ current.content }}</p>
        </div>
        <div id="postB">
            <h1>{{ current.title }}</h1>
            <h2>{{ current.date }}</h2>
            <p>{{ current.content }}</p>
        </div>
        <div id="postC">
            <h1>{{ current.title }}</h1>
            <h2>{{ current.date }}</h2>
            <p>{{ current.content }}</p>
        </div>


    {% endblock %}
    
    </body>
    
''')

# NOTE your main code would create a data structure such as this 
# list of dictionaries ready to pass in to your template
now=datetime.date.today()

post_1 = [
         { 'url' : 'http://www.icecast.org/',
          'title' : 'Icecast',
          'date' : now,
          'content' : 'This is the icecast streaming channel'}

        ]

post_2=[ { 'url' : 'http://www.irc.org/',
          'title' : 'IRC channel',
          'date' : now,
          'content' : 'This is the IRC channel'}
        ]
post_3=[{'url': 'http://etherpad.org/',
          'title':'Etherpad',
          'date':now,
          'content':'Etherpad is an online editor'}
        ]


# Pass in a full list of posts and a variable containing the last
# post in the list, assumed to be the most recent. 
s=page_template.render(posts1 = post_1, post2=post_2, post3=post_3, current=post_2[0]
                            )
with open("httpTemplate.html","w") as html_file:
    html_file.write(s)
     
f2=open("httpTemplate.html","r+")
m=f2.read()
#print m


# pass the event with url data and location to store the resulting html file
# apply html template and store it to file 
#def createHTMLFile(event, fileLocation):
#    eventPost = event.getHtmlFormat()
#    s=page_template.render(posts = eventPost,
#                           current = eventPost[0])
#    with open(fileLocation,"w") as html_file:
#        html_file.write(s)
#        
#
#
#    f2=open("httpTemplate.html","r+")
#    m=f2.read()
#    print m

    