from setuptools import setup

setup(
    name='DICOMParts',
    version='0.1.0',
    description='A set of parts for working with DICOM',
    author='Steve Pieper',
    author_email='pieper@isomics.com',
    url='https://github.com/pieper/DICOMParts',
    packages=['DICOMParts'],
    install_requires=[
        'pydicom',
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Topic :: Scientific/Engineering :: Medical Science Apps.',
    ],
)
