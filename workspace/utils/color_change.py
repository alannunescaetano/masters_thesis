import os
from PIL import Image
import cv2
import numpy as np
  
def toGrayScale(datasetPath, destPath):
    for folder_path, folders, files in os.walk(datasetPath):
        for file in files:
            img_path = os.path.join(folder_path, file)
            if(img_path.endswith('.jpg')):
                img = Image.open(img_path).convert('L')
                img.save(img_path.replace(datasetPath, destPath))

def toRedChannel(datasetPath, destPath):
    for folder_path, folders, files in os.walk(datasetPath):
        for file in files:
            img_path = os.path.join(folder_path, file)
            if(img_path.endswith('.jpg')):
                src = cv2.imread(img_path, cv2.IMREAD_UNCHANGED)
                red_channel = src[:,:,2]
                red_img = np.zeros(src.shape)
                red_img[:,:,2] = red_channel
                cv2.imwrite(img_path.replace(datasetPath, destPath), red_img) 

def toBlueChannel(datasetPath, destPath):
    for folder_path, folders, files in os.walk(datasetPath):
        for file in files:
            img_path = os.path.join(folder_path, file)
            if(img_path.endswith('.jpg')):
                src = cv2.imread(img_path, cv2.IMREAD_UNCHANGED)
                blue_channel = src[:,:,0]
                blue_img = np.zeros(src.shape)
                blue_img[:,:,0] = blue_channel
                cv2.imwrite(img_path.replace(datasetPath, destPath), blue_img) 

def toGreenChannel(datasetPath, destPath):
    for folder_path, folders, files in os.walk(datasetPath):
        for file in files:
            img_path = os.path.join(folder_path, file)
            if(img_path.endswith('.jpg')):
                src = cv2.imread(img_path, cv2.IMREAD_UNCHANGED)
                green_channel = src[:,:,1]
                green_img = np.zeros(src.shape)
                green_img[:,:,1] = green_channel
                cv2.imwrite(img_path.replace(datasetPath, destPath), green_img) 

toGrayScale('C:\\Projetos\\Mestrado\\pavement_type_dataset\\pavement_type_reduced', 'C:\\Projetos\\Mestrado\\pavement_type_dataset\\pavement_type_reduced_grayscale')
toRedChannel('C:\\Projetos\\Mestrado\\pavement_type_dataset\\pavement_type_reduced', 'C:\\Projetos\\Mestrado\\pavement_type_dataset\\pavement_type_reduced_red_channel')
toBlueChannel('C:\\Projetos\\Mestrado\\pavement_type_dataset\\pavement_type_reduced', 'C:\\Projetos\\Mestrado\\pavement_type_dataset\\pavement_type_reduced_blue_channel')
toGreenChannel('C:\\Projetos\\Mestrado\\pavement_type_dataset\\pavement_type_reduced', 'C:\\Projetos\\Mestrado\\pavement_type_dataset\\pavement_type_reduced_green_channel')