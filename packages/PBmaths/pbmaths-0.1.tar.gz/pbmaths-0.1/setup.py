from setuptools import setup, find_packages

setup(
    name='PBmaths',  # Package name
    version='0.1',  # Update with your package's version number
    packages=find_packages(),
    description='Basic arithmetic operations package',
    long_description=open('README.md').read(),  # Read your README file
    long_description_content_type='text/markdown',
    author='Prakrititz Borah',
    author_email='Prakrititz.Borah@iiitb.ac.in',
    url='https://github.com/SweetBunny123/PrakBasicMaths',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
)
