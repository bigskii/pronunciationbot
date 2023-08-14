from gtts import gTTS
from moviepy.editor import *
from simple_youtube_api.Channel import Channel
from simple_youtube_api.LocalVideo import LocalVideo
import PIL


# asks the word and makes it 3x
keyword = input('What word should the video be of? ')
threeword = f"Here is how to pronounce this word. {keyword} {keyword} {keyword}"

# generates tts and loads the file
speed = 0.75
tts = gTTS(text=threeword, slow=True)
tts.save('audio.mp3')
audio = AudioFileClip('audio.mp3')

# create white screen video and set the length to the audio
white_duration = audio.duration
white = ColorClip(size=(1280,720), color=(255,255,255), duration=white_duration)

# create text clip
text = f"How to pronounce {keyword}"
bottomtext = "Subscribe for more pronunciations n whatnot"
textclip = TextClip(text, fontsize=100, color="black", size=(1280,720)).set_duration(white_duration)
bottomtextclip = TextClip(bottomtext, fontsize= 25, color="black", size=(1280,None)).set_duration(white_duration)
bottomtextclip = bottomtextclip.set_position(('center', 'bottom'))
txtheight = bottomtextclip.h
newtextheight = txtheight // 2
bottomtextclip = bottomtextclip.resize(height=newtextheight)

# composite the text and the white
whitetextnobot = CompositeVideoClip([white, textclip.set_position(('center', 'center'))])
whitetext = CompositeVideoClip([whitetextnobot, bottomtextclip])

# add audio
vidaudtxt = whitetext.set_audio(audio)

# export video
path = "video.mp4"
vidaudtxt.write_videofile(path, codec="libx264", fps=24)
