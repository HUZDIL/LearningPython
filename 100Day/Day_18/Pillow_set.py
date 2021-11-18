from PIL import Image, ImageFilter


image = Image.open("Kemal-Ataturk.jpg")
#print(image.show())

#print(image.rotate(180).show())

print(image.filter(ImageFilter.GaussianBlur(3)).show())

