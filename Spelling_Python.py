import pygame
from gtts import gTTS
import json
from random import randint
import os

def play_sound(filename):
    pygame.mixer.music.load(filename)
    pygame.mixer.music.set_volume(0.7)
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

with open('dictionary.json', 'r') as file:
    my_dict = json.load(file)

def generate_speech_files(word, defenition):
    pygame.mixer.music.stop()
    pygame.mixer.music.unload()

    wordSound = gTTS(word, lang='en', tld='com')
    wordSound.save('WordSound.mp3')

    defenitionSound = gTTS(defenition, lang='en', tld='com')
    defenitionSound.save('DefSound.mp3')

pygame.init()

playing = True
while (playing):
    keys = list(my_dict.keys())
    randomIndex = randint(0, len(keys) - 1)
    randomWord = (keys[randomIndex])
    randomWordDefenition = my_dict[randomWord]
    generate_speech_files(randomWord, randomWordDefenition)
    opt = 0

    while (opt != "3"):
        print("\n1. Hear Word\n2. Hear Defenition\n3. Exit\n")
        opt = str(input("Enter option or spell word: "))

        if (opt == "1"):
            play_sound('WordSound.mp3')
        elif (opt == "2"):
            play_sound('DefSound.mp3')
        elif (opt == "3"):
            break
        else:
            if (opt.lower() == randomWord.lower()):
                print("You Win")
                opt = "3"
                again = input("Would you like to play again? (y/n): ")
            else:
                print("you lose, better luck next time!")
                print(f"The word is {randomWord}")
                opt = "3"
                again = input("Would you like to play again? (y/n): ")

            if (again == 'y'):
                playing = True

            else:
                playing = False

pygame.quit()

os.remove('WordSound.mp3')
os.remove('DefSound.mp3')