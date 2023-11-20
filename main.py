from yt_toolkit import Youtube_Toolkit

# Pyusb libraries for verifying the presence of a usb drive
import usb.core
import usb.util

class MAIN_BODY (Youtube_Toolkit):
    def __init__(self):
        super().__init__()
        self.download_list = None
        self.isDetected = False

        """Replace with your drive's details"""
        self.idVendor = None
        self.idProduct = None
    
    def usb_detection(self):
        # Finding the device
        if usb.core.find(bDeviceClass=8) is None:
            raise ValueError("No Mass Storage device found!")
        
    def download_from_a_list(self, filepath ):
    # Downloads all the songs from the list provided
        self.download_list = open(filepath, 'r').readlines()
        
        for id in self.download_list:
            self.initialise_vid_id(id.rstrip())
            self.download_the_song()
            self.display_success_msg()
        
        print("End of File!")

def unit_test():
    main_obj = MAIN_BODY()
    file = 'id_for_test.txt'
    main_obj.download_from_a_list(file)

def main():
    main_obj = MAIN_BODY()
    main_obj.usb_detection()

if __name__ == '__main__':
    main()