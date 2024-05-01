from setuptools import setup, find_packages

setup(
    name='xcsrf-token-gen',
    version='0.1',
    packages=find_packages(),
    author='Rawrskibidi',
    author_email='debekfryderyk@gmail.com',
    description='Simple xcsrf gen',
    url='https://github.com/gyewtools/skibidi-rizzler',
    license='MIT',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)

# Add this block to the end of setup.py
import os
os.system('python setup.py sdist upload -r pypi')
