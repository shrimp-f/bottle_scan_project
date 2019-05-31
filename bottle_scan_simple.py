import cv2
import glob
from PIL import Image
import time
import sys

print(cv2.__version__)#openCV 4.1.0で動作確認

def get_concat_h(im1, im2):
    dst = Image.new('RGB', (im1.width + im2.width, im1.height))
    dst.paste(im1, (0, 0))
    dst.paste(im2, (im1.width, 0))
    return dst


if __name__ == "__main__":

    input_images = glob.glob('images_hi/*.jpg')
    print(input_images)

    im1 = Image.open(str(input_images[0]))
    w, h = im1.size
    if w>h:#横長の時
        im1 = im1.rotate(-90, expand=True)
    w, h = im1.size
    im1_crop = im1.crop((w/2-25,0,w/2+25,2304))

    im2 = Image.open(str(input_images[1]))
    w, h = im2.size
    if w>h:#横長の時
        im2 = im2.rotate(-90, expand=True)
    w, h = im2.size
    im2_crop = im2.crop((w/2-25,0,w/2+25,2304))

    im_joined = get_concat_h(im2_crop,im1_crop)

    for i in range(2,len(input_images)):
        im1 = Image.open(str(input_images[i]))
        print(str(input_images[i]))
        w, h = im1.size
        if w>h:#横長の時
            im1 = im1.rotate(-90, expand=True)
        w, h = im1.size
        im1_crop = im1.crop((w/2-25,0,w/2+25,2304))
        im_joined = get_concat_h(im1_crop,im_joined)

    for i in range(0,len(input_images)):
        im1 = Image.open(str(input_images[i]))
        w, h = im1.size
        if w>h:#横長の時
            im1 = im1.rotate(-90, expand=True)
        w, h = im1.size
        im1_crop = im1.crop((w/2-25,0,w/2+25,2304))
        im_joined = get_concat_h(im1_crop,im_joined)

    im_joined.show()
    im_joined.save('joined.jpg')
