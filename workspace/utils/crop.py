import cv2
import os

def cropImage(img, h, w, paddingBottom, scalepercent = 100):
    width = int(img.shape[1] * scalepercent / 100)
    height = int(img.shape[0] * scalepercent / 100)
    dimension = (width, height)
    resized = cv2.resize(img, dimension, interpolation = cv2.INTER_LINEAR)

    x = int((width / 2) - (w / 2))
    y = int((height / 2) - (h / 2) - paddingBottom)

    return resized[y:h+y, x:w+x]



#cropImage('C:\\Projetos\\Mestrado\\masters_thesis\\workspace\\gsv\\images\\gravel\\gsv_4.jpg', 'C:\\Projetos\\Mestrado\\masters_thesis\\workspace\\gsv\\images\\gravel\\4.jpg')

#srcFolder = "C:\\Projetos\\Mestrado\\masters_thesis\\workspace\\gsv\\images\\asphalt"
#destFolder = "C:\\Projetos\\Mestrado\\masters_thesis\\workspace\\gsv\\images\\asphalt\\cut"


#i = 0
#for file in os.listdir(srcFolder):
    #i += 1
    #cropImage(os.path.join(srcFolder, file), os.path.join(destFolder, str(i)+'.jpg'), 224, 224, 100, 100)

#i = 0
#for file in os.listdir(srcFolder):
#    i += 1
#    cropImage(os.path.join(srcFolder, file), os.path.join(destFolder, str(i)+'.png'), 240, 240, 90)
    