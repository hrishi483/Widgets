import setuptools
from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='Widgets1.1',
#     version='0.0.3',
    author='Hrishikesh',
    author_email='hrishikeshkarande2020@gmail.com',
    description='Testing installation of Package',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/hrishi483/Widgets1.1.git',
    packages=find_packages(),
    install_requires=['panel','ipywidgets','openai','dotenv','langchain'],
)
