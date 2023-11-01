Image Captioning project during Semester 
## Image Captioning

 Image Captioning is the process of generating textual description of an image. You have to create a python package for transforming images and analysing their effect on the captions of an image captioning model. We are providing you with a pretrained captioning model, all you need to do is to call the model on the image and get the outputs.

A python package means that one can install the package in the python environment and can import the modules in any python script, irrespective of the location of the script. Creating a python package is fairly easy, just follow the steps [here](https://packaging.python.org/tutorials/packaging-projects/).

## Installation instructions

Note: To install the dependencies you need to run the following commands:
 - `pip install -r requirements.txt`
 - `python3 -m spacy download en_core_web_sm`
 - Download LAVIS zip into the project directory from https://github.com/salesforce/LAVIS, Unzip LAVIS-main.zip and install lavis using the following commands 
    * `cd LAVIS-main/`
    * `pip install .`

## File descriptions

1. `main.py`: This is the main file which is to be called to execute the program. The main file calls the corresponding functions as needed while execution. The main file should call the appropriate function to prepare the dataset, then transform the images read, obtain the captions in the image by calling the captioner model, and then plot the obtained images by calling the appropriate functions from the package described below.

2. `./my_package/model.py`: This file contains the image captioning model definition. Consider it as a black-box model which takes an image and number of captions to be generated as input and provides the captions as output.

&nbsp;
<p align="center">
<img src='./sample_imgs/picandcaptions.png' width=400>
</p>
<p align="center">
<b>Fig. 1</b>. Sample Output of the Captioner. </p>
&nbsp;


3. `./my_package/data/dataset.py`: This file contains the class ```Dataset``` that reads the provided dataset from the annotation file and provides the  transformed image object. The annotation format is provided in `data/README.md`

4. `./my_package/data/transforms`: This folder contains 5 files. Each of these files is responsible for performing the corresponding transformation, as follows:
	
a) `crop.py`: This file takes an image as input and crops it based on the provided arguments. Declare a class `CropImage()` for performing the operation. 

&nbsp;
<p align="center">
<img src='./sample_imgs/crop.png' width=400>
</p>
<p align="center">
<b>Fig. (a)</b>. Crop Operation. </p>
&nbsp;
	
b) `flip.py`: This file takes an image as input and flips it based on the provided arguments. Declare a class `FlipImage()` for performing the operation. 

&nbsp;
<p align="center">
<img src='./sample_imgs/flip.png' width=400>
</p>
<p align="center">
<b>Fig. (b)</b>. Flip Operation. </p>
&nbsp;
	
c) `rotate.py`: This file takes an image as input and rotates it based on the provided arguments. Declare a class `RotateImage()` for performing the operation. 

&nbsp;
<p align="center">
<img src='./sample_imgs/rotate.png' width=400>
</p>
<p align="center">
<b>Fig. (c)</b>. Rotate Operation. </p>
&nbsp;

d) `rescale.py`: This file takes an image as input and rescales it based on the provided arguments. Declare a class `RescaleImage()` for performing the operation. 

&nbsp;
<p align="center">
<img src='./sample_imgs/rescale.png' width=400>
</p>
<p align="center">
<b>Fig. (d)</b>. Rescale Operation. </p>
&nbsp;

e) `blur.py`: This file takes an image as input and applies a gaussian blur to it based on the provided arguments. Declare a class `GaussBlurImage()` for performing the operation. 

&nbsp;
<p align="center">
<img src='./sample_imgs/blur.png' width=400>
</p>
<p align="center">
<b>Fig. (e)</b>. Blur Operation. </p>
&nbsp;

5. `./my_package/data/download.py` : This file takes in url (to download the image) and path (to store the downloaded image).

6. `setup.py`: Use this file for constructing the package `my_package`.


