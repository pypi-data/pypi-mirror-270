from setuptools import setup, find_packages
import os

# Get the current directory
here = os.path.abspath(os.path.dirname(__file__))

# Function to collect all files and directories under oscb folder
def find_oscb_contents():
    oscb_contents = []
    for root, dirs, files in os.walk(os.path.join(here, 'oscb')):
        for file in files:
            oscb_contents.append(os.path.relpath(os.path.join(root, file), here))
        for dir in dirs:
            oscb_contents.append(os.path.relpath(os.path.join(root, dir), here))
    return oscb_contents

# Include the oscb/download_dataset directory as well
oscb_contents = find_oscb_contents()
oscb_contents.extend(['oscb/download_dataset/*'])  # Include the download_dataset folder and its contents

setup(
    name='oscb',
    version='1.1.9',
    description='Description of your package',
    long_description='Long description of your package',
    long_description_content_type='text/markdown',
    url='https://github.com/your_username/oscb',
    author='Your Name',
    author_email='your.email@example.com',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    keywords='sample setuptools development',
    packages=find_packages(),
    package_data={'oscb': oscb_contents},  # Specify package data directly
    include_package_data=True,
    install_requires=[
        'torch>=1.6.0',
        'numpy>=1.16.0',
        'tqdm>=4.29.0',
        'scikit-learn>=0.20.0',
        'pandas>=0.24.0',
        'six>=1.12.0',
        'urllib3>=1.24.0',
        'outdated>=0.2.0',
        'joblib>=1.3.2'
    ],
)
