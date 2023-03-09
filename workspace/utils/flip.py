import cv2
import os
from PIL import Image
import uuid

def flipImage(image, vertical, horizontal):
    
    if(vertical):
        image = image.transpose(Image.FLIP_TOP_BOTTOM)

    if(horizontal):
        image = image.transpose(Image.FLIP_LEFT_RIGHT)
    
    return image    