def makethumb(cover, output):

    prefix = '[Thumbnail PNG]'

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
    
    # Create a rounded cornered square mask for the rounded cover
    rad = 45
    circle = Image.new('L', (rad * 2, rad * 2), 0)
    draw = ImageDraw.Draw(circle)
    draw.ellipse((0, 0, rad * 2, rad * 2), fill=255)
    rounded_mask = Image.new('L', (x, y), "white")
    rounded_mask.paste(circle.crop((0, 0, rad, rad)), (0, 0))
    rounded_mask.paste(circle.crop((0, rad, rad, rad * 2)), (0, y - rad))
    rounded_mask.paste(circle.crop((rad, 0, rad * 2, rad)), (x - rad, 0))
    rounded_mask.paste(circle.crop((rad, rad, rad * 2, rad * 2)), (x - rad, y - rad))
    
    # Add a shadow (Black square with blur)
    print(prefix, 'Creating the shadow...')
    square = Image.new(mode = "RGBA", size = (x, y), color = 'black')
    tb.paste(square, middle, rounded_mask)

    # Blur and turn brightness down
    print(prefix, 'Adding blur to background...')
    tb = ImageEnhance.Brightness(tb).enhance(0.4)
    tb = tb.filter(ImageFilter.GaussianBlur(25))

    # Paste cover into the background
    print(prefix, 'Merging cover with background...')
    tb.paste(cv, middle, rounded_mask)
    
    # Export final thing to a file
    print(prefix, f'Exporting thumbnail as {output} ...')
    tb.save(output)
    
    return print(prefix, 'Done')

def makevideo(cover, song, artist, toptext, output):

    prefix = '[Video PNG]'

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

    # Create a rounded cornered square mask for the rounded cover
    rad = 100
    circle = Image.new('L', (rad * 2, rad * 2), 0)
    draw = ImageDraw.Draw(circle)
    draw.ellipse((0, 0, rad * 2, rad * 2), fill=255)
    rounded_mask = Image.new('L', (x, y), "white")
    rounded_mask.paste(circle.crop((0, 0, rad, rad)), (0, 0))
    rounded_mask.paste(circle.crop((0, rad, rad, rad * 2)), (0, y - rad))
    rounded_mask.paste(circle.crop((rad, 0, rad * 2, rad)), (x - rad, 0))
    rounded_mask.paste(circle.crop((rad, rad, rad * 2, rad * 2)), (x - rad, y - rad))

    # Add a shadow (Black square with blur)
    print(prefix, 'Creating the shadow...')
    square = Image.new(mode = "RGBA", size = (2500, 2500), color = 'black')
    bg.paste(square, (trunc((X-x)/2), 659), rounded_mask)

    # Blur and turn brightness down
    print(prefix, 'Adding blur to background...')
    bg = ImageEnhance.Brightness(bg).enhance(0.4)
    bg = bg.filter(ImageFilter.GaussianBlur(120))

    # Paste cover into the background
    print(prefix, 'Merging cover with background')
    bg.paste(cv, ( trunc((X-x)/2 ), 659), rounded_mask)


    ### Text
    text = ImageDraw.Draw(bg)

    # Layout is [text, y-coordinates (from top), font, font-size]
    toptext = [toptext, 300, 'toptext_font.ttf', 250]
    song = [song, 3250, 'down1_font.ttf', 279]
    artist = [artist, 3640, 'down2_font.ttf', 186]

    # Generate the text
    for i in [toptext, song, artist]:

        # Get font from module subfolder "makeimages"
        with resources.open_binary('slowedvideos.fonts', i[2]) as font:
            font = io.BytesIO(font.read())
        
        print(prefix, f'Writing "{i[0]}" with "{i[2]}" font')
        font = ImageFont.truetype(font, i[3])
        x, y = text.textsize(i[0], font=font)
        text.text(((X-x)/2, i[1]), i[0], fill='white', font=font, align='center')

    # Export final thing to a file
    print(prefix, f'Exporting file as {output} ...')
    bg.save(output)

    return print(prefix, 'Done')

def exportvideo(audio, img, mode, output):
    
    prefix = '[Export MP4]'

    if 'moviepy' in mode:

        prefix = '[Export MP4 (MOVIEPY)]'

        from moviepy.editor import AudioFileClip, ImageClip
        print(prefix, 'Starting to export video with "MOVIEPY"')

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

    elif 'ffmpeg' in mode:
        
        prefix = '[Export MP4 (FFMPEG)]'
        
        from os import system, remove
        
        print(prefix, 'Starting to export video with "FFMPEG"')
        
        export_cmd = system(f'''ffmpeg -loop 1 -framerate 1 -i "{img}" -i "{audio}" -c copy -shortest "{output}.mkv"''')
        if export_cmd == 0:
            print(prefix, 'Export ran sucessfully')
            convert_cmd = system(f'''ffmpeg -i "{output}.mkv" "{output}"''')
            if convert_cmd == 0:
                print(prefix, 'Convertion ran sucessfully')
                remove(f'{output}.mkv')
            else:
                print(prefix, f'Error occured in convertion: {convert_cmd}')
        else:
            print(prefix, f'Error occured in download: {export_cmd}')

    else:
        
        print(prefix, 'Invalid export mode.')

    return print(prefix, 'Done')
