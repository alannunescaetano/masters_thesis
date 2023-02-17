#chave google 
#https://maps.googleapis.com/maps/api/streetview?size=700x700&location=41.182899,-8.631079&fov=110&heading=-20&pitch=-30&key=AIzaSyByAmga1wYKYBssQqGB3AsQw7NXI5LTYI8

import google_streetview.api
import google_streetview.helpers

def getImagesFromGSV(lat, long, path):

    params = [{
        'size': '640x640',
        'location': str(lat)+','+str(long),
        'heading': '-20', # lateral rotation
        'pitch': '-30', # vertical rotation
        'key': 'AIzaSyByAmga1wYKYBssQqGB3AsQw7NXI5LTYI8'
    }]

    results = google_streetview.api.results(params)

    results.download_links(path)

getImagesFromGSV(41.182899,-8.631079, 'C:\Projetos\Mestrado\masters_thesis\workspace\gsv\images')