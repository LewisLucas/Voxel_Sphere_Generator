from PIL import Image


image = Image.new("RGB", (10, 10), (255, 0, 0))
for i in range(10):
    image.putpixel((i, 0), (255, 255, 255))

for i in range(10):
    image.putpixel((i, 9), (255, 255, 255))

for i in range(10):
    image.putpixel((0, i), (255, 255, 255))

for i in range(10):
    image.putpixel((9, i), (255, 255, 255))



image.save("block_template.png")
