import sys
import urllib.request
import json
import requests
import PIL
import os
import io
from PIL import Image
# Fetch parameters from the command line
# Make sure there are only 4 parameters!
# 5 because position 0 == the application name

#print ('Argument List:', str(sys.argv))
 
# Read the API KEY from the file somewhere
#starting at 1


# Get the center location of the city.
lati=""
long=""
def getMap(city,apiKey):
  url = 'https://api.tomtom.com/search/2/search/'+city+'.json?idxSet=Geo&key='+apiKey
  print ( url )

  req = urllib.request.urlopen(url)
  data = req.read().decode('utf-8')
  #print(data)
  # Convert data into JSON
  obj = json.loads(data)

  if (len(obj["results"]) == 0):
    print ('City not found')
    quit()

  print('Found city center of '+city+' at '+ str(obj["results"][0]["position"]))
  lat = obj["results"][0]["position"]["lat"]
  lon = obj["results"][0]["position"]["lon"]


  #switch case dictionary indicates the sizes for each image specification

  # Create API CALL to 'static image'
  #switcher is called passing in size to let command arg input choose size

  urlStaticImage = f"https://api.tomtom.com/map/1/staticimage?center={lon},{lat}&zoom=8&key={apiKey}"
  print(urlStaticImage)
  # Save image to a file ..
  imageRequest = urllib.request.urlopen(urlStaticImage)
  response = requests.get(urlStaticImage)
  image_bytes = io.BytesIO(response.content)

  img = PIL.Image.open(image_bytes)
  img.save("tempimg.png","PNG")
  global lati
  lati=lat
  global long
  long=lon

 # sys.stdout.buffer.write(imageBinary)