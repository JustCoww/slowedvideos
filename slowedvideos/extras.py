def buildvideo(song, artist, audiomode, audio, covermode, cover, toptext, exportmode, speed):

    # Importing modules
    from slowedvideos.video import makevideo, makethumb, exportvideo
    from slowedvideos.audio import makeslowed, downloadurl
    from multiprocessing import Process
    from shutil import copyfileobj
    from os import mkdir, chdir
    from requests import get
    from shutil import copy
    from time import sleep

    # Setting up file names
    video_export = f'videofile {song}.mov'
    thumb_output = f'thumb {song}.png'
    video_output = f'video {song}.png'
    slowd_output = f'slowed {song}.wav'
    folder = f'slowed {song}'
    mkdir(folder)

    if audiomode == 'url':

        chdir(folder)
        downloadurl(audio, 'original')
        chdir('..')
        audio = 'original.wav'

    else:
        copy(audio, folder)

    if covermode == 'url':

        chdir(folder)
        with open("cover.png", "wb") as f:
            with get(cover) as r:
                f.write(r.content)
        chdir('..')
        cover = 'cover.png'

    else:
        copy(cover, folder)

    chdir(folder)

    # Building the video
    slow_cmd = Process(target=makeslowed, args=[audio, speed, slowd_output])
    mkthumb_cmd = Process(target=makethumb, args=[cover, thumb_output])

    slow_cmd.start()
    mkthumb_cmd.start()
    makevideo(cover, song, artist, toptext, video_output)
    exportvideo(slowd_output, video_output, exportmode, video_export)

    chdir('..')
