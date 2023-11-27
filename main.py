from yt_toolkit import Youtube_Toolkit

from os import scandir, rename
from os.path import splitext, exists, join
from shutil import move
from time import sleep

import subprocess
import sys

try:
    from watchdog.events import FileSystemEventHandler
    from watchdog.observers import Observer
except ModuleNotFoundError:
    print("Install Watchdog library: python -m pip install -U watchdog")

# Pyusb libraries for verifying the presence of a usb drive
try:
    import usb.core
    import usb.util
except ModuleNotFoundError:
    print("Install pyusb module: pip install pyusb")


USB_PRESENCE = False


class music_management (Youtube_Toolkit, FileSystemEventHandler):
    def __init__(self):
        super().__init__()
        self.download_list = None
        # self.isDetected = False

        # Paths
        self.source = self.src = r'C:\Users\Shiv\Music-downloader'
        self.destinaton  = None
        self.des = None

        
        self.default_destination = r'C:\Users\Shiv\Music'

        """Replace with your drive's details"""
        self.idVendor = None
        self.idProduct = None

    def reset(self):
        # Resets the source and destination
        self.source = self.src
        self.destinaton = self.des
    
    def usb_detection(self):
        # Finding the drive
        if USB_PRESENCE:
            # Specify the path inside the USB
            self.destinaton = None
        else:
            # Use default location
            self.destinaton = self.des = self.default_destination

    def move_the_file(self, name):
        self.video_name = name
        # Creating the absolute path to the file
        self.source = self.source + '\\' +self.video_name
        self.destinaton = self.destinaton + '\\'+self.video_name
        move(self.source, self.destinaton)
        print('Moved the song to the destination!')
        
        
        # We can use FileExistsError to check if the song is already downloaded or not

    def check_audio_files(self):

        with scandir(self.source) as entries:
            for entry in entries:
                name = entry.name
                if name.endswith('mp4') or name.endswith('MP4'):
                    self.move_the_file(name)


    def download_from_id(self,id):
        self.initialise_vid_id(id)
        self.download_the_song()
        self.display_success_msg()
        self.check_audio_files()
        self.reset()

        
    def download_from_a_list(self, filepath):
    # Downloads all the songs from the list provided
        self.download_list = open(filepath, 'r').readlines()
        
        for id in self.download_list:
            self.initialise_vid_id(id.rstrip())
            self.download_the_song()
            self.display_success_msg()
            self.check_audio_files()
            self.reset()
        
        print("End of File!")

def unit_test():
    main_obj = music_management()
    file = 'id_for_test.txt'
    #main_obj.check_audio_files()
    main_obj.usb_detection()
    main_obj.download_from_a_list(file)

def main():
    main_obj = music_management()
    vid_link = sys.argv[1]
    vid_id = vid_link.split('v=')[1]
    main_obj.usb_detection()
    main_obj.download_from_id(vid_id)
    

if __name__ == '__main__':
    main()