import requests
import os
import shutil
import sys

def copy_image(image_url, download_path):
	r = requests.get(image_url, stream=True)
	if r.status_code == 200:
	    with open(download_path, 'wb') as f:
	        r.raw.decode_content = True
	        shutil.copyfileobj(r.raw, f)   

def get_images(url):
	if url is None:
		return []
	r = requests.get(url)
	if r.status_code == 200:
		return [result['large_thumbnail_url'] for result in r.json()["search"]["results"]]
	return []

api_key = "eJesEUUomq_zGoW9nBAW"
url = "http://api.digitalnz.org/v3/records.json?api_key={api_key}&text=stamp&and[category][]=Images&per_page=200".format(api_key=api_key)
page = sys.argv[1]

url += "&page=%s" % page

folder = "image_collection"
if not os.path.exists(folder):
	os.mkdir(folder)

for index, thumb in enumerate(get_images(url)):
	print "downloading:", thumb
	try:
		copy_image(thumb, os.path.join(folder, "%s_%s.jpg" % (page, index)))
	except Exception as error:
		print "Error downloading image %s:" % thumb, error
		continue
