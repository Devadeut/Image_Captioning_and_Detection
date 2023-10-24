from setuptools import setup, find_packages

setup(

    name='my_package',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[

       'numpy',
       'opencv-python'
    ],
    author='Devashri',
    author_email='deulkardr@gmail.com',
    description='A package for image transformation'

)