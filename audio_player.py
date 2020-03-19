import pyaudio
import wave
import sys
from speech_recog.py import detectLanguage
import os
from google.cloud import translate_v2 as translate
import speech_recognition as sr


class AudioFile:
    chunk = 1024

    def __init__(self, file):
        """ Init audio stream """ 
        self.wf = wave.open(file, 'rb')
        self.p = pyaudio.PyAudio()
        self.stream = self.p.open(
            format = self.p.get_format_from_width(self.wf.getsampwidth()),
            channels = self.wf.getnchannels(),
            rate = self.wf.getframerate(),
            output = True
        )

    def play(self):
        """ Play entire file """
        data = self.wf.readframes(self.chunk)
        while data != '':
            self.stream.write(data)
            data = self.wf.readframes(self.chunk)

    def close(self):
        """ Graceful shutdown """ 
        self.stream.close()
        self.p.terminate()

# Usage example for pyaudio
r = sr.Recognizer()
audio = AudioFile("file.wav")
# a.play()
# a.close()
try:
    text = r.recognize_google(audio)
    inputText = "{}".format(text)
    detectLanguage(inputText)
except:
    print("Sorry could not recognize what you said")