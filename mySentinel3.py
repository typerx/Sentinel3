#!/usr/bin/python

from sentinelsat.sentinel import SentinelAPI, read_geojson, geojson_to_wkt
import datetime
import logging
import bson
import json
import os, sys
from dateutil import parser

logging.basicConfig(format='%(message)s', level='DEBUG')

# connect to the API
api = SentinelAPI('s3guest', 's3guest', 'https://scihub.copernicus.eu/s3')


# download single scene by known product id
#api.download(<product_id>)

# search by polygon, time, and SciHub query keywords
#products = api.query(,'20151219', date(2015, 12, 29), platformname = 'Sentinel-2', cloudcoverpercentage = '[0 TO 30]'})
#products = api.query(get_coordinates('map.geojson'),


footprint = geojson_to_wkt(read_geojson('map.geojson'))
products = api.query(footprint, date=('NOW-48HOURS', 'NOW'),platformname = 'Sentinel-3', processinglevel="1")
#print(products)

#api.get_products_size(products)
print("PRODUCT SIZE: "+ str(api.get_products_size(products)))


# download all results from the search
#api.download_all(products)

# GeoJSON FeatureCollection containing footprints and metadata of the scenes
fp=api.to_geojson(products)
#print(fp)

with open('footprints.json', 'w') as outfile:
	#json.dump({'numbers':n, 'strings':s, 'x':x, 'y':y}, outfile, indent=4)
	json.dump(fp, outfile, indent=4)  


i=0
#2017-02-07T10:42:00.746Z
#datetime_old = format_date("20170101")
usertime = "2017-11-01T00:00:00.0Z"
datetime_old = parser.parse(usertime)

print (datetime_old)


for entry in fp["features"]:
	datetime = parser.parse(entry["properties"]["beginposition"])
	if (datetime >= datetime_old):
		datetime_old=datetime
		product_id= entry["properties"]["id"]
		print ("###########"+str(datetime))
		print (entry["properties"]["identifier"])
		print (entry["properties"]["id"])
		print (entry["properties"]["beginposition"])


api.download(product_id)

sys.exit()	