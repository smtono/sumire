"""
Text to speech
"""

import os
import pyttsx3

def tts(text: str):
    engine = pyttsx3.init()

    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)

    engine.save_to_file(text, os.path.join(os.getcwd(), "src", "data", "output", "output.mp3"))
    engine.runAndWait()

if __name__ == "__main__":
    text = "Hello World!"
    tts(text)
