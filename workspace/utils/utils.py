import cv2
from pathlib import Path

def cropImage(srcPath, destPath):
    y=216
    x=200
    h=360
    w=240

    scale_percent = 200
    
    img = cv2.imread(srcPath)

    width = int(img.shape[1] * scale_percent / 100)
    height = int(img.shape[0] * scale_percent / 100)
    dimension = (width, height)
    resized = cv2.resize(img, dimension, interpolation = cv2.INTER_AREA)

    crop_img = resized[y:h+y, x:w+x]

    cv2.imwrite(destPath)

    #cv2.imshow("original", img)
    #cv2.imshow("resized", resized)
    #cv2.imshow("cropped", crop_img)
    #cv2.waitKey(0)



onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]