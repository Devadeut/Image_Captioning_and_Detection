#Imports
from PIL import Image

class FlipImage(object):
    '''
        Flips the image.
    '''

    def __init__(self, flip_type='horizontal'):
        '''
            Arguments:
            flip_type: 'horizontal' or 'vertical' Default: 'horizontal'
        '''
        self.flip_type=flip_type

    def __call__(self, image):
        '''
            Arguments:
            image (numpy array or PIL image)

            Returns:
            image (numpy array or PIL image)
        '''
        image=Image.open(object)
        if(self.flip_type=='horizontal'):
            im=image.transpose(Image.FLIP_LEFT_RIGHT)
            im.show()
        elif(self.flip_type=='vertical'):
            im=image.transpose(Image.FLIP_TOP_BOTTOM)   
            im.show()
        else:
            raise ValueError("Invalid crop type specified. Use 'horizontal' or 'verticle'.")    

        return