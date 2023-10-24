#Imports
from PIL import Image


class RescaleImage(object):
    '''
        Rescales the image to a given size.
    '''

    def __init__(self, output_size):
        '''
            Arguments:
            output_size (tuple or int): Desired output size. If tuple, output is
            matched to output_size. If int, smaller of image edges is matched
            to output_size keeping aspect ratio the same.
        '''
        self.output_size=output_size


    def __call__(self, image):
        '''
            Arguments:
            image (numpy array or PIL image)

            Returns:
            image (numpy array or PIL image)

            Note: You do not need to resize the bounding boxes. ONLY RESIZE THE IMAGE.
        '''
        
        image=Image.open(object)
        width,height=image.size
        d=min(image.size)
        r=(self.output_size/d)


        if(type(self.output_size)==tuple):
            im=image.resize(self.output_size)
         
        elif(type(self.output_size)==int):
            im=image.resize(width*r,height*r)  

        im.show()     

        

