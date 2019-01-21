"""
Search google images and use albums.csv to store them in proper directory.
"""

from google_images_download import google_images_download
import urllib

import csv
with open('albums.csv', encoding="utf8") as csvfile:
    for row in csv.reader(csvfile, delimiter=';'):
        try:
            response = google_images_download.googleimagesdownload()
            arguments = {"keywords":row[1], "limit":1, "image_directory": row[0], "output_directory": "img",
                         "format": "jpg", "size": ">640*480"}
            absolute_image_paths = response.download(arguments)
        except: pass


