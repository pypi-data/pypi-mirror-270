from setuptools import setup, find_packages

setup(
    name='model_paclone_daredata',
    version='0.1.0',
    author='João Sanches',
    author_email='youremail@example.com',
    description='model',
    packages=find_packages(),
    install_requires=[
        'numpy',
        'pandas',
        'nltk',
        'scikit-learn',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.9',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)