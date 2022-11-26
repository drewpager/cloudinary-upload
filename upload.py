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
from dotenv import load_dotenv
load_dotenv()

# Import the Cloudinary libraries
# ==============================
# Import to format the JSON responses
# ==============================

# Set configuration parameter: return "https" URLs by setting secure=true
# ==============================
config = cloudinary.config(
    # ADD CONFIG VARIABLES
)

# Log the configuration
# ==============================

print("****1. Set up and configure the SDK:****\nCredentials: ",
      config.cloud_name, config.api_key, "\n")

# Get File system // UPDATE USING PWD in TERMINAL
# ==============================
mypath = "/Volumes/Film and Music Backups/testing"
files = [f for f in listdir(mypath) if isfile(join(mypath, f))]

for file in files:
    route = mypath + "/" + file
    print(route)

    # Upload to Cloudinary: Change folder when ready!
    cloudinary.uploader.upload_large(
        mypath + "/" + file,
        upload_preset="platos-peach",
        resource_type="video",
        use_filename=True
    )

    srcURL = cloudinary.CloudinaryVideo(file).build_url()
    print(srcURL)

with open('videos.csv', 'w') as csvfile:
    filewriter = csv.writer(csvfile,
                            quoting=csv.QUOTE_MINIMAL, dialect="excel")
    filewriter.writerow(['title', 'cloudinary_url'])
    for file in files:
        name = Path(file).stem
        filewriter.writerow([name, srcURL])
