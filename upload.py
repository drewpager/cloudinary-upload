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
# Import to format the JSON responses
# ==============================
import json

# Set configuration parameter: return "https" URLs by setting secure=true  
# ==============================
config = cloudinary.config()

# Log the configuration
# ==============================

print("****1. Set up and configure the SDK:****\nCredentials: ", config.cloud_name, config.api_key, "\n")

# Get File system
# ==============================
mypath = "/Users/drewpage/Desktop/Personal/Video"
files = [f for f in listdir(mypath) if isfile(join(mypath, f))]
print(files)
for file in files:
  print(mypath + "/" + file)
  cloudinary.uploader.upload(mypath + "/" + file, folder="TH_assets", resource_type="video")

  srcURL = cloudinary.CloudinaryImage(file).build_url()

  with open('videos.csv', 'wb') as csvfile:
    filewriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
    filewriter.writerow(["title", "cloudinary_url"])
    filewriter.writerow({ 'title': file, 'cloudinary_url': srcURL })

  print(srcURL)

# Upload files from folder``
# ==============================
# cloudinary.uploader.upload(files[0], folder="TH_assets")

# srcURL = cloudinary.CloudinaryImage(files).build_url()

# print(srcURL)