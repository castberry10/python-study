from PIL import Image

def depixel(im, im2):
    w,h = im.size
    key = im.getpixel((10, 10))
    for y in range(h):
        for x in range(w):
            r1, g1, b1 = im.getpixel((x, y))
            r2, g2, b2 = im2.getpixel((x, y))
            if r2 - r1 < 0:
                r3 = r2 - r1 + 255
            else:
                r3 = r2 - r1

            if g2 - g1 < 0:
                g3 = g2 - g1 + 255
            else:
                g3 = g2 - g1

            if b2 - b1 < 0:
                b3 = b2 - b1 + 255
            else:
                b3 = b2 - b1

            im2.putpixel((x, y), (r3, g3, b3))

im = Image.open("pic1.jpg")
im2 = Image.open("result.jpg")

depixel(im, im2)
im2.show()