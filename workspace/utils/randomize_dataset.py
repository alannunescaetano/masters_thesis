import os
import random
import shutil
  
def splitDataset(datasetPath):
    i = 0
    pathFull = os.path.join(datasetPath, 'full')

    random.seed(10)

    for folder_path, folders, files in os.walk(datasetPath):
        if(folder_path != pathFull and 'full' in folder_path):
            for file in files:
                rand_int = random.randint(0, 9)

                if rand_int >= 0 and rand_int <= 6:
                    train_path = folder_path.replace("full", "train")

                    if(not os.path.isdir(train_path)):
                        os.makedirs(train_path)
                    
                    shutil.copyfile(os.path.join(folder_path, file), os.path.join(train_path, file))
                elif rand_int >= 7 and rand_int <= 8:
                    test_path = folder_path.replace("full", "test")

                    if(not os.path.isdir(test_path)):
                        os.makedirs(test_path)
                    
                    shutil.copyfile(os.path.join(folder_path, file), os.path.join(test_path, file))
                elif rand_int == 9:
                    validation_path = folder_path.replace("full", "validation")

                    if(not os.path.isdir(validation_path)):
                        os.makedirs(validation_path)
                    
                    shutil.copyfile(os.path.join(folder_path, file), os.path.join(validation_path, file))
    
    print('finished splitting!')
            
            

splitDataset('C:\\Projetos\\Mestrado\\masters_thesis\\datasets\\pavement_type')