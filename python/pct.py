#  py pct.py
# This line imports or includes the library we will need
from PIL import Image

# This line opens the image and loads it into a variable called "image_original"
image_original = Image.open("cat_small.jpg")

print(image_original.size)
print(image_original.format)

pixels_original = image_original.load()

width, height = image_original.size
print(f"Width: {width}")
print(f"Height: {height}")

green = (66, 229, 24)

if pixels_original == (66, 229, 24):
    pixels_original(255, 0, 255)

image_original.show()

#image_original.show()

#r, g, b = pixels_original[100, 200]