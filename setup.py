import setuptools
from setuptools import setup, find_packages

setuptools.setup(
    name='Widgets1.1',
#     version='0.0.3',
    author='Hrishikesh',
    author_email='hrishikeshkarande2020@gmail.com',
    url='https://github.com/hrishi483/Widgets1.1.git',
    packages=find_packages(),
    install_requires=['panel','ipywidgets','openai','langchain','dotenv']
)
