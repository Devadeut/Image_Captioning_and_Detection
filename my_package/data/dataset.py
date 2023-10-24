import jsonlines
from PIL import Image
import os
import numpy as np

class Dataset(object):
    '''
        A class for the dataset that will return data items as per the given index
    '''

    def __init__(self, annotation_file, transforms=None):
        '''
            Arguments:
            annotation_file: path to the annotation file
            transforms: list of transforms (class instances)
                        For instance, [<class 'RandomCrop'>, <class 'Rotate'>]
        '''
        # Store the path to the annotation file
        self.annotation_file = annotation_file
        # Store the list of transforms
        self.transforms = transforms
        # Create an empty list to store the data items
        self.data = []
        # Open the annotation file and read the data items into the list
        with jsonlines.open(annotation_file) as reader:
            for obj in reader:
                self.data.append(obj)
    
    def __len__(self):
        '''
            return the number of data points in the dataset
        '''
        # Return the length of the data list
        return len(self.data)

    def __getitem__(self, idx):
        '''
            return the data items for the index idx as an object
        '''
        # Get the path to the image for the given index
        path = self.data[idx]['path']
        # Get the transformed image for the given path
        image = self.__transformitem__(path)
        # Return the transformed image
        return image

    def __transformitem__(self, path):
        '''
            return transformed PIL Image object for the image in the given path
        '''
        # Open the image using PIL
        image = Image.open(path)
        # If there are transforms, apply each one to the image
        if self.transforms:
            for t in self.transforms:
                image = t(image)
        # Return the transformed image
        return image
