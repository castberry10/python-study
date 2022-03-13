from PIL import Image
import math

thresh_ = 30

def dis_color(c1, c2):
    r1, g1, b1 = c1
    r2, g2, b2 = c2
    return math.sqrt((r1 - r2) ** 2 + (g1 - g2) ** 2 + (b1 - b2) ** 2)

def background(im, backim):
    w,h = im.size
    key = im.getpixel((10, 10))
    for y in range(h):
        for x in range(w):
            p = im.getpixel((x, y))
            if(dis_color(p , key) < thresh_):
                pass
            else:
                backim.putpixel((x + 300,y), im.getpixel((x,y)))

backim = Image.open("background.jpg")
im = Image.open("person.jpg")

background(im, backim)
backim.show()
# for y in range(h):
#     for x in range(w):