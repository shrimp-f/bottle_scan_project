import cv2
import glob
from PIL import Image
import time
import sys
import math
import numpy as np
import matplotlib.pyplot as plt

def to_matplotlib_format(img):
    return cv2.cvtColor(img, cv2.COLOR_BGR2RGB)


def make_longer_than_width(image):
    w, h = image.size

    if w>h:#横長の時
        image = image.rotate(-90, expand=True)

    return image

def morph(img):
    kernel = np.ones((10, 10),np.uint8)
    opened = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel, iterations=2)
    return opened


input_images = glob.glob('image_takanoi/*.jpg')
#print(input_images)

im1 = Image.open(str(input_images[0]))
im1 = make_longer_than_width(im1)
#PIL形式をopenCV形式に変換
im1_cv=np.asarray(im1)



# 定数定義
ORG_WINDOW_NAME = "org"
GRAY_WINDOW_NAME = "gray"
CANNY_WINDOW_NAME = "canny"

ORG_FILE_NAME = "org.jpg"
GRAY_FILE_NAME = "gray.png"
CANNY_FILE_NAME = "canny.png"

#閾値処理
im2_cv = im1_cv
min = np.array([98, 98, 98], np.uint8) #BGR #49,0,0だと緑消えた。0,49,0だと両方消えた。
max = np.array([255, 255, 255], np.uint8)

blue_region = cv2.inRange(im2_cv, min, max)#BGR

plt.imshow(to_matplotlib_format(blue_region))
plt.show()


#org_img = cv2.imread(ORG_FILE_NAME, cv2.IMREAD_UNCHANGED)
img = morph(blue_region)
# グレースケールに変換
#gray_img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
# エッジ抽出
#canny_img = cv2.Canny(gray_img, 50, 110)
canny_img = cv2.Canny(img, 50, 110)

#plt.imshow(to_matplotlib_format(org_img))
#plt.imshow(img)
#plt.show()
#plt.imshow(to_matplotlib_format(gray_img))
#plt.show()
plt.imshow(to_matplotlib_format(canny_img))
plt.show()

'''
# ウィンドウに表示
cv2.namedWindow(ORG_WINDOW_NAME)
cv2.namedWindow(GRAY_WINDOW_NAME)
cv2.namedWindow(CANNY_WINDOW_NAME)

cv2.imshow(ORG_WINDOW_NAME, org_img)
cv2.imshow(GRAY_WINDOW_NAME, gray_img)
cv2.imshow(CANNY_WINDOW_NAME, canny_img)

# ファイルに保存
cv2.imwrite(GRAY_FILE_NAME, gray_img)
cv2.imwrite(CANNY_FILE_NAME, canny_img)

# 終了処理
cv2.waitKey(0)
cv2.destroyAllWindows()
'''