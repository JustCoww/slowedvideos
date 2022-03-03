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