from tkinter import *
from PIL import ImageTk, Image
import simpleaudio as sa
from curses.ascii import isupper
import signal
import os



root = Tk()
root.title("Learn To Code at Codemy.com")
#root.iconbitmap('Graphicloads-Flat-Finance-Global.ico')

#my_img1 = ImageTk.PhotoImage(Image.open("images/a.jpg"))
#my_img2 = ImageTk.PhotoImage(Image.open("images/b.jpg"))
#my_img3 = ImageTk.PhotoImage(Image.open("images/c.jpg"))
#my_img4 = ImageTk.PhotoImage(Image.open("images/d.jpg"))
#my_img5 = ImageTk.PhotoImage(Image.open("images/e.jpg"))

#image_list = [my_img1, my_img2, my_img3, my_img4, my_img5]
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

word_list = list(words[0])

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

my_label = Label(image=new_image)
my_label.grid(row=0, column=0, columnspan=3)
sound1 = 'sounds/and.wav' 
wave_obj = sa.WaveObject.from_wave_file(sound1)
play_obj = wave_obj.play()
#play_obj.wait_done()

def forward(image_number):
    global my_label
    global button_forward
    global button_back

    my_label.grid_forget()
    my_label = Label(image=image_list[image_number-1])

    sound1 = 'sounds/and.wav' 
    wave_obj = sa.WaveObject.from_wave_file(sound1)
    play_obj = wave_obj.play()
#    play_obj.wait_done()

    button_forward = Button(root, text=">>", command=lambda: forward(image_number+1))
    button_back = Button(root, text="<<", command=lambda: back(image_number-1))

    if image_number == 5:
        button_forward = Button(root, text=">>", state=DISABLED)

    my_label.grid(row=0, column=0, columnspan=3)
    button_back.grid(row=1, column=0)
    button_forward.grid(row=1, column=2)

def back(image_number):
    global my_label
    global button_forward
    global button_back

    my_label.grid_forget()
    my_label = Label(image=image_list[image_number-1])
    button_forward = Button(root, text=">>", command=lambda: forward(image_number+1))
    button_back = Button(root, text="<<", command=lambda: back(image_number-1))

    if image_number == 1:
        button_back = Button(root, text="<<", state=DISABLED)

    my_label.grid(row=0, column=0, columnspan=3)
    button_back.grid(row=1, column=0)
    button_forward.grid(row=1, column=2)


button_back = Button(root, text="<<", command=back, state=DISABLED)
button_exit = Button(root, text="EXIT PROGRAM", command=root.quit)
button_forward = Button(root, text=">>", command=lambda: forward(2))

button_back.grid(row=1, column=0)
button_exit.grid(row=1, column=1)
button_forward.grid(row=1, column=2)


root.mainloop()