# Importing necessary libraries
from PIL import Image, ImageEnhance, ImageFilter #PIL: Python Imaging Library. It is a library for opening, manipulating, and saving many different image file formats.
import os

# Setting the path to the folder with images to be edited and the path to the output folder
path='./imgs'
pathOut='/editedImgs'

# Looping through all files in the specified folder
for filename in os.listdir(path):

    # Opening the image file
    img=Image.open(f'{path}/{filename}')

    # Applying a sharpen filter and converting the image to black and white.
    # edit=img.filter(ImageFilter.SHARPEN).convert('L')

    # Applying a Gaussian blur filter to the image
    edit = img.filter(ImageFilter.GaussianBlur(radius=2))
    
    # Applying an emboss filter to the image
    # edit = img.filter(ImageFilter.EMBOSS)

    # Enhancing the contrast of the image
    factor=1.5
    enhancer=ImageEnhance.Contrast(edit)
    edit=enhancer.enhance(factor)
    
    # Extracting the file name without the extension
    clean_name=os.path.splitext(filename)[0]

    # Saving the edited image in the output folder with the file name indicating it has been edited
    edit.save(f'.{pathOut}/{clean_name}_edited.jpg')
