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

# Import the Cloudinary libraries
# ==============================
# Import to format the JSON responses
# ==============================

# Set configuration parameter: return "https" URLs by setting secure=true
# ==============================
print("Enter API Secret: ")

config = cloudinary.config(
    cloud_name="drewpager",
    api_key="249778568612973",
    api_secret = input()
)

# Log the configuration
# ==============================
print("Enter the path to content (ex. Volumes/Desktop/Academic Version Uploads): ")
mypath = input()
print("****1. Set up and configure the SDK:****\nCredentials: ", config.cloud_name, config.api_key, "\n")

# Get File system // UPDATE USING PWD in TERMINAL
# ==============================
files = [f for f in listdir(mypath) if isfile(join(mypath, f))]

with open('videos.csv', 'w') as csvfile:
    filewriter = csv.writer(csvfile,
                            quoting=csv.QUOTE_MINIMAL, dialect="excel")
    filewriter.writerow(['title', 'cloudinary_url'])
    for file in files:
        route = mypath + "/" + file
        print(route)

        cloudinary.uploader.upload_large(
            mypath + "/" + file,
            upload_preset="platos-peach",
            resource_type="video",
            use_filename=True
        )

        srcURL = cloudinary.CloudinaryVideo(file).build_url()
        print(srcURL)
        # If videos have extensions:
        # name = Path(file).stem

        # If videos do not have extensions:
        name = Path(file)
        filewriter.writerow([name, srcURL])
