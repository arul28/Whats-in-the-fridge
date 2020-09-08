from PIL import Image
import os

ingredientslist = os.listdir(r'C:/Users/sarve/Desktop/images1/') # Getting a list of the ingredients
for ingredient in ingredientslist:
    directory = r'C:/Users/sarve/Desktop/images1/' + ingredient + r'/' # Getting the working directory
    print(directory)
    directory2 = r"C:/Users/sarve/Desktop/newimages/" + ingredient + r'/' # Getting the output directory
    print(directory2)
    if not os.path.exists(directory2): # Making the directory if it does not exist
        os.mkdir(directory2)
    i = 1
    for file_name in os.listdir(directory): # Looping for each ingredient that we have
        if (file_name.endswith(".jpeg") or file_name.endswith('.png') or file_name.endswith(
                '.jpg')) and not file_name.startswith('._'): # Checking to make sure each image is a supported filetype
            try:
                im = Image.open(directory + file_name)
                name = ingredient + str(i) + '.jpg' # Converting each image to .jpg
                rgb_im = im.convert('RGB')
                rgb_im.save(directory2 + name)
                resize_im = Image.open((directory2 + name))
                resize_im = resize_im.resize((224, 224)) # Resizing each image to 224x224
                resize_im.save(directory2 + name) # Saving the new image in the output directory
                i += 1
                print(os.path.join(directory2, name))
            except Image.UnidentifiedImageError: # Ignore unidentified image errors
                continue
        else:
            continue
