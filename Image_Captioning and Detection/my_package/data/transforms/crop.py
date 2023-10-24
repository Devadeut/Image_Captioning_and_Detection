from PIL import Image
import numpy as np
import random

class CropImage(object):
    '''
        Performs either random cropping or center cropping.
    '''

    def __init__(self, shape, crop_type='center'):
        '''
            Arguments:
            shape: output shape of the crop (h, w)
            crop_type: center crop or random crop. Default: center
        '''
        self.shape=shape
        self.crop_type=crop_type

    def __call__(self, image):
        '''
            Arguments:
            image (numpy array or PIL image)

            Returns:
            image (numpy array or PIL image)
        '''
        image=Image.open(object)
        
        w, h = image.size
        crop_h, crop_w = self.shape
        if self.crop_type == 'center':
            left = (w - crop_w) // 2
            right = (w + crop_w) // 2
            top = (h - crop_h) // 2
            bottom = (h + crop_h) // 2
        elif self.crop_type == 'random':
            left = random.randint(0, w - crop_w)
            right = left + crop_w
            top = random.randint(0, h - crop_h)
            bottom = top + crop_h
        else:
            raise ValueError("Invalid crop type specified. Use 'center' or 'random'.")
        
        im = image.crop((left, top, right, bottom))
        im.show()

        

 