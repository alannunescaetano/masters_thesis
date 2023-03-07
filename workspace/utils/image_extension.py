import os
from PIL import Image
  
def pngToJpg(datasetPath):
    for folder_path, folders, files in os.walk(datasetPath):
        for file in files:
            img_path = os.path.join(folder_path, file)
            if(img_path.endswith('.png')):
                im = Image.open(img_path)
                rgb_im = im.convert('RGB')
                rgb_im.save(img_path.replace('.png', '.jpg'))

pngToJpg('C:\\Projetos\\Mestrado\\pavement_type_dataset\\pavement_type_reduced\\val\\cobblestone')