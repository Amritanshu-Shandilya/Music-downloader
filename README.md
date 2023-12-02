# Music Downloader

This project is built for those who, like me, are frustrated from ads on music streaming apps and/or want to stop paying money to listening add-free music on music streaming apps. This project works by downloading the songs from your youtube into your own local storage, so you can listen to them anytime without any ads and without spending any money to get any kind of premium subscription.


## Current-version -> **v1.2.4**
Currently it is in *version 1.2.4* where you can download a single song (the first one) from it's youtube link through the command line and it will be stored inside the predefined location.

![Demonstration:](/readme.png)


*I will not be working on later versions and ideas as this project is good enough for me at this stage. Sometime later if I wish or there is a need to I will revisit this project to add on new features or change something that needs to be changed.*

## Python library dependencies: 
(Clicking on these hyperlinks will take you to the documentation page of these libraries)
  1. pytube -> For downloading audio files from youtube
  2. sys -> for accepting command line arguments
  3. watchdog -> for detecting new files in the source folder
  4. shutil -> for moving the files
  

## v1.0
This version, as stated earlier, was a proof of concept for this idea. So right now it can download only a single song from a playlist, the first one to be exact, and save it in the Present Working Directory - besides the python code that downloaded it.

## v1.1
This version, downloads song's audio using its youtube id in the same folder where the code is located.

## v1.2
This version, downloads the song in mp4 audio format and stores it inside a pre mentioned location. It is downloading the song almost all of the time but it is not saving all songs in the specified folder.

## Action-Plan :
Suggested improvements in future versions. This is not final and can change if it needs to be
#### Improvements to be made in v1 -
1. Change the code structure to make it more efficient
2. Store the downloaded songs in a predefined folder
3. Make it able to download more than one song. 

#### Improvements for v2 -  
1. Add an option to save music to an external drive like a SD card or a USB pendrive, and not in the current folder.
2. Support playlist creation.

#### Improvements for v3 -
1. Make a bot to give inputs to this program. Preferably a Discord bot.
   
### Improvements for v4 -
1. Automate the process.
2. Make it as a CLI tool. 

#### Improvements for v4 -
1. Make a Graphical User Interface for this, so that anyone can use it easily.
2. Make it run on Raspberry pi. 
3. 
   
#### Improvements for v6 and beyond - 
1. Turn it into a free full-fleged music server connected through IoT.
2. Generating recommendations for next song. 
3. Make it compatible with alexa and google-home. 
4. Do things using audio commands from user.
5. Make a dedicated app.
   
## Changelog
A list of changes made in all commits/versions.
### v1.0 :
- **v1.0.1 ->** Base commit, pushed the code for downloading audio files.
- **v1.0.1 ->** The first working code that downloads a single song
- **v1.0.2 ->** Removed unused libraries, and wrote this readme
- **v1.0.3 ->** Made the code Object-oriented
- **v1.1.3 ->** Removed spotipy as it was error prone, fixed some minor mistakes and updated this readme
- **v1.2.1 ->** Added code to store song inside the Music folder inside the C://
- **v1.2.2 ->** 100% succesful shifting of the music from one folder to another
- **v1.2.4 ->** Taking links from users and storing it in a folder


## Contributors :
- **Amritanshu-Shandilya** 