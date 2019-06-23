import cv2
import glob
from PIL import Image
import time
import sys
import math

UI_ON = 0 #UIの方からボトルの端を選択するときは1

# 外部プログラムから拾う値
crop_width_left = 431
crop_width_right = 978

#写真は縦長
PIXEL_PICT_WIDTH = 1536
PIXEL_PICT_HEIGHT = 2304
CAMERA_BOTTLE_DISTANCE = 250 #mm カメラとボトル中心までの距離
ANGLE_OF_VIEW = 43.3 #degree 水平方向の画角


print(cv2.__version__)#openCV 4.1.0で動作確認

def get_concat_h(im1, im2):
    dst = Image.new('RGB', (im1.width + im2.width, im1.height))
    dst.paste(im1, (0, 0))
    dst.paste(im2, (im1.width, 0))
    return dst

def make_longer_than_width(image):
    w, h = image.size

    if w>h:#横長の時
        image = image.rotate(-90, expand=True)

    return image

def estimate_diameter(image, left_px, right_px,camera_angle,camera_bottle_distance):
    image_ltw = make_longer_than_width(image)

    if UI_ON:
        image_ltw_crop = image_ltw.crop((left_px, 0, right_px, PIXEL_PICT_WIDTH))
    else:
        crop_width_right_from_center = 210
        crop_width_left_from_center = 337
        image_ltw_crop = image_ltw.crop((PIXEL_PICT_WIDTH/2-crop_width_left_from_center,0,PIXEL_PICT_WIDTH/2+crop_width_right_from_center,PIXEL_PICT_HEIGHT))

    image_ltw_crop.save('croped.jpg')

    if UI_ON:
        pixel_bottle_diameter = abs(crop_width_right - crop_width_left)
        print("pixel_bottle_diameter")
        print(pixel_bottle_diameter)
    else:
        pixel_bottle_diameter = crop_width_left_from_center + crop_width_right_from_center

#    estimeated_bottle_diameter = 2.*CAMERA_BOTTLE_DISTANCE * math.tan(math.radians(ANGLE_OF_VIEW/2))*pixel_bottle_diameter/PIXEL_PICT_WIDTH
    estimeated_bottle_diameter = 2.*CAMERA_BOTTLE_DISTANCE * math.tan(math.radians(ANGLE_OF_VIEW/2))*547/PIXEL_PICT_WIDTH

    return estimeated_bottle_diameter




if __name__ == "__main__":

    input_images = glob.glob('image_data/*.jpg')
    print(input_images)

    im1 = Image.open(str(input_images[0]))

    val = estimate_diameter(im1, crop_width_left, crop_width_right, ANGLE_OF_VIEW, CAMERA_BOTTLE_DISTANCE)

    print(str(val) + "mm")

    '''
    print("pixel_pict_width")
    print(pixel_pict_width)


    print(pixel_bottle_diameter)
    print(pixel_pict_width)
    '''