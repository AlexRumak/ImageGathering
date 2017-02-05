from icrawler.builtin import GoogleImageCrawler
from PIL import Image
import math
import os
import shutil
import colorsys
import sys

#from icrawler.examples import BingImageCrawler
#from icrawler.examples import BaiduImageCrawler

def greenEnough(pixels, threshold):
	total = len(pixels)
	sampleSize = int(round(total/1000))
	count = 0
	for i in range(0, total, sampleSize):
		if pixelIsGreen(pixels[i]):
			count += 1
	if count*sampleSize/total > threshold:
		return True
	return False
	
def pixelIsGreen(rgb):
	if rgb[1] > 64 and rgb[1] > rgb[0] + rgb[2]:
		return True
	return False
	
def colorDistance(rgb1, rgb2):
	red_mean = (long(rgb1[0]) + long(rgb2[0])) / 2;
	r = long(rgb1[0]) - long(rgb2[0])
	g = long(rgb1[1]) - long(rgb2[1])
	b = long(rgb1[2]) - long(rgb2[2])
	return sqrt((((512+red_mean)*r*r)>>8) + 4*g*g + (((767 - red_mean)*b*b)>>8))
	
def main():
	try:
		searchTerm = str(sys.argv[1])
		numberOfImages = int(sys.argv[2])
	except IndexError:
		print("Invalid args. Correct usage:")
		print("	 ImageFilter searchTerm numberOfImages")
		return -1
	fileDirectory = "your_image_dir/"
	filteredDirectory = "your_image_dir/ 	"
	filetypes = [".jpg", ".jpeg", "end_flag"]
	threshold = 0.20
	searchParam = searchTerm + " filetype:jpg"

	google_crawler = GoogleImageCrawler(parser_threads=2, downloader_threads=4, storage={'root_dir': 'your_image_dir'})
	google_crawler.crawl(keyword = searchParam, offset=0, max_num=numberOfImages, date_min=None, date_max=None, min_size=(200,200), max_size=None)


	for i in range(1, numberOfImages + 1):
		numDigits = len(str(i))
		stringBuild = ""
		for j in range(0,6-numDigits):
			stringBuild += str(0)
		stringBuild += str(i)
		print('checking: {:s}'.format(stringBuild))
		hasOccured = False
		
		for file in filetypes:
			try:
				file_path = fileDirectory + stringBuild + file
				target_path = filteredDirectory + stringBuild + file
				
				#check if file is green enough
				im = Image.open(file_path)
				pix = im.getdata() #get the pixels as a flattened sequence
				width, height = im.size
				if greenEnough(pix, threshold):
					shutil.move(file_path, target_path)
					print('File {:s} successfully moved to {:s}'.format(stringBuild, target_path))
					break
			except FileNotFoundError:
				continue
			except PermissionError:
				print('Permission Error on file number {:s}'.format(stringBuild))
				continue
			except OSError:
				print('OS Error on file number {:s}'.format(stringBuild))
		
if __name__ == "__main__":
	main()
