Freeseer Video Page Template Editor
====================



## Overview

Freeseer Video Page Template Editor allow users to easily create webpages with a video and optionally integrated ether pad and/or irc client. This helps people with easy chatting or collaborative editing while watching videos, whether it's a live stream or an archived film. 

The template editor also supports customized branding. It's easy to specify color, logo, texts all around the page, as well as full CSS control.

## Workflow

This template editor allows users to create a webpage with Youtube video, etherpad, and IRC client. It also allows automation with multiple pages, with the help of **a csv file** containing a list of video links, etherpad links, etc. 

### Single Page Creation
- Open `index.html` (Currently tested with Chrome 26)
- The dark grey section is the editor. You can click `toggle editor` to hide it and get a real sense of the resulting page.
- In the editor, it's possible to change Logo URL, color, and texts all around the page. All changes are reflected in the bottom half of the page immediately for you to preview. The editor is pre-filled with some default value to give a sense of how it works.
- It's possible to put any text in those text fields -- including html tags. They are not escaped. 
- Users will have full control of CSS to control the look of the page.
- Finally, click `Save as template` button. The page will refresh, then the editor and all disabled sections will be removed. Users can go ahead save this page and upload it to their web server.

### Multiple Page Creation
- Users will customize the look and feel of the page as if they are creating a single webpage.
- It's possible to user place holders for values that will differ between difference pages. For example, it's possible to put `{{ video.youtube_link }}` in the Youtube field. 
- Prepare the csv so that there is a `youtube_link` field for each row. Each row of the csv file will becomes a webpage.
- Save the template. Run a script which takes the template and a csv file as input, generating a batch of webpages. (The script is still in development)


