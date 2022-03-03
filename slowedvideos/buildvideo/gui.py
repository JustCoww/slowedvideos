def gui():

    from tkinter import Tk, Label, Entry, Button

    root = Tk()
    root.title("Video maker")
    root.geometry('350x200')

    audiomode_status = False
    covermode_status = False
    audiomode = 'url'
    covermode = 'url'

    def toggle_audio():

        global audiomode_status
        global audiomode

        if audiomode_status:
            audiomode_button.config(text = 'On')
            audiomode = 'url'
            audiomode_text.config(text = f'Audio mode is: {audiomode}')
            audiomode_status = False
        else:
            audiomode_button.config(text = 'Off')
            audiomode = 'file'
            audiomode_text.config(text = f'Audio mode is: {audiomode}')
            audiomode_status = True

    def toggle_cover():

        global covermode_status
        global covermode

        if covermode_status:
            covermode_button.config(text = 'On')
            covermode = 'url'
            covermode_text.config(text = f'Cover mode is: {covermode} ')
            covermode_status = False
        else:
            covermode_button.config(text = 'Off')
            covermode = 'file'
            covermode_text.config(text = f'Cover mode is: {covermode} ')
            covermode_status = True

    blank = Label(root)
    blank.grid(column=0, row=0) 

    # Audio
    audio_text = Label(root, text='Audio')
    audio_text.grid(column=0, row=1)
    audio_text_input = Entry(root, width=30)
    audio_text_input.grid(column=1, row=1)
    audiomode_button = Button(text = 'On', width=5, command=toggle_audio)
    audiomode_button.grid(column=3, row=1)
    audiomode_text = Label(root, width=20, text=f'Audio mode is: {audiomode}')
    audiomode_text.grid(column=2, row=1)

    blank = Label(root)
    blank.grid(column=0, row=2)

    # Cover
    cover_text = Label(root, text='Cover')
    cover_text.grid(column=0, row=3)
    cover_text_input = Entry(root, width=30)
    cover_text_input.grid(column=1, row=3)
    covermode_button = Button(text = 'On', width=5, command=toggle_cover)
    covermode_button.grid(column=3, row=3)
    covermode_text = Label(root, width=20, text=f'Cover mode is: {covermode}')
    covermode_text.grid(column=2, row=3)

    blank = Label(root)
    blank.grid(column=0, row=4)

    # Song
    song_text = Label(root, text='Song')
    song_text.grid(column=0, row=5)
    song_text_input = Entry(root,width=30)
    song_text_input.grid(column=1, row=5)

    blank = Label(root)
    blank.grid(column=0, row=6)

    # Artist
    artist_text = Label(root, text='Artist')
    artist_text.grid(column=0, row=7)
    artist_text_input = Entry(root, width=30)
    artist_text_input.grid(column=1, row=7)

    def build():

        global audiomode
        global covermode

        from buildvideo import buildvideo

        audio = audio_text_input.get()
        cover = cover_text_input.get()
        artist = artist_text_input.get()
        song = song_text_input.get()

        buildvideo(song, artist, audiomode, audio, covermode, cover)

    blank = Label(root)
    blank.grid(column=0, row=8)

    # Build
    build_button = Button(root, text="Build", command=build)
    build_button.grid(column=0, row=9)
    build_text = Label(root, text='Click here after inserting all the things.')
    build_text.grid(column=1, row=9)

    root.mainloop()