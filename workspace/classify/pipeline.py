import sys
sys.path.insert(0, 'C:\\Projetos\\Mestrado\\yolov5')

import torch
import pathlib
import torch.nn.functional as F
from torchvision import transforms
import numpy as np
import tensorflow as tf
import json
from shapely.geometry import Point, shape
import cv2
from enum import Enum

from models.common import DetectMultiBackend
from utils.augmentations import classify_transforms
from utils.dataloaders import IMG_FORMATS, VID_FORMATS, LoadImages, LoadScreenshots, LoadStreams
from utils.general import (LOGGER, Profile, check_file, check_img_size, check_imshow, check_requirements, colorstr, cv2,
                           increment_path, print_args, strip_optimizer)
from utils.plots import Annotator
from utils.torch_utils import select_device, smart_inference_mode

tf.config.run_functions_eagerly(True)

temp = pathlib.PosixPath
pathlib.PosixPath = pathlib.WindowsPath

yolo_repo_path_obj_detection = 'C:\\Projetos\\Mestrado\\yolov5'
yolo_repo_path_classification = 'C:\\Projetos\\Mestrado\\yolov5:classifier'

cycle_path_model_path = r'C:\Projetos\Mestrado\masters_thesis\experiments\cycle_path_detection\cycle_path_400 epochs_model_s_default\train\yolov5s_cycle_path_results\weights\best.pt'
pavement_defects_model_path = r'C:\Projetos\Mestrado\masters_thesis\experiments\pavement_defects\yolov5l_ls_01_results_400_epochs\weights\best.pt'
pavement_type_model_path = r'C:\Projetos\Mestrado\masters_thesis\experiments\pavement_type\our_dataset\1500_epochs_gsv_dataset_model_s\content\yolov5\runs\train-cls\exp4\weights\best.pt'
road_type_database_path = r'..\geodados\data\CartografiaBase.geojson'

pavement_type_preprocessing_padding_bottom = 100
pavement_type_preprocessing_scale = 150
pavement_type_preprocessing_crop_size = 224

score_pavement_type_asphalt_without_defects = 3.01
score_pavement_type_asphalt_with_defects = 2.26
score_pavement_type_cobblestone = 2.26
score_pavement_type_unpaved = 0
score_presence_of_cycle_infrastructure = 4.09
score_local_street = 2.9

class PavementType(Enum):
    ASPHALT = 0
    COBBLESTONE = 1
    UNPAVED = 2

def isThereCycleInfrastructure(img, model_path):
    model = torch.hub.load(yolo_repo_path_obj_detection, 'custom', path=model_path, source='local')

    results = model(img)

    return len(results.pandas().xyxy[0]) > 0

def isTherePavementDefects(img, model_path):
    model = torch.hub.load(yolo_repo_path_obj_detection, 'custom', path=model_path, source='local')

    results = model(img)

    return len(results.pandas().xyxy[0]) > 0

def getPavementType(img, model_path):
    #preprocessed = preprocess_image_for_pavement_type_model(img, pavement_type_preprocessing_crop_size, pavement_type_preprocessing_crop_size, pavement_type_preprocessing_padding_bottom, pavement_type_preprocessing_scale)

    #model = torch.hub.load(yolo_repo_path_obj_detection, 'custom', path=model_path, source='local', force_reload=True)
    device = ''
    device = select_device(device)
    model = DetectMultiBackend(model_path, device=device, dnn=False, data='data/coco128.yaml', fp16=False)
    stride, names, pt = model.stride, model.names, model.pt

    imgsz=(640, 640)
    imgsz = check_img_size(imgsz, s=stride)  # check image size
    bs = 1  # batch_size
    dataset = LoadImages(img, img_size=imgsz, transforms=classify_transforms(imgsz[0]), vid_stride=1)
    vid_path, vid_writer = [None] * bs, [None] * bs

    model.warmup(imgsz=(1 if pt else bs, 3, *imgsz))  # warmup
    seen, windows, dt = 0, [], (Profile(), Profile(), Profile())

    for path, im, im0s, vid_cap, s in dataset:
        with dt[0]:
            im = torch.Tensor(im).to(model.device)
            im = im.half() if model.fp16 else im.float()  # uint8 to fp16/32
            if len(im.shape) == 3:
                im = im[None]  # expand for batch dim

    results = model(im)

    pred = F.softmax(results, dim=1)[0]

    return np.argmax(pred).item()

def isMajorStreet(lat, lon):
    majorStreetsHier = [1,2,3]

    with open(road_type_database_path, encoding="utf8") as f:
        geojson = json.load(f)

    ref_point = Point(lon, lat)

    for feature in enumerate(geojson["features"]):
        line = shape(feature[1]["geometry"])

        if line.within(ref_point) or line.distance(ref_point) < 0.001:
            print(feature[1]["properties"])
            return feature[1]["properties"]["HIERARQUIA"] in majorStreetsHier
    
    return False;

def preprocess_image_for_pavement_type_model(img, h, w, paddingBottom, scalepercent = 100):
    width = int(img.shape[1] * scalepercent / 100)
    height = int(img.shape[0] * scalepercent / 100)
    dimension = (width, height)
    resized = cv2.resize(img, dimension, interpolation = cv2.INTER_LINEAR)

    x = int((width / 2) - (w / 2))
    y = int((height / 2) - (h / 2) - paddingBottom)

    return resized[y:h+y, x:w+x]

def calculate_route_segment_score(isThereCycleInfrastructure, isTherePavementDefects, pavementType, isLocalStreet):
    score = 0
    
    if isThereCycleInfrastructure:
        score += score_presence_of_cycle_infrastructure
    
    if pavementType == PavementType.ASPHALT.value:
        if isTherePavementDefects:
            score += score_pavement_type_asphalt_with_defects
        else:
            score += score_pavement_type_asphalt_without_defects

    if pavementType == PavementType.COBBLESTONE.value:
        score += score_pavement_type_cobblestone

    if pavementType == PavementType.UNPAVED.value:
        score += score_pavement_type_unpaved

    if isLocalStreet:
        score += score_local_street

    return score


def assessRouteSegment(route_segment_image_path, route_segment_lat, route_segment_lon):
    #img = cv2.imread(route_segment_image_path)

    isThereCycleInfrast = isThereCycleInfrastructure(route_segment_image_path, cycle_path_model_path)
    pavementType = getPavementType(route_segment_image_path, pavement_type_model_path)

    isTherePavementDef = False

    if pavementType == PavementType.ASPHALT.value:
        isTherePavementDef = isTherePavementDefects(route_segment_image_path, pavement_defects_model_path)

    isLocal = not isMajorStreet(route_segment_lat, route_segment_lon)

    score = calculate_route_segment_score(isThereCycleInfrast, isTherePavementDef, pavementType, isLocal)

    print('Route Segment Assessment Tool')
    print('CYCLE INFRASTRUCTURE: ' + str(isThereCycleInfrast))
    print('PAVEMENT DEFECTS: ' + str(isTherePavementDef))
    print('PAVEMENT TYPE: ' + str(pavementType))
    print('MAJOR STREET: ' + str(not isLocal))
    print('SCORE: ' + str(score))

    return [isThereCycleInfrast, pavementType, isTherePavementDef, isLocal, score]
    
fileInput = open('input.txt', 'r')
fileOutput = open('output.txt', 'w')

while True: 
    line = fileInput.readline()
    if not line:
        break

    params = line.split(',')
    
    result = assessRouteSegment(r'C:\Projetos\Mestrado\masters_thesis\survey\SurveyApp\SurveyApp\wwwroot\img\\'+params[0], params[1], params[2])
    print(result)

    fileOutput.write(params[0] + ',' + str(result[0]) + ',' + str(result[1]) + ',' + str(result[2]) + ',' +  str(result[3]) + ',' + str(result[4]) + '\n')
    
 
fileInput.close()
fileOutput.close()