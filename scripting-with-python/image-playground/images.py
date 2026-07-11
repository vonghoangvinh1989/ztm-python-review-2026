from PIL import Image, ImageFilter

img = Image.open("./Pokedex/pikachu.jpg")
# filtered_img = img.filter(ImageFilter.SHARPEN)
# filtered_img.save("blur.png", "png")

converted_img = img.convert("L")

box = (100, 100, 400, 400)
region = converted_img.crop(box)
region.save("grey.png", "png")

# crooked = converted_img.rotate(90)
# crooked.save("grey.png", "png")

# resize = converted_img.resize((300, 300))
# resize.save("grey.png", "png")
