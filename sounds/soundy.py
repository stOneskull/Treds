import os
import random
import pygame

sounds = [
    sound for sound in os.listdir(os.curdir)
    if sound.endswith('.wav')
]

print(sounds)

#pygame.init()
pygame.mixer.init(48000, -16, 1, 1024)

load = pygame.mixer.Sound
pause = pygame.time.wait

#for sound in sounds:
    #cue = load(sound)
    #cue.play()
    #pause(int(cue.get_length()) * 1000)

for times in range(4):
    sound = random.choice(sounds)
    cue = load(sound)
    print(sound)
    delay = int(cue.get_length()) * 1000 + 222
    cue.play()
    pause(delay)


