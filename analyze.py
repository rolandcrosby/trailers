from __future__ import print_function
import json
import math
import os
import sys
import time
import urllib

if not os.path.isfile('trailers.json'):
    urllib.urlretrieve('https://data.ny.gov/api/views/rcmm-pc7d/rows.json?accessType=DOWNLOAD', 'trailers.json')

vins = []
bad_vins = 0
with open('trailers.json') as f:
    data = json.load(f)
    for d in data['data']:
        vin = d[9].strip()
        if len(vin) != 17:
            bad_vins += 1
        else:
            vins.append(vin)

sys.stderr.write("%d VINs to check, %d obviously bad\n" %
                 (len(vins), bad_vins))

if not os.path.isfile('trailer-lengths.tsv'):
    with open('trailer-lengths.tsv', 'w') as f:
        idx = 0
        while idx < len(vins):
            sys.stderr.write("fetching index %d\n" % idx)
            vin_chunk = ';'.join(vins[idx:idx+100])
            try:
                http_response = urllib.urlopen('https://vpic.nhtsa.dot.gov/api/vehicles/DecodeVINValuesBatch/',
                                    urllib.urlencode({'format': 'JSON', 'DATA': vin_chunk}))
                response_data = json.load(http_response)
                for trailer in response_data['Results']:
                    if trailer['TrailerLength'] != '':
                        f.write("%s\t%s\n" % (trailer['VIN'], trailer['TrailerLength']))
                        print(trailer['VIN'], trailer['TrailerLength'])
            except IOError:
                sys.stderr.write("error retrieving from NHTSA, retrying...\n")
                time.sleep(1)
                next
            idx += 100

total = 0
gt48 = 0
gt53 = 0

with open('trailer-lengths.tsv') as f:
    for line in f:
        vin, length = line.rstrip().split("\t")
        total += 1
        l = float(length)
        if l >= 48:
            gt48 += 1
        if l >= 53:
            gt53 += 1
sys.stderr.write("%d total trailers, %d longer than 48', %d longer than 53'\n" % (total, gt48, gt53))
