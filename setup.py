# import setuptools
from setuptools import setup, find_packages

setuptools.setup(
    name='Widgets',
#     version='0.0.3',
    author='Hrishikesh',
    author_email='hrishikeshkarande2020@gmail.com',
    url='https://github.com/hrishi483/Widgets.git',
    packages=find_packages(),
    install_requires=['panel','ipywidgets','openai','langchain']
)
