#chave google 
#https://maps.googleapis.com/maps/api/streetview?size=700x700&location=41.182899,-8.631079&fov=110&heading=-20&pitch=-30&key=AIzaSyByAmga1wYKYBssQqGB3AsQw7NXI5LTYI8

import google_streetview.api
import google_streetview.helpers
import os
import uuid

def getImagesFromGSV(location, path, heading, fileName = None):

    params = [{
        'size': '640x640',
        'location': location,
        'heading': heading, # lateral rotation
        'pitch': '-50', # vertical rotation
        'key': 'AIzaSyByAmga1wYKYBssQqGB3AsQw7NXI5LTYI8'
    }]

    results = google_streetview.api.results(params)

    results.download_links(path)

    if(fileName is None):
        os.rename(os.path.join(path, 'gsv_0.jpg'), os.path.join(path, str(uuid.uuid4())+'.jpg'))
    else:
        os.rename(os.path.join(path, 'gsv_0.jpg'), os.path.join(path, fileName+'.jpg'))

location = '38.7351638,-9.1432162'

getImagesFromGSV('38.7319946,-9.1049083', 'C:\\Projetos\\Mestrado\\masters_thesis\\workspace\\gsv\\images\\survey',35,'segment1')
