from PIL import Image
from pathlib import Path

resize_factor = 2
base_path = Path('./../pictures/Originals')

for image_path in base_path.glob('*.png'):
    img = Image.open(image_path)
    size = img.size
    new_size = (int(size[0] / resize_factor), int(size[1] / resize_factor))
    print('Original size was: {}'.format(size))
    print('New size is: {}'.format(new_size))
    img = img.resize(new_size)
    save_path = './../pictures/2xSmallerOriginals/' +  str(image_path.name)
    print('Saving at {}', format(save_path))
    img.save(save_path)