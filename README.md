# Slowed Videos Scripts

Various scritps from justcow.


# Install
```sh
pip install slowedvideos
```


# Dependencies

You will need to have ffmpeg in your **PATH** for the "**downloadurl**" to work.


**Arch Based**
```sh
sudo pacman -S ffmpeg
```
  
  
**Debian Based**
```sh
sudo apt install ffmpeg
```
  
  
**Other**

Just install ffmpeg and make it availabe in your **PATH**.


# Examples


**Downloading audio from soundcloud**
```python
from slowedvideos.audio import downloadurl

# Variables
url = 'https://soundcloud.com/100gecs/gecgecgec-remix-feat-lil-west-and-tony-velour'
output = 'downloaded' # It will download as .wav 

downloadurl(url, output)
```
https://soundcloud.com/100gecs/gecgecgec-remix-feat-lil-west-and-tony-velour


**Slowing and adding reverb to the downloaded audio**
```python
from slowedvideos.audio import makeslowed

# Variables
audio = 'downloaded.wav'
speed = 10 # This changes how slow the audio will be
output = 'slowed gecgecgec (Remix).wav'

makeslowed(audio, speed, output)
```
https://soundcloud.com/justcoww/slowed-gecgecgec-remix


**Creating the video image**
```python
from slowedvideos.video import makevideo

# Variables
cover = 'cover.png'
song = 'gecgecgec (Remix)'
artist = '100 gecs'
toptext = '(Slowed + Reverb)'
video_output = 'video gecgecgec (Remix).png'

makevideo(cover, song, artist, toptext, video_output)
```
![video gecgecgec (Remix)](https://user-images.githubusercontent.com/68345611/158817334-633d7128-5b70-43a1-8140-67e22bc523f1.png)


**Creating the thumbnail image**
```python
from slowedvideos.video import makethumb

# Variables
cover = 'cover.png'
thumb_output = 'thumb gecgecgec (Remix).png'

makethumb(cover, thumb_output)
```
![thumb gecgecgec (Remix)](https://user-images.githubusercontent.com/68345611/158817432-3340c16c-4e8b-49fb-8630-ce43d72ef7a8.png)


**Exporting the video**
```python
from slowedvideos.video import exportvideo

# Variables
audio = 'slowed gecgecgec (Remix).wav'
image = 'video gecgecgec (Remix).png'
output = 'videofile gecgecgec (Remix).mp4'

exportvideo(audio, image, output)
```
https://user-images.githubusercontent.com/68345611/158817541-f0fe9117-b1c7-48fb-9aae-47d99a38b790.mp4
