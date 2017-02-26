#!/usr/bin/python

from sentinelsat.sentinel import SentinelAPI, get_coordinates, format_date
from datetime import date, datetime, timedelta
import logging
import json
 
logging.basicConfig(format='%(message)s', level='DEBUG')

# connect to the API
api = SentinelAPI('s3guest', 's3guest', 'https://scihub.copernicus.eu/s3')


# download single scene by known product id
#api.download(<product_id>)

# search by polygon, time, and SciHub query keywords
#products = api.query(,'20151219', date(2015, 12, 29), platformname = 'Sentinel-2', cloudcoverpercentage = '[0 TO 30]'})
products = api.query(get_coordinates('map.geojson'),
    initial_date=datetime(2017, 2, 24),
    end_date=datetime(2017, 2, 25))
	
#api.get_products_size(products)
print(api.get_products_size(products))

# download all results from the search
#api.download_all(products)

# GeoJSON FeatureCollection containing footprints and metadata of the scenes
fp=api.get_footprints(products)

with open('footprints.json', 'w') as outfile:
	#json.dump({'numbers':n, 'strings':s, 'x':x, 'y':y}, outfile, indent=4)
	json.dump(fp, outfile, indent=4)  

with open('product.json', 'w') as outfile:
	#json.dump({'numbers':n, 'strings':s, 'x':x, 'y':y}, outfile, indent=4)
	json.dump(products, outfile, indent=4) 

#print(fp["features"][0]["properties"]["identifier"])

i=0
#2017-02-07T10:42:00.746Z
datetime_old = format_date("20170101")
print datetime_old

for entry in fp["features"]:
	datetime = entry["properties"]["date_beginposition"]
	if (datetime >= datetime_old):
		datetime_old=datetime
		product_id= entry["properties"]["product_id"]
		print "###########"+datetime
		print entry["properties"]["identifier"]
		print entry["properties"]["product_id"]
		print entry["properties"]["date_beginposition"]

api.download(product_id)
