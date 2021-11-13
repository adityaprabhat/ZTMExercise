from PIL import Image, ImageFilter

image = Image.open("./Pictures/pikachu.jpg")
formatted_image = image.convert("L")
formatted_image.save("grey.png","png")
formatted_image.show()


print(image)