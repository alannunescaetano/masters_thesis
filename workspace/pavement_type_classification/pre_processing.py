import os
import cv2
import uuid
  
def preProcessImages(datasetPath, destPath, flip, toGrayScale, height, width, paddingBottom = 0, scalePercent = 100):
    for folder_path, folders, files in os.walk(datasetPath):
        for file in files:
            img_path = os.path.join(folder_path, file)
            if(img_path.endswith('.jpg')):
                img = cv2.imread(img_path)
                preProcessImage(img, destPath, flip, toGrayScale, height, width, paddingBottom, scalePercent)

def preProcessImage(img, destPath, flip, toGrayScale, height, width, paddingBottom = 0, scalePercent = 100):
    if(toGrayScale):
        img = convertToGrayScale(img)

    img = cropImage(img, height, width, paddingBottom, scalePercent)
    cv2.imwrite(os.path.join(destPath, str(uuid.uuid4())+'.jpg'), img)

    if(flip):
        cv2.imwrite(os.path.join(destPath, str(uuid.uuid4())+'.jpg'), flipImage(img, True, False))
        cv2.imwrite(os.path.join(destPath, str(uuid.uuid4())+'.jpg'), flipImage(img, False, True))
        cv2.imwrite(os.path.join(destPath, str(uuid.uuid4())+'.jpg'), flipImage(img, True, True))

def cropImage(img, h, w, paddingBottom, scalepercent = 100):
    width = int(img.shape[1] * scalepercent / 100)
    height = int(img.shape[0] * scalepercent / 100)
    dimension = (width, height)
    resized = cv2.resize(img, dimension, interpolation = cv2.INTER_LINEAR)

    x = int((width / 2) - (w / 2))
    y = int((height / 2) - (h / 2) - paddingBottom)

    return resized[y:h+y, x:w+x]

def flipImage(image, vertical, horizontal):
    
    if(vertical):
        image = cv2.flip(image, 1)

    if(horizontal):
        image = cv2.flip(image, 0)
    
    return image   

def convertToGrayScale(img):
    return cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


preProcessImages('C:\\Projetos\\Mestrado\\pavement_type_dataset\\gsv\\asphalt', 'C:\\Projetos\\Mestrado\\pavement_type_dataset\\gsv_pre_processed\\asphalt\\full', False, False, 224, 224, 200, 150)
preProcessImages('C:\\Projetos\\Mestrado\\pavement_type_dataset\\gsv\\cobblestone', 'C:\\Projetos\\Mestrado\\pavement_type_dataset\\gsv_pre_processed\\cobblestone\\full', False, False, 224, 224, 200, 150)
preProcessImages('C:\\Projetos\\Mestrado\\pavement_type_dataset\\gsv\\unpaved', 'C:\\Projetos\\Mestrado\\pavement_type_dataset\\gsv_pre_processed\\unpaved\\full', False, False, 224, 224, 200, 150)


