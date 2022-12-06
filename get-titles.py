from os import listdir
from os.path import isfile, join
import csv
from pathlib import Path

# Get File system // UPDATE USING PWD in TERMINAL
# ==============================
# mypath = "/Users/drewpage/Desktop/"
# mypath = "/Volumes/Film and Music Backups/Cloudinary-Success"
mypath = "/Volumes/Film\ and\ Music\ Backups/Cloudinary-Success"
files = [f for f in listdir(mypath) if isfile(join(mypath, f))]

with open('names.csv', 'w') as csvfile:
    filewriter = csv.writer(csvfile, quotechar='|',
                            quoting=csv.QUOTE_MINIMAL, dialect="excel")
    filewriter.writerow(['title'])
    for file in files:
        name = Path(file).stem
        filewriter.writerow([name])
