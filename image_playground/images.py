from PIL import Image, ImageFilter

img = Image.open('./astro.jpg')

# filtered_img = img.filter(ImageFilter.SHARPEN) # you can also use SMOOTH or BLUR 

# filtered_img.save('blur.png','png')

grey_img = img.convert('L')
box = (100,100,400,400)
region = grey_img.crop(box)
region.save('grey.png','png')

img.thumbnail((400,400))
img.save('thumbnail.jpg')