# To install necessary modules, run 'pip install -r <path to requirements.txt>'
import googletrans as gtrans
import speech_recognition as sr
import gtts as tts
import playsound as play

# print(gtrans.LANGUAGES)

recognizer = sr.Recognizer()

with sr.Microphone() as source:
    print("Speak Now!")
    voice = recognizer.listen(source)
    text = recognizer.recognize_google(voice, language="en") # Change language code for input language (to see codes, run line 7)

    print(text)

translator = gtrans.Translator()
translation = translator.translate(text, dest="ru") # Change language code for output language (to see codes, run line 7)
print(translation.text)

converted_audio = tts.gTTS(translation.text, lang="ru") # Change language code for output language (to see codes, run line 7)
converted_audio.save("translated.mp3")
play.playsound("translated.mp3")
