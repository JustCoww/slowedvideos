def makethumb(cover, output):

    prefix = 'Thumbnail -'

    from PIL import Image, ImageDraw, ImageEnhance, ImageFilter 
    from math import trunc

    # Import
    print(prefix, f'Importing {cover} ...')
    tb = Image.open(cover)
    cv = Image.open(cover)

    # Cover
    print(prefix, 'Resizing cover...')
    x, y = (626, 626)
    cv = cv.resize((x, y), resample=0, box=None)
    
    # Thumb Resize
    print(prefix, 'Resizing background...')
    X, Y = (1920, 1080)
    tb = tb.resize((X, Y), resample=0, box=None)
    
    # Blur and brightness
    print(prefix, 'Bluring background...')
    tb = ImageEnhance.Brightness(tb).enhance(0.3)
    tb = tb.filter(ImageFilter.GaussianBlur(60))
    tb = tb.copy()

    # Mix into file
    print(prefix, 'Merging cover to background...')
    center = (trunc((X-x)/2), trunc((Y-y)/2))
    tb.paste(cv, center)
    print(prefix, f'Exporting thumbnail as {output} ...')
    tb.save(output)
    
    return print(prefix, 'Done')