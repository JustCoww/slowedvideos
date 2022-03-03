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
