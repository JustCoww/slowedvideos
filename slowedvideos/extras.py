def buildvideo(song, artist, audiomode, audio, covermode, cover, toptext, exportmode, speed):

    # Importing modules
    from slowedvideos.video import makevideo, makethumb, exportvideo
    from slowedvideos.audio import makeslowed, downloadurl
    from os import mkdir, chdir, system, remove
    from multiprocessing import Process
    from shutil import copyfileobj
    from requests import get
    from shutil import copy
    from time import sleep

    # Setting up file names
    video_export = f'videofile {song}.mp4'
    thumb_output = f'thumb {song}.png'
    video_output = f'video {song}.png'
    slowd_output = f'slowed {song}.mp3'
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
    temp_slowd_output = slowd_output + '.wav'
    slow_cmd = Process(target=makeslowed, args=[audio, speed, temp_slowd_output])
    mkthumb_cmd = Process(target=makethumb, args=[cover, thumb_output])

    slow_cmd.start()
    mkthumb_cmd.start()
    system(f'ffmpeg -i "{temp_slowd_output}" -vn -ar 44100 -ac 2 -b:a 320k "{slowd_output}"')
    remove(temp_slowd_output)
    makevideo(cover, song, artist, toptext, video_output)
    exportvideo(slowd_output, video_output, exportmode, video_export)

    chdir('..')
