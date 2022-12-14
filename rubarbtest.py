import pygame
import os
import subprocess
import time
from time import time as tyme, sleep
import json
from threading import Timer
import threading
#subprocess.call(crop, shell=True)

pygame.init()
pygame.mixer.init()

X = 480
Y = 320

    
screen = pygame.display.set_mode((X, Y))

result = pygame.mixer.music.load("meme.mp3")

A = pygame.image.load("mouth/A.png").convert()
B = pygame.image.load("mouth/B.png").convert()
C = pygame.image.load("mouth/C.png").convert()
D = pygame.image.load("mouth/D.png").convert()
E = pygame.image.load("mouth/E.png").convert()
F = pygame.image.load("mouth/F.png").convert()
G = pygame.image.load("mouth/G.png").convert()
H = pygame.image.load("mouth/H.png").convert()
X = pygame.image.load("mouth/X.png").convert()


#os.system ("/home/se101/rhubarb-lip-sync/rhubarb/rhubarb -o output.json -f json -r pocketSphinx meme.wav")

f = open('output.json')
  
timing = json.load(f)

start = time.time()
music = threading.Thread(target=pygame.mixer.music.play())
music.start()
secs = time.time()
beg = secs
while pygame.mixer.get_busy:
    
    print(secs)
    for i in timing['mouthCues']:
            
        
        while secs -beg < i['start']:
            secs = time.time()
            
            screen.blit(globals().get(i['value']), (0, 0))
            pygame.display.update()
music.join()

f.close()
end = time.time()
pygame.mixer.music.unload()
#os.remove("output.json")