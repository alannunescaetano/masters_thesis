import cv2
import os
from PIL import Image
import uuid

def flipImage(srcPath, destFolder):
    
    imageObject = Image.open(srcPath)

    flippedH = imageObject.transpose(Image.FLIP_LEFT_RIGHT)
    flippedV = imageObject.transpose(Image.FLIP_TOP_BOTTOM)
    flippedBoth = imageObject.transpose(Image.FLIP_TOP_BOTTOM).transpose(Image.FLIP_LEFT_RIGHT)

    imageObject.save(os.path.join(destFolder, str(uuid.uuid4())+'.jpg'))
    flippedH.save(os.path.join(destFolder, str(uuid.uuid4())+'.jpg'))
    flippedV.save(os.path.join(destFolder, str(uuid.uuid4())+'.jpg'))
    flippedBoth.save(os.path.join(destFolder, str(uuid.uuid4())+'.jpg'))

    #cv2.imwrite(destPath, crop_img)

#cropImage('C:\\Projetos\\Mestrado\\masters_thesis\\workspace\\gsv\\images\\gravel\\gsv_4.jpg', 'C:\\Projetos\\Mestrado\\masters_thesis\\workspace\\gsv\\images\\gravel\\4.jpg')

srcFolder = "C:\\Projetos\\Mestrado\\masters_thesis\\datasets\\cobblestone_cut"
destFolder = "C:\\Projetos\\Mestrado\\masters_thesis\\datasets\\cobblestone_flipped"

for file in os.listdir(srcFolder):
    flipImage(os.path.join(srcFolder, file), destFolder)
    