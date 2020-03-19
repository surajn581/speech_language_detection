import os
from google.cloud import translate_v2 as translate
import speech_recognition as sr

def detectLanguage(inputText, target='en'):
    print("Detecting language...")
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r"reactpageagent-jojkmj-ed363b8932c0.json"
    translate_client = translate.Client()
    # result = translate_client.detect_language(inputText)
    result = translate_client.translate(inputText, target_language=target)
    print(result['detectedSourceLanguage'])
		# Language code for German: de


r = sr.Recognizer()
with sr.Microphone() as source:
    print("Speak Anything :")
    audio = r.listen(source)
    print(audio)
    print('audio captured')
    try:
        text = r.recognize_google(audio)
        inputText = "{}".format(text)
        detectLanguage(inputText)
    except:
        print("Sorry could not recognize what you said")