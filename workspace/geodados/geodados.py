import json

from shapely.ops import nearest_points
from shapely.geometry import Point, LineString, mapping, shape

def isMajorStreet(lat, lon):
    majorStreetsHier = [1,2,3]

    with open("geodados\data\CartografiaBase.geojson", encoding="utf8") as f:
        geojson = json.load(f)

    ref_point = Point(lon, lat)

    for feature in enumerate(geojson["features"]):
        line = shape(feature[1]["geometry"])

        if line.within(ref_point) or line.distance(ref_point) < 0.001:
            print(feature[1]["properties"])
            return feature[1]["properties"]["HIERARQUIA"] in majorStreetsHier
    
    return False;
        
print(isMajorStreet(38.759694, -9.1158574))