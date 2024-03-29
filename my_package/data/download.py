from tokenize import Imagnumber
from urllib import response
from PIL import Image
import requests
from io import BytesIO

class Download(object):
    '''
        A class for helping in dowloading the required images from the given url to the specified path
    '''

    def __call__(self, path, url):
        '''
            Arguments:
            path: download path with the file name
            url: required image URL
        ''' 
        response = requests.get(url)
        image = Image.open(BytesIO(response.content))
        image.save(path)
