

def jpg_to_png(filename):
    """This function converts jpg to png-Insert the file name as input..."""
    img = open(f"{filename}.jpg")
    img.save(f"{filename}.png")
    print("Conversion to PNG successful")

def png_to_jpg(filename):
    """This function converts png to jpg-Insert the file name as input..."""
    img = open(f"{filename}.png")
    img.save(f"{filename}.jpg")
    print("Conversion to JPG successful")
