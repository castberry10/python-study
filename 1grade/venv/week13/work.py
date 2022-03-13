from PIL import Image

def pandan(p):
    r,g,b,a, = p
    if r % 2 == 1:
        return True
    else:
        return False

def bw(im):
    w,h = im.size
    for y in range(h):
        for x in range(w):

            if(pandan(im.getpixel((x, y)))):
                im.putpixel((x, y), (255, 255, 255, 255))
            else:
                im.putpixel((x, y), (0, 0, 0, 255))

im = Image.open("hidden.png")
bw(im)
im.show()