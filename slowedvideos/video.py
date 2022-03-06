def makethumb(cover, output):

    prefix = 'Thumbnail -'

    from PIL import Image, ImageDraw, ImageEnhance, ImageFilter 
    from math import trunc

    # Sizes
    x, y = (626, 626) # Cover size
    X, Y = (1920, 1080) # Background size
    
    # Get the middle coordinates of the image
    middle = (trunc((X-x)/2), trunc((Y-y)/2))
    
    # Import cover
    print(prefix, f'Importing {cover} ...')
    tb = Image.open(cover)
    cv = Image.open(cover)

    # Resizing
    print(prefix, 'Resizing cover and background...')
    cv = cv.resize((x, y))
    tb = tb.resize((X, Y))
    
    # Add a shadow (Black square with blur)
    print(prefix, 'Creating the shadow...')
    square = Image.new(mode = "RGBA", size = (x, y), color = (0, 0, 0))
    tb.paste(square, middle)

    # Blur and turn brightness down
    print(prefix, 'Adding blur to background...')
    tb = ImageEnhance.Brightness(tb).enhance(0.4)
    tb = tb.filter(ImageFilter.GaussianBlur(25))

    # Paste cover into the background
    print(prefix, 'Merging cover with background...')
    tb.paste(cv, middle)
    
    # Export final thing to a file
    print(prefix, f'Exporting thumbnail as {output} ...')
    tb.save(output)
    
    return print(prefix, 'Done')

def makevideo(cover, song, artist, toptext, output):

    prefix = 'Make Video -'

    from PIL import Image, ImageDraw, ImageFont, ImageEnhance, ImageFilter
    from importlib import resources
    from math import trunc
    import io

    x, y = (2500, 2500) # Cover size
    X, Y = (7680, 4320) # Background size

    # Import cover
    print(prefix, f'Importing {cover} ...')
    bg = Image.open(cover)
    cv = Image.open(cover)

    # Resizing
    print(prefix, 'Resizing cover and background...')
    cv = cv.resize((x, y))
    bg = bg.resize((X, Y))

    # Add a shadow (Black square with blur)
    print(prefix, 'Creating the shadow...')
    square = Image.new(mode = "RGBA", size = (2500, 2500), color = (0, 0, 0))
    bg.paste(square, (trunc((X-x)/2), 659))

    # Blur and turn brightness down
    print(prefix, 'Adding blur to background...')
    bg = ImageEnhance.Brightness(bg).enhance(0.4)
    bg = bg.filter(ImageFilter.GaussianBlur(120))

    # Paste cover into the background
    print(prefix, 'Merging cover with background')
    bg.paste(cv, ( trunc((X-x)/2 ), 659))


    ### Text
    text = ImageDraw.Draw(bg)

    # Layout is [text, y-coordinates (from top), font, font-size]
    toptext = [toptext, 300, 'toptext_font.ttf', 250]
    song = [song, 3240, 'down1_font.ttf', 279]
    artist = [artist, 3640, 'down2_font.ttf', 186]

    # Generate the text
    for i in [toptext, song, artist]:

        # Get font from module subfolder "makeimages"
        with resources.open_binary('slowedvideos.fonts', i[2]) as font:
            font = io.BytesIO(font.read())
        
        print(prefix, f'Writing "{i[0]}" with "{i[2]}" font')
        font = ImageFont.truetype(font, i[3])
        x, y = text.textsize(i[0], font=font)
        text.text(((X-x)/2, i[1]), i[0], fill=(255, 255, 255), font=font, align='center')

    # Export final thing to a file
    print(prefix, f'Exporting file as {output} ...')
    bg.save(output)

    return print(prefix, 'Done')

def exportvideo(audio, img, output):
    
    prefix = 'Export Video -'

    from moviepy.editor import AudioFileClip, ImageClip

    # Import files
    print(prefix, f'Importing {audio}, {img} ...')
    audio = AudioFileClip(audio)
    img = ImageClip(img)
    
    # Mix into video
    print(prefix, 'Setting audio...')
    video = img.set_audio(audio)
    print(prefix, 'Setting video duration...')
    video.duration = audio.duration
    print(prefix, 'Setting video at 1 fps...')
    video.fps = 1
    print(prefix, f'Exporting {output}...')
    video.write_videofile(output)

    return print(prefix, 'Done')

def buildvideo(song, artist, audiomode, audio, covermode, cover, speed):

    # Importing modules to create and enter the folder
    from os import mkdir, chdir
    from shutil import copy

    folder = f'slowed {song}'
    mkdir(folder)

    if audiomode == 'url':

        from slowedvideos.audio import downloadurl
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
    from slowedvideos.audio import makeslowed
    from slowedvideos.video import makevideo, makethumb, exportvideo
    makeslowed(audio, speed, slowd_output)
    makevideo(cover, song, artist, '(Slowed + Reverb)', video_output)
    makethumb(cover, thumb_output)
    exportvideo(slowd_output, video_output, video_export)

    chdir('..')