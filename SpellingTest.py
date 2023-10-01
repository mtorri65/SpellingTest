from tkinter import *
from PIL import ImageTk, Image

from curses.ascii import isupper
import signal
from PIL import Image
import simpleaudio as sa
import os

displayImages = True

directory = os.getcwd()
dirImages = directory + '\images'
dirSounds = directory + '\sounds'

words = ['a', 'and', 'the', 'me', 
         'I', 'at', 'fat', 'tap', 
         'map', 'mat', 'it', 'if', 
         'its', 'good', 'in', 'is', 
         'his', 'cat', 'pit']

imagesList = os.listdir(dirImages)

for word in words:
    word_list = list(word)

    if displayImages == True:
        images = []

        image_index = 0
        for letter in word_list:
            if isupper(letter):
                letter = letter + 'cap'
            while image_index < len(imagesList):
                base = os.path.basename(imagesList[image_index])
                imageName = os.path.splitext(base)[0]
                imageExt = os.path.splitext(base)[1]
                if letter == imageName:
                    pathImage = dirImages + '\\' + letter + imageExt
                    imageOpened = Image.open(dirImages + '\\' + letter + imageExt)
                    imageOpened_resized = imageOpened.resize((200, 200))
                    images.append(imageOpened_resized)
                    image_index = 0
                    break
                image_index += 1

        new_image = Image.new('RGB',(len(images)*images[0].size[0], images[0].size[1]), (250,250,250))
        new_image.paste(images[0],(0,0))
        for i in range(1, len(images)):
            new_image.paste(images[i], (i*images[i].size[0], 0))

        new_image.show()

    sound1 = dirSounds + '\\' + word + '.wav' 
    wave_obj = sa.WaveObject.from_wave_file(sound1)
    play_obj = wave_obj.play()
    play_obj.wait_done()

    input('Press Enter!')