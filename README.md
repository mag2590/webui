webui
=====

Freeseer Web UI project

This software would allow you to create html page with live video stream, IRC 
Channel and etherpad through command line interfacce. 

Dependencies and Libraries:
The webUI Generator consists of two parts:
1)  A commandLine tool 
2)	A Template Editor
For the commandLine tool, we have the following classes: 
cmlControl.py
config.py
event.py
httpTemplate.py
parsecsv.py
validurl.py
External libraries:
The httpTemplate.py class depends on the external library Jinja 2. Download and install the Jinja 2 version compatible with python 2.7
For the Template Editor, we have a separate detailed README inside the Editor section.
Configuration details:
In order to run the Command Line Tool run the cmlControl.py class.  There are two ways to run this class:
1)	Manual Mode
2)	CSV mode
1)Manual Mode:
This will prompt you to enter the URL for YouTube video or live stream, the Etherpad and IRC channel.
Based on the Command Line inputs, it generates a corresponding HTML Template using the Jinja 2 framework based template generator.
 2)CSV Mode:
For this mode, we have created two test CSV files.  However, user can create his/her own CSV file and pass it as argument to the cmlControl.py class, along with the corresponding command.
Example usage:
-i test.csv
Where, -i is the first argument (args[0]) which stands for  input CSV file.
test.csv is the second argument (args[1]), which is the name of the CSV file.

