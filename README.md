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


**Download URL**
```python
from slowedvideos.audio import downloadurl

# Variables
url = 'https://soundcloud.com/trink3tofficial/trink3tofficial-sunrise-prod-plxce'
output = 'downloaded' # It will download as .wav 

downloadurl(url, output)
```
https://soundcloud.com/user-544064018/downloadedwav


**Make Slowed**
```python
from slowedvideos.audio import makeslowed

# Variables
audio = 'downloaded.wav'
howslow = 10 # This changes how slow the audio will be
output = 'slowed sunrise.wav'

makeslowed(audio, howslow, output)
```
https://soundcloud.com/user-544064018/slowed-sunrisewav


**Make Video Image**
```python
from slowedvideos.video import makevideo

# Variables
cover = 'sunrise.jpg'
song = 'sunrise'
artist = 'Kid Trink'
toptext = '(Slowed + Reverb)'
video_output = 'video sunrise.png'

makevideo(cover, song, artist, toptext, video_output)
```
![video sunrise](https://user-images.githubusercontent.com/68345611/156537825-23bf7b0a-b106-4223-95f3-f7309185a836.png)


**Make Thumb Image**
```python
from slowedvideos.video import makethumb

# Variables
cover = 'sunrise.jpg'
thumb_output = 'thumb sunrise.png'

makethumb(cover, thumb_output)
```
![thumb sunrise](https://user-images.githubusercontent.com/68345611/156541806-1d7ccdcf-fc5f-43db-9309-af23147baba8.png)


**Export Video**
```python
from slowedvideos.video import exportvideo

# Variables
audio = 'slowed sunrise.wav'
image = 'video sunrise.png'
output = 'videofile sunrise.mp4'

exportvideo(audio, image, output)
```
https://user-images.githubusercontent.com/68345611/156537554-da514beb-b470-4685-976a-71817961e4cd.mp4
