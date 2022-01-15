# Project2
DEVELOPMENT OF IOT BASED SMART INTRUDER PREVENTION SYSTEM WITH WEB SERVER USER INTERFACE APPLICATIONS

This projects involves developing a IOT based smart intruder prevention system, which automatically detects any intrusion and alerting the users through the Telegram app. Besides, provides the users 24 hrs live video streaming of their premise through manually developed Webpage. This system also has counter action capabilities which helps to prevent the intrusion happening by just using their smart devices.

For the file management:
pytho files
1) bot.py file for the Telegram automated message using Telegram ID token.
2) raspi.py The detection program uses PIR sensor. (The bot.py file will be integrated into raspi.py file in order to generate the alert message upon detection)
3) camera_pi.py file enables the live streaming.
4) UI.py is the main file runs the overall system.

Templates Folder
1) camera.html
2) index.html
3) login.html

Note: Create a New folder, in that folder saves all the python files and html files. Make sure to put all the html files into a seperate folder.
