#filename: py w8p.py
#student: Jeremias Moracca
from PIL import Image

image_earth = Image.open('earth.jpg')
image_cat = Image.open('cat.jpg')
image_new = Image.new("RGB", image_earth.size)
pixels_new = image_new.load()

pixels_earth = image_earth.load()
pixels_cat = image_cat.load()
print('load succesful')

width,height = image_earth.size
print(f'Width: {width}')
print(f'Height: {height}')

for x in range(0, width):
    for y in range(0, height):
        (r, g, b) = pixels_cat[x,y]
        if r <= 150 and g >= 215 and b <= 60:
            pixels_cat[x,y] = pixels_earth[x,y]
        elif r <= 130 and g >= 200 and b <= 130:
            pixels_cat[x,y] = pixels_earth[x,y]
        
        
        pixels_new[x,y] = pixels_cat[x,y]
image_new.save('spacecat.jpg')
image_new.show()







#cat_width, cat_height = image_cat.size
#print(f'Width: {cat_width}')
#print(f'Height: {cat_height}')

#lines to show me the image
#image_earth.show()
#image_cat.show()