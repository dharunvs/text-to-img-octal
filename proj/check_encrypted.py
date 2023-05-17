from PIL import Image
from data import CANVAS_SIZE


def create_points(side_length):
    points = []
    for x in range(side_length):
        for y in range(side_length):
            points.append([x, y])
    return points

def check_encrypted(im=None):
    rgb_im = im.convert('RGB')
    points = create_points(CANVAS_SIZE)
    for point in points:
        rgb = rgb_im.getpixel((point[0], point[1]))
        if(rgb == (0, 0, 0)):
            return True
    return False
