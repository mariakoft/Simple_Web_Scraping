# -*- coding: utf-8 -*-
"""
Created on Tue Jun 12 02:58:20 2018

@author: Koft
"""

from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
from urllib.parse import urlparse
import os


website=input("Please type the url of the website you want to extract the links from:")
############Extract and print all links from a site
req = Request(website)  #download the webpage data 
html_page = urlopen(req)    

soup = BeautifulSoup(html_page, "lxml") #loads the data into a BeautifulSoup object

links = []                      #
for link in soup.findAll('a'):
    links.append(link.get('href'))

with open("links.txt", "a") as output:
    for item in links:
        output.write("{}\n".format(item))
    #output.write(str(links))
print (str(len(links)) +"   links found.")

#http://www.protagon.gr/

# use this image scraper from the location that 
#you want to save scraped images to

def make_soup(url):
    html = urlopen(url).read()
    return BeautifulSoup(html, "lxml")

def get_images(url):
    soup = make_soup(url)
    #this makes a list of bs4 element tags
    images = [img for img in soup.findAll('img')]
    print (str(len(images)) + "   images found.")
    #compile our unicode list of image links
    image_links = {each.get('src') for each in images} #gets the images path(link)
    filename={}
    for each in image_links:
       a = urlparse(each)
       filename[each]=os.path.basename(a.path)
       with open("image.txt",'w') as imagetxt:
           #imagetxt.write(str(image_links))
           [imagetxt.write('{0},{1}\n'.format(key, value)) for key, value in filename.items()]
           #imagetxt.write(str(filename))
    return image_links


get_images(website)








