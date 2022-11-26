import speech_recognition as sr
import pyttsx3
import os
import subprocess

import vlc
# for text-to-speech
from gtts import gTTS

# for language model

from playsound import playsound

import threading
import time

# for data
import datetime
import numpy as np

import recording
import responses

import pygame

import pvporcupine

from pvrecorder import PvRecorder

import lights

p = vlc.MediaPlayer("everydaybro.mp4/")
p.set_position(0)

access_key = "KrtyFBDP3S9uW20iiBF0l0QarTeLnJx7hIgT8noopQrXFfqTOCrhTg=="
#keyword_paths = ['/wakeword']
#handle = pvporcupine.create(access_key=access_key, keyword_paths=keyword_paths)
#handle = pvporcupine.create(access_key=access_key, keywords=['picovoice'])



# Building the AI
class ChatBot():
    def __init__(self, name):
        print("----- Starting up", name, "-----")
        self.name = name
        self.awake = False
        self.mood = 1

    def speech_to_text(self):
        recognizer = sr.Recognizer()
        with sr.AudioFile("input.wav") as source:
            audio = recognizer.record(source) 
            self.text="ERROR"
        try:
            self.text = recognizer.recognize_google(audio)
            print("Input  --> ", self.text)
        except:
            print("Input  -->  ERROR")

    def listen(self):
        recognizer = sr.Recognizer()
        with sr.Microphone() as mic:
            print("Say 'Jake Paul'...")
            audio = recognizer.listen(mic)
            self.text="ERROR"
        try:
            self.text = recognizer.recognize_google(audio)
        except:
            self.text="ERROR"



    @staticmethod
    def text_to_speech(text):
        print("Jake Paul --> ", text)
        speaker = gTTS(text=text, lang="en", slow=False)
        speaker.save("res.wav")
        subprocess.run(["rhubarb -o output.json -f --json-r --pocketSphinx res.mp3"])
        statbuf = os.stat("res.wav")
        mbytes = statbuf.st_size / 1024
        duration = mbytes / 200
        result = pygame.mixer.music.load("res.wav")
        pygame.mixer.music.play()
        lights.purple()
        start = time.time()
        print("hello")
        end = time.time()
        print(end - start)
        while pygame.mixer.music.get_busy():
            pygame.time.wait(500)
            screen.blit(open, (0, 0))
            pygame.display.flip()
            pygame.time.wait(500)
            screen.blit(closed, (0, 0))
            pygame.display.flip()
        lights.turnOff()
        screen.blit(m1, (0, 0))
        pygame.mixer.music.unload()
        os.remove("res.wav")

    @staticmethod
    def action_time():
        return datetime.datetime.now().time().strftime('%H:%M')


# Running the AI
if __name__ == "__main__":

    pygame.init()
    pygame.mixer.init()

    X = 480
    Y = 320

    
    screen = pygame.display.set_mode((X, Y))
    m1 = pygame.image.load("mouth/m1.png").convert()
    screen.blit(m1, (0, 0))
    lights.turnOff()
    
    pygame.display.flip()
    pygame.mouse.set_visible(False)

    ai = ChatBot(name="Jake Paul")

    WAKE = "Jake Paul"

    ex=True

    while ex:

        if ai.awake:     

            ai.awake = False  
        
            thread = threading.Thread(target=recording.record)
            lights.blue()
            thread.start()
            thread.join()
            lights.turnOff()
            ai.speech_to_text()

            result = responses.respond(ai.mood, ai.text)
            os.remove("input.wav")
            if result == 0:
                ai.text_to_speech(np.random.choice(["Tata","Have a good day","Bye","Goodbye","Hope to meet soon","peace out!"]))
                ex = False
                break
                  
            elif result == 1:
                rainbow = threading.Thread(target=lights.disco)
                rainbow.start()
                p.play()
                while not "Jake Paul" in ai.text:
                    ai.listen()
                rainbow.join()
                lights.turnOff()
                screen.blit(m1, (0, 0))

            elif result == 2:

                pygame.mixer.music.load("christmas.mp3")
                holiday = threading.Thread(target=lights.holiday)
                holiday.start()
                pygame.mixer.music.play()
                while not "Jake Paul" in ai.text:
                    ai.listen()
                holiday.join()
                lights.Turnoff()
                screen.blit(m1, (0, 0))


                
                
            else: ai.text_to_speech(result)
            
        else: 
            pygame.display.update()
            ai.listen()

        if ai.name in ai.text:
            pygame.mixer.music.load("discord.mp3")
            pygame.mixer.music.play()
            ai.awake = True
    pygame.quit()
    exit()

 

