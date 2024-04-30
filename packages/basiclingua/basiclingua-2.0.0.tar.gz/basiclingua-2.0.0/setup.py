from setuptools import setup, find_packages
import os

here = os.path.abspath(os.path.dirname(__file__))

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

VERSION = '2.0.0'
DESCRIPTION = 'A Python library based on various LLMs to perform basic and advanced natural language processing (NLP) tasks'

# Setting up
setup(
    name="basiclingua",
    version=VERSION,
    author="Fareed Hassan Khan",
    author_email="<fareedhassankhan12@gmail.com>",
    description=DESCRIPTION,
    long_description=read('README.md'),
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=["google-generativeai", "grpcio", "grpcio-tools", "openai", "emoji", "PyMuPDF"],  # Add any dependencies here
    keywords=['python', 'NLP', 'Natural Language Processing', 'Linguistics', 'Gemini LLM', 'Google Gemini LLM'],
    classifiers=[
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ]
)