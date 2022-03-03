def buildvideo(song, artist, audiomode, audio, covermode, cover):

    # Importing modules to create and enter the folder
    from os import mkdir, chdir
    from shutil import copy

    folder = f'slowed {song}'
    mkdir(folder)

    if audiomode == 'url':

        from slowedvideos import downloadurl
        chdir(folder)
        downloadurl(audio, 'original')
        chdir('..')
        audio = 'original.wav'

    else:
        copy(audio, folder)

    if covermode == 'url':

        from requests import get
        from shutil import copyfileobj
        chdir(folder)
        with open('cover.png','wb') as f, get(cover, stream = True) as res:
            copyfileobj(res.raw, f)
        chdir('..')
        cover = 'cover.png'

    else:
        copy(cover, folder)

    chdir(folder)

    # Setting up file names
    video_export = f'videofile {song}.mp4'
    thumb_output = f'thumb {song}.png'
    video_output = f'video {song}.png'
    slowd_output = f'slowed {song}.wav'

    # Building the video
    from slowedvideos import makeslowed, makevideo, makethumb, exportvideo
    makeslowed(audio, 10, slowd_output)
    makevideo(cover, song, artist, '(Slowed + Reverb)', video_output)
    makethumb(cover, thumb_output)
    exportvideo(slowd_output, video_output, video_export)