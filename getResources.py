# Set your Cloudinary credentials
# ==============================
import cloudinary.api
import cloudinary.uploader
import cloudinary
import json
from pathlib import Path
import csv
from os.path import isfile, join
from os import listdir
import os

 # Set configuration parameter: return "https" URLs by setting secure=true
# ==============================

config = cloudinary.config(
#   "cloud_name": "",
#   "api_key": "",
#   "api_secret": ""
)

# Log the configuration
# ==============================

print("****1. Set up and configure the SDK:****\nCredentials: ",
      config.cloud_name, config.api_key, "\n")


# Set Max Count to 363 and then flip to ascending for 362
res = cloudinary.api.resources(resource_type="video", max_results=348)
resources = res['resources']
next = res['next_cursor']

with open('urls.csv', 'w') as csvfile:
    filewriter = csv.writer(csvfile, delimiter=",",
                            quoting=csv.QUOTE_MINIMAL, dialect="excel")
    filewriter.writerow(['cloudinary_url'])
    for v in resources:
        filewriter.writerow([v['url']])


res = cloudinary.api.resources(resource_type="video", max_results=348, next_cursor=next)
resources = res['resources']

with open('second-half.csv', 'w') as csvfile:
    filewriter = csv.writer(csvfile, delimiter=",",
                            quoting=csv.QUOTE_MINIMAL, dialect="excel")
    filewriter.writerow(['cloudinary_url'])
    for v in resources:
        filewriter.writerow([v['url']])