from PIL import Image, UnidentifiedImageError
import pytesseract as pt 
import os, re, shutil
from tqdm import tqdm 
from datetime import datetime

# These are the options you can specify according to your needs
# Specify the path for the folder containing the images to be searched
search_path = "/path/for/images/to-be-search/"
# Specify the path for the folder to save images containing the text
found_path = "/path/for/images/found/"
# Specify the text to search in images
search_text = ""    
# Specify the path for the tesseract executable
pt.pytesseract.tesseract_cmd = r'<full_path_to_your_tesseract_executable>'

def count_images(path, image_path_list):
    """This function calculates and returns the total number of images found
     in the folder containing the images to be searched. It also appends their
     full path to a list"""
    number_of_files = 0
    for subdir, dirs, files in os.walk(search_path):
        for imageName in files:
            if imageName.lower().endswith(('.png', '.jpg', '.jpeg', '.tiff', \
                 '.bmp', '.gif')):
                # If the file has an image extension, increment the counter 
                # and append full path of the image to image_path_list 
                number_of_files += 1
                image_path_list.append(os.path.join(subdir, imageName))
    return number_of_files

def main(): 
    # A list to store full paths of the images in the search_path.
    image_path_list = []
    
    # Count and print the total number of files in path
    number_of_files = count_images(search_path, image_path_list)
    print(number_of_files, " image(s) found in the directory: ", search_path)

    with tqdm(total=number_of_files) as pbar:
        # Initialize the progress bar
        for image_path in image_path_list:
            # Iterate over the path images in image_path_list
            try:
                # Check if the image is valid or not
                img = Image.open(image_path)    
            except UnidentifiedImageError:
                # Print an error message and the file path
                print("Unidentified image error for the file: ", image_path)
                pbar.update(1)
                continue

            # Applying OCR using pytesseract for python 
            image_text = pt.image_to_string(img, lang ="eng") 

            if re.search(search_text, image_text): 
                # If the text extracted from the image includes the 
                # search_text copy the image to found_path
                shutil.copy2(image_path, found_path)

            # Update the progress bar
            pbar.update(1)        

if __name__ == '__main__': 
    main() 
