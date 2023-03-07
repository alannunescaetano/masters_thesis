import os
from PIL import Image
  
def toGrayScale(datasetPath, destPath):
    for folder_path, folders, files in os.walk(datasetPath):
        for file in files:
            img_path = os.path.join(folder_path, file)
            img = Image.open(img_path).convert('L')
            img.save(img_path.replace(datasetPath, destPath))

toGrayScale('C:\\Projetos\\Mestrado\\pavement_type_dataset\\pavement_type_reduced', 'C:\\Projetos\\Mestrado\\pavement_type_dataset\\pavement_type_reduced_grayscale')