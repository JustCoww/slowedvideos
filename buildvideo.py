# Questions
audio_mode = input('What audio mode do you want to use? ( URL (1) / File (2) ): ')
cover_mode = input('What cover mode do you want to use? ( URL (1) / File (2) ): ')
song = input('Song name: ')
artist = input('''Artist's name: ''')

# Importing modules to create and enter the folder
from os import mkdir, chdir
from shutil import copy

# Creating the folder
folder = f'slowed {song}'
mkdir(folder)

# Getting audio file
if audio_mode == '1':
    url = input('Audio URL: ')
    audio = 'original'
    from slowedvideos import downloadurl

    chdir(folder)
    downloadurl(url, audio)
    chdir('..')

    audio = 'original.wav'
else:
    audio = input('Audio location: ')
    copy(audio, folder)

# Getting cover file
if cover_mode == '1':
    url = input('Cover URL: ')
    cover = 'cover.png'

    from requests import get
    from shutil import copyfileobj

    chdir(folder)
    with open(cover,'wb') as f, get(url, stream = True) as res:
        copyfileobj(res.raw, f)
    chdir('..')

else:
    cover = input('Cover location: ')
    copy(cover, folder)

# Enter the folder
chdir(folder)

# Setting up file names
video_export = f'videofile {song}.mp4'
thumb_output = f'thumb {song}.png'
video_output = f'video {song}.png'
slowd_output = f'slowed {song}.wav'

# Making the files
from slowedvideos import makeslowed, makevideo, makethumb, exportvideo

makeslowed(audio, 10, slowd_output)
makevideo(cover, song, artist, '(Slowed + Reverb)', video_output)
makethumb(cover, thumb_output)
exportvideo(slowd_output, video_output, video_export)