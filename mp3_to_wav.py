from os import path
from pydub import AudioSegment

# files                                                                         
src = "aganda.mp3"
dst = "aganda.wav"

# convert wav to mp3                                                            
sound = AudioSegment.from_mp3(src)
sound.export(dst, format="wav")

# import subprocess
# subprocess.call(['ffmpeg', '-i', 'aganda.mp3',
#                    'aganda.wav'])