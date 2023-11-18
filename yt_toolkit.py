from pytube import Search, YouTube
import sys
import shutil

class Youtube_Toolkit:
    def __init__(self):
        self.yt_query = 'https://www.youtube.com/watch?v='
        self.vid_id = None
        self.isrc_code = None

        self.video_name = None
        self.is_success = False

        # Replace it if on another system
        self.CURRENT_LOC = r'C:\Users\Shiv\Music-downloader'
        # Replace it to change where the code is stored
        self.DESTINATION = r'C:\Users\Shiv\Music'


    def generate_vid_id(self):
    # Generates Video Id for the avaialble isrc code
        search_object = Search(self.isrc_code)
        self.vid_id = str(search_object.results).split('=')[1].rstrip('>]')
        
        #Ensuring that the extracted vid_is is of string type
        if (type(self.vid_id) != "<class 'str'>"):
            self.vid_id = str(self.vid_id)

    
    def initialise_isrc_code(self, isrc_code):
    # Used when the isrc_code is available for the song
        self.isrc_code = isrc_code
        self.generate_vid_id()

    def initialise_vid_id(self, vid_id):
    # Used in case isrc_code is not available for any song and vid_id will be directly feeded 
        self.vid_id = vid_id


    def download_the_song(self):
    # Once the vid_id is available or is generated, this function uses it to download the song
        # Create the youtube link for the song
        yt_link = self.yt_query + self.vid_id
        # Search the song using the link
        yt_object = YouTube(yt_link)
        self.video_name = yt_object.title
        # Filter yt_object to extract the audio format song
        stream = str(yt_object.streams.filter(mime_type='audio/mp4')[0])
        #Extract the tag_id from the object
        tag_id = (((((stream.rstrip('>')).lstrip('<')).split(' ')[1]).split('=')[1])).strip('"')
        
        # Download the song using the tag_id
        audio = yt_object.streams.get_by_itag(tag_id)  
        audio.download()

        # Display a success message
        self.is_success = True

        # Moving the audio to  Music directory in PC
        file_loc = self.CURRENT_LOC + '\\' +self.video_name + '.mp3'
        # print(file_loc)
        shutil.move (file_loc, self.DESTINATION)

    def cli_callback(self):
        self.vid_id = sys.argv[1]
        self.download_the_song()

    def display_success_msg(self):
        if self.is_success:
            print(self.video_name + " Downloaded and moved to the specified destination!")
            self.is_success = False
        else:
            print("Song Could not be Downloaded!")
            self.is_success = False
        

def unit_test():
# A simple unit test
    # Sample data:
    VID_ID = ['5clR_JZdZ-k']
    ISRC_CODE = ['QZHN62151552']
    
    yt_toolkit = Youtube_Toolkit()
    print('Downloading songs from the video id ')
    for id in VID_ID:
        yt_toolkit.initialise_vid_id(id)
        yt_toolkit.download_the_song()
        yt_toolkit.display_success_msg()

    print("Check if a song called 𝕋𝕙𝕖 𝕃𝕠𝕤𝕥 𝕊𝕠𝕦𝕝 𝔻𝕠𝕨𝕟 𝕩 𝕃𝕠𝕤𝕥 𝕊𝕠𝕦𝕝 is downloaded or not")
    check = input("Do you see the song? (y/n)   ")
    if check == 'y':
        print("Downloading songs from the isrc_codes")
        for code in ISRC_CODE:
            yt_toolkit.initialise_isrc_code(code)
            yt_toolkit.download_the_song()
            yt_toolkit.display_success_msg()

            print("Check if a song called Link Up is downloaded or not")
            check = input("Do you see the song? (y/n)   ")
            if check == 'y':
                print("Successfully completed the unit test")


def main():
# For downloading songs using Command_line
    yt_toolkit = Youtube_Toolkit()
    yt_toolkit.cli_callback()
    yt_toolkit.display_success_msg()



if __name__ == '__main__':
    main()