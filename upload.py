# Set your Cloudinary credentials
# ==============================
from dotenv import load_dotenv
load_dotenv()

# Import the Cloudinary libraries
# ==============================
import cloudinary
import cloudinary.uploader
import cloudinary.api
import os
from os import listdir
from os.path import isfile, join
import csv
from pathlib import Path
# Import to format the JSON responses
# ==============================
import json

# Set configuration parameter: return "https" URLs by setting secure=true  
# ==============================
config = cloudinary.config()

# Log the configuration
# ==============================

print("****1. Set up and configure the SDK:****\nCredentials: ", config.cloud_name, config.api_key, "\n")

# Get File system // UPDATE USING PWD in TERMINAL
# ==============================
mypath = "/Users/drewpage/Desktop/Personal/Video"
files = [f for f in listdir(mypath) if isfile(join(mypath, f))]

for file in files:
  route = mypath + "/" + file
  print(route)
  
  # Upload to Cloudinary: Change folder when ready! 
  cloudinary.uploader.upload(mypath + "/" + file, folder="TH_assets", resource_type="video")

  srcURL = cloudinary.CloudinaryImage(file).build_url()
  print(srcURL)

with open('videos.csv', 'w') as csvfile:
  filewriter = csv.writer(csvfile, quotechar='|', quoting=csv.QUOTE_MINIMAL, dialect="excel")
  filewriter.writerow(['title', 'cloudinary_url'])
  for file in files:
    name = Path(file).stem
    filewriter.writerow([name, srcURL])
