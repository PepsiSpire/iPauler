import pyttsx3
import speech_recognition as sr

import time
import os
import sys
import pygame.display

import pygame


pygame.init()
pygame.display.init()

X = 480
Y = 320

scrn = pygame.display.set_mode((X, Y))


run = True
imp = pygame.image.load("boxer.jpg").convert()
scrn.blit(imp, (0, 0))
pygame.display.flip()
while (run):
 
  # iterate over the list of Event objects
  # that was returned by pygame.event.get() method.
    for i in pygame.event.get():
 
        # if event object type is QUIT
        # then quitting the pygame
        # and program both.
        if i.type == pygame.QUIT:
            status = False
 
    
pygame.quit()
