from setuptools import setup, find_packages

setup(
    name='techdom',
    version='1.0.0',
    packages=find_packages(),
    author='abc',
    author_email='dragonslayer461313@gmail.com',
    description='Simple library for techdoms',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/FranklyShovelTrap/TechdomLibrary',
    install_requires=[
        'screeninfo',
        'pillow',
        'pyttsx3',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
    ],
)
