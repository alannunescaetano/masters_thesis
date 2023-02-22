import cv2
import os

def cropImage(srcPath, destPath):
    print(srcPath)
    print(destPath)
    y=216
    x=150
    h=360
    w=240

    scale_percent = 200
    
    img = cv2.imread(srcPath)

    width = int(img.shape[1] * scale_percent / 100)
    height = int(img.shape[0] * scale_percent / 100)
    dimension = (width, height)
    resized = cv2.resize(img, dimension, interpolation = cv2.INTER_AREA)

    crop_img = resized[y:h+y, x:w+x]

    cv2.imwrite(destPath, crop_img)

    #cv2.imshow("original", img)
    #cv2.imshow("resized", resized)
    #cv2.imshow("cropped", crop_img)
    #cv2.waitKey(0)

#cropImage(os.path.join('C:\\Projetos\\Mestrado\\masters_thesis\\datasets\\pavement_type\\cobblestone\\raw', '3_000001358 (1285).png'), os.path.join('C:\\Projetos\\Mestrado\\masters_thesis\\datasets\\pavement_type\\cobblestone', '1.png'))

srcFolder = "C:\\Projetos\\Mestrado\\masters_thesis\\datasets\\pavement_type\\cobblestone\\raw"
destFolder = "C:\\Projetos\\Mestrado\\masters_thesis\\datasets\\pavement_type\\cobblestone"

i = 0
for file in os.listdir(srcFolder):
    i += 1
    cropImage(os.path.join(srcFolder, file), os.path.join(destFolder, str(i)+'.png'))
    