
#Imports
from my_package.model import ImageCaptioningModel
from my_package.data import Dataset, Download
from my_package.data.transforms import FlipImage, RescaleImage, BlurImage, CropImage, RotateImage
import numpy as np
from PIL import Image
import os

def experiment(annotation_file, captioner, transforms, outputs):
    '''
        Function to perform the desired experiments

        Arguments:
        annotation_file: Path to annotation file
        captioner: The image captioner
        transforms: List of transformation classes
        outputs: Path of the output folder to store the images
    '''

    #Create the instances of the dataset, download
    dataset = Dataset(annotation_file, transforms)
    download = Download()


    #Print image names and their captions from annotation file using dataset object
    for x in range(len(dataset)):
        print(dataset.data[x]["file_name"],dataset.data[x]["captions"])

    #Download images to ./data/imgs/ folder using download object
    for i in range(len(dataset)):
        download('./data/imgs/'+dataset.data[i]["file_name"])

    #Transform the required image (roll number mod 10) and save it seperately
    i = 1 # 21%10
    # replace this with your desired index
    img_path = os.path.join('./data/imgs/', dataset.data[i]["file_name"])
    img = Image.open(img_path)
    img = dataset.__transformitem__(img)
    img.save('./data/imgs/transformed.jpg')

    #Get the predictions from the captioner for the above saved transformed image  
    predictions = captioner('./data/imgs/transformed.jpg',3)
    print(predictions)

def main():
    captioner = ImageCaptioningModel()
    experiment('./data/annotations.jsonl', captioner, [FlipImage(), BlurImage(1)], None) # Sample arguments to call experiment()


if __name__ == '__main__':
    main()
