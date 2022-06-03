import re
import math

def dms2dd(*dms):
    degrees = dms[0][0]
    minutes = dms[0][1]
    seconds = dms[0][2]
    print(degrees)
    print(minutes)
    print(seconds)
    dd = float(degrees) + float(minutes)/60 + float(seconds)/(60*60);
    # if direction == 'E' or direction == 'N':
    #     dd *= -1
    return dd;

def dd2dms(deg):
    d = int(deg)
    md = abs(deg - d) * 60
    m = int(md)
    sd = (md - m) * 60
    return [d, m, sd]

def parse_dms(dms):
    parts = re.split('[^\d\w]+', dms)
    lat = dms2dd(parts[0], parts[1], parts[2], parts[3])

    return (lat)

# 8.3
d = 485.32
d_s = 0.018
az = (78, 16, 8)
az_s = (0, 0, 5)
lat = d * math.cos(math.radians(dms2dd(az)))
dep = d * math.sin(math.radians(dms2dd(az)))


print("""
lat: {}
dep: {}
""".format(lat, dep))




