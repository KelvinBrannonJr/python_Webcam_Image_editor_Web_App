from PIL import Image


def convert_image(input_image):
    # Create image instance using 'Pillow' module
    img = Image.open(input_image)

    # Convert image instance into grayscale
    gray_img = img.convert("L")
    return gray_img
