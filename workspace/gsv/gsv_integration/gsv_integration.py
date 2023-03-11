#chave google 
#https://maps.googleapis.com/maps/api/streetview?size=700x700&location=41.182899,-8.631079&fov=110&heading=-20&pitch=-30&key=AIzaSyByAmga1wYKYBssQqGB3AsQw7NXI5LTYI8

import google_streetview.api
import google_streetview.helpers
import os
import uuid

def getImagesFromGSV(lat, long, path):

    params = [{
        'size': '640x640',
        'location': str(lat)+','+str(long),
        'heading': '-50', # lateral rotation
        'pitch': '-50', # vertical rotation
        'key': 'AIzaSyByAmga1wYKYBssQqGB3AsQw7NXI5LTYI8'
    }]

    results = google_streetview.api.results(params)

    results.download_links(path)

    os.rename(os.path.join(path, 'gsv_0.jpg'), os.path.join(path, str(uuid.uuid4())+'.jpg'))


getImagesFromGSV(38.7085145,-9.1470139, 'C:\\Projetos\\Mestrado\\masters_thesis\\datasets\\pavement_type_raw\\cobblestone')