import cv2
import glob
from PIL import Image
import time
import sys
import math

print(cv2.__version__)#openCV 4.1.0で動作確認

def get_concat_h(im1, im2):
    dst = Image.new('RGB', (im1.width + im2.width, im1.height))
    dst.paste(im1, (0, 0))
    dst.paste(im2, (im1.width, 0))
    return dst


if __name__ == "__main__":

    input_images = glob.glob('image_data/*.jpg')
    print(input_images)

    im1 = Image.open(str(input_images[0]))
    w, h = im1.size

    if w>h:#横長の時
        im1 = im1.rotate(-90, expand=True)
    w, h = im1.size
    pixel_pict_width = w
    crop_width_right = 210
    crop_width_left = 337
    im1_crop = im1.crop((w/2-crop_width_left,0,w/2+crop_width_right,2304))

#    im_joined.show()
    im1_crop.save('croped.jpg')

    pixel_bottle_diameter = crop_width_left + crop_width_right
    print(pixel_bottle_diameter)
    print(pixel_pict_width)

    camera_bottle_distance = 250 #mm
    angle_of_view = 43.3 #degree

    estimeated_bottle_diameter = 2.*camera_bottle_distance * math.tan(math.radians(angle_of_view/2))*pixel_bottle_diameter/pixel_pict_width
    print(str(estimeated_bottle_diameter) + "mm")