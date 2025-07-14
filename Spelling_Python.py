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

def generate_speech_files(word, definition):
    pygame.mixer.music.stop()
    pygame.mixer.music.unload()

    wordSound = gTTS(word, lang='en', tld='com')
    wordSound.save('WordSound.mp3')

    definitionSound = gTTS(definition, lang='en', tld='com')
    definitionSound.save('DefSound.mp3')

with open("score.txt", "r") as file:
    score = int(file.readline())

pygame.init()

playing = True
while (playing):
    keys = list(my_dict.keys())
    randomIndex = randint(0, len(keys) - 1)
    randomWord = (keys[randomIndex])
    randomWordDefinition = my_dict[randomWord]
    generate_speech_files(randomWord, randomWordDefinition)
    opt = 0

    with open("word_history.txt", "a") as file:
        file.write(f"\n{randomWord}")

    while (opt != "4"):
        print("\n1. Hear Word\n2. Hear definition\n3. See score\n4. Exit\n")
        opt = str(input("Enter option or spell word: "))

        if (opt == "1"):
            play_sound('WordSound.mp3')
            os.system('cls')
        elif (opt == "2"):
            play_sound('DefSound.mp3')
            os.system('cls')
        elif (opt == "3"):
            print(f"Score: {score}")
        elif (opt == "4"):
            playing = False
        else:
            if (opt.lower() == randomWord.lower()):
                print("You Win")
                opt = "4"
                score += 1
                again = input("Would you like to play again? (y/n): ")
                os.system('cls')
            else:
                print("you lose, better luck next time!")
                print(f"The word is {randomWord}")
                opt = "4"
                again = input("Would you like to play again? (y/n): ")
                os.system('cls')

            if (again == 'y'):
                playing = True

            else:
                playing = False

with open("score.txt", "w") as file:
    file.write(str(score))

pygame.quit()
os.remove('WordSound.mp3')
os.remove('DefSound.mp3')
