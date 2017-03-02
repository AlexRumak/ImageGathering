
# ImageGathering

## About:
Image crawler implementation using Python library icrawler. ImageFilter crawls google images for a given number of search images and puts them into a directory called your_image_dir. Then, it moves all images that meach a filter criteria into a folder called filtered_images_dir. This project was created as my first coding experience in Python.

## Input:

ImageFilter.py "[search parameters]" [number of images]

Example Input:

ImageFilter.py "Zombie" 500

The exaple input would crawl Google images for the first 500 search results for "Zombie". The current filter would then attempt to filter out zombie images that are not green.
