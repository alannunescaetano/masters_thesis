import cv2
import os

def cropImage(srcPath, destPath, scalepercent = 100):
    print(srcPath)
    print(destPath)

    h=360
    w=240
   
    img = cv2.imread(srcPath)

    width = int(img.shape[1] * scalepercent / 100)
    height = int(img.shape[0] * scalepercent / 100)
    dimension = (width, height)
    resized = cv2.resize(img, dimension, interpolation = cv2.INTER_AREA)

    x = int((width / 2) - (w / 2))
    y = int((height - h))

    crop_img = resized[y:h+y, x:w+x]

    cv2.imwrite(destPath, crop_img)

    #cv2.imshow("original", img)
    #cv2.imshow("resized", resized)
    #cv2.imshow("cropped", crop_img)
    #cv2.waitKey(0)

cropImage('C:\\Projetos\\Mestrado\\masters_thesis\\workspace\\gsv\\images\\asphalt\\gsv_1.jpg', 'C:\\Projetos\\Mestrado\\masters_thesis\\workspace\\gsv\\images\\asphalt\\1.jpg')
cropImage('C:\\Projetos\\Mestrado\\masters_thesis\\workspace\\gsv\\images\\asphalt\\gsv_2.jpg', 'C:\\Projetos\\Mestrado\\masters_thesis\\workspace\\gsv\\images\\asphalt\\2.jpg')
cropImage('C:\\Projetos\\Mestrado\\masters_thesis\\workspace\\gsv\\images\\asphalt\\gsv_3.jpg', 'C:\\Projetos\\Mestrado\\masters_thesis\\workspace\\gsv\\images\\asphalt\\3.jpg')

cropImage('C:\\Projetos\\Mestrado\\masters_thesis\\workspace\\gsv\\images\\cobblestone\\gsv_1.jpg', 'C:\\Projetos\\Mestrado\\masters_thesis\\workspace\\gsv\\images\\cobblestone\\1.jpg')
cropImage('C:\\Projetos\\Mestrado\\masters_thesis\\workspace\\gsv\\images\\cobblestone\\gsv_2.jpg', 'C:\\Projetos\\Mestrado\\masters_thesis\\workspace\\gsv\\images\\cobblestone\\2.jpg')
cropImage('C:\\Projetos\\Mestrado\\masters_thesis\\workspace\\gsv\\images\\cobblestone\\gsv_3.jpg', 'C:\\Projetos\\Mestrado\\masters_thesis\\workspace\\gsv\\images\\cobblestone\\3.jpg')
cropImage('C:\\Projetos\\Mestrado\\masters_thesis\\workspace\\gsv\\images\\cobblestone\\gsv_4.jpg', 'C:\\Projetos\\Mestrado\\masters_thesis\\workspace\\gsv\\images\\cobblestone\\4.jpg')

cropImage('C:\\Projetos\\Mestrado\\masters_thesis\\workspace\\gsv\\images\\gravel\\gsv_1.jpg', 'C:\\Projetos\\Mestrado\\masters_thesis\\workspace\\gsv\\images\\gravel\\1.jpg')
cropImage('C:\\Projetos\\Mestrado\\masters_thesis\\workspace\\gsv\\images\\gravel\\gsv_2.jpg', 'C:\\Projetos\\Mestrado\\masters_thesis\\workspace\\gsv\\images\\gravel\\2.jpg')
cropImage('C:\\Projetos\\Mestrado\\masters_thesis\\workspace\\gsv\\images\\gravel\\gsv_3.jpg', 'C:\\Projetos\\Mestrado\\masters_thesis\\workspace\\gsv\\images\\gravel\\3.jpg')
cropImage('C:\\Projetos\\Mestrado\\masters_thesis\\workspace\\gsv\\images\\gravel\\gsv_4.jpg', 'C:\\Projetos\\Mestrado\\masters_thesis\\workspace\\gsv\\images\\gravel\\4.jpg')

#srcFolder = "C:\\Projetos\\Mestrado\\masters_thesis\\datasets\\pavement_type\\cobblestone\\raw"
#destFolder = "C:\\Projetos\\Mestrado\\masters_thesis\\datasets\\pavement_type\\cobblestone"

#i = 0
#for file in os.listdir(srcFolder):
#    i += 1
#    cropImage(os.path.join(srcFolder, file), os.path.join(destFolder, str(i)+'.png'))
    