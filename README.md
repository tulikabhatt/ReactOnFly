# ReactOnFly #
We built a tool for people to seamlessly react to their friends' posts on Facebook. All you need to do is laugh, smile, and be happy and we take care of the rest for you by liking a post you are looking at.

We built a chrome extension that enables the user's webcam to take photos of the user, capturing thier reaction. We then used Microsoft's Cognitive Services to determine whether a user was smiling (how happy were they?) and based off their reaction we programmed our Chrome Extension to automatically like the Facebook posts they were currently looking at.

Behind the scenese, we push photos to Microsoft's Cloud Azure and then work with a bit of Javascript to pull information through Flask. We have some Python scripts and Java code that interact with Microsoft's APIs and we used PyGame to take a photo of the user every five seconds.  

* In order to run this, request and replaces access tokens for Azure (storefilesintoazure.py)and Microsoft Cognitive Services (emotioncog.py) 
* Install all python dependencies using the command 'pip install -r requirements.txt' 
* Remember to activate your virtual environemnt using source newvenv/bin/activate
* Load your JS files in Google Chrome Extensions 
* Run your python Appserver.py
