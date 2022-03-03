def downloadurl(url, output):

    prefix = 'Download URL -'

    from youtube_dl import YoutubeDL

    output = output + '.mp3'
    
    # Set opts
    print(prefix, 'Setting opts...')
    ytdl_opts = { 'format': 'bestaudio/best', 'outtmpl':output, 'postprocessors':[{'key': 'FFmpegExtractAudio','preferredcodec': 'wav'}] }
    print(prefix, ytdl_opts)
    
    # Download video
    print(prefix, 'Downloading audio...')
    YoutubeDL(ytdl_opts).download([url])

    return print(prefix, 'Done')
