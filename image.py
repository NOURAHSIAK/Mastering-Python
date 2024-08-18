from PIL import Image
myimage = Image.open(r"C:\Users\kaisb\OneDrive\Documents\GitHub\Mastering-Python\__pycache__\Picture1.png")
# myimage.show()
# mybox = (200, 200, 400, 400)
# mycroppedimage = myimage.crop(mybox)
# mycroppedimage.show()
newimage = myimage.convert("L")
newimage.show()