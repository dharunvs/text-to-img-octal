from PIL import Image
from data import *
from main import octal_to_text
from predict import predict_color
from check_encrypted import check_encrypted
from junk import removejunk

canvas = (CANVAS_SIZE, CANVAS_SIZE)
box_size = BOX_SIZE

def decrypt(key, im):

    with open(key, "r") as f:
        num = int(f.read())

    im = Image.open(im)
    rgb_im = im.convert('RGB')

    if check_encrypted(im):
        li = []
        x=y=a=0

        for i in range(num):
            rgb = rgb_im.getpixel((x, y))
            li.append(rgb)
            
            x+=box_size
            a+=1
            if a>= canvas[0]/box_size:
                a=0
                y+=box_size
                x=0

        colors_li = []
        for rgb in li:
            color = predict_color(rgb[0], rgb[1], rgb[2])
            colors_li.append(color)


        text = ""

        for i in colors_li:
            text += NUMS[i]

        text = removejunk(text)
        decrypted = octal_to_text(text)

        with open("decrypted.txt", "w") as f:
            f.write(decrypted)

        return(decrypted)
    
    return False

print(decrypt("key", "test.png"))