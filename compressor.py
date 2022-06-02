from statistics import quantiles
from PIL import Image
import sys


if len(sys.argv) != 2:
    print("USAGE: python compressor.py <image_name>")
    sys.exit(1)

#convert to JPG
try:
    image = Image.open(sys.argv[1])    
except:
    print("please put the image in the same directory and type the correct name with the extension")
    sys.exit(1)

image = image.convert("RGB")
image.save("NEW.jpg", quality=30)

print("successfully reduce")