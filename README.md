# CW2

***Web app Created by Usman Ashraf - 40096834***

To run app, run levinux and pull GIT clone from: 
https://github.com/UAshraf123/CW2.git

Go into the src folder via the following linux command: 

cd /home/tc/CW2/src

Within this directory, you will find python script "index.py"

To run the script/webapp, type the following: 

python index.py

Once the levenix has restarted the app and given you the debugger pin, go into 
your browser and enter the url: http://localhost:5000

This will open the web app.

To close everything down, press CTRL+C within levenix, and shut down levenix
safely by typing "sudo poweroff". 


**TESTING** Can be done by typing: python test.py - when in the correct level ( cd /home/tc/CW2/src ) 

**LOGGER" - This can only be used when you are NOT in debug mode, which in the real world is how your web app would generally run. Please remove "debug=True" from index.py, and create an error, such as instead of "return render_template('index.html')", do "return 1 / 0", then when you run the app (python index.py) and go to localhost:5000 on your web browser, an error will occur and this WILL be logged within file  "errorlog.txt". If the file does not exist, the file will be created. 
