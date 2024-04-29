from setuptools import setup, find_packages

setup(
    name='Rajsaro',
    version='1.1',
    packages=find_packages(),
    author='RajsaroITSolutions',
    author_email='rajsaroitsolutions@gmail.com',
    description='Python package for extracting information from various documents like Aadhar card, '
                'Covid certificate, GST certificate, PAN card, Passport, PDF to Image, and Voter ID card.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/Gokul-RS16/RS_LIB/tree/master/Rajsaro',
    license='MIT',
    include_package_data=True,
    package_data={
        '': ['models/*.pt'],  # Include all .pt files in the models directory
    },
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Programming Language :: Python :: 3.13',
    ],
    install_requires=[
        'torch',  # Assuming PyTorch is needed to load the model
        'setuptools',  # setuptools is required for pkg_resources
        'Flask == 3.0.3',
        'pytesseract == 0.3.10',
        'opencv-python == 4.9.0.80',
        'matplotlib == 3.8.4',
        'easyocr == 1.7.1',
        'torch == 2.2.2',
        'torchvision == 0.17.2',
        'torchaudio == 2.2.2',
        'ultralyticsplus == 0.1.0',
        'pdf2image == 1.17.0',
    ],
    python_requires='>=3.8',  # Specify the minimum Python version required
)
