from PIL import Image, ImageDraw
from main import text_to_octal
from data import *
from junk import addjunk
import random


canvas = (CANVAS_SIZE, CANVAS_SIZE)
box_size = BOX_SIZE
colors = COLORS

def encrypt(file):
    with open(file, "r") as f:
        num = f.read()

    num = text_to_octal(num)
    num , _ = addjunk(num)

    im = Image.new('RGBA', canvas, (255, 255, 255, 255))
    draw = ImageDraw.Draw(im)

    x=y=a=0

    for i in num:
        draw.rectangle([(x, y), (x+box_size, y+box_size)], fill=colors[i])
        x+=box_size
        a+=1
        if a>= canvas[0]/box_size:
            a=0
            y+=box_size
            x=0

    with open("key", "w") as f:
        f.write(str(len(num)))

    # im.thumbnail(thumb)

    file = file.split(".")
    im.save(f"./{file[0]}.png")


def encrypt_fake(file):
    with open(file, "r") as f:
        num = f.read()

    num = text_to_octal(num)
    num , _ = addjunk(num, True)

    im = Image.new('RGBA', canvas, (255, 255, 255, 255))
    draw = ImageDraw.Draw(im)


    for j in range(1, 11):
        x=y=a=0
        num = list(num)
        random.shuffle(num)
        num = "".join(num)
        print(num)
        for i in num:
            draw.rectangle([(x, y), (x+box_size, y+box_size)], fill=colors[i])
            x+=box_size
            a+=1
            if a>= canvas[0]/box_size:
                a=0
                y+=box_size
                x=0

        with open("key", "w") as f:
            f.write(str(len(num)))

        # im.thumbnail(thumb)

        fn= file.split(".")
        im.save(f"./fake/{fn[0]}{j}.png")

encrypt_fake("test.txt")
encrypt("test.txt")
