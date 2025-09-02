
from setuptools import setup, find_packages

setup(
    name="mcq-generator",
    version="0.0.1",
    author='jaya rani',
    author_email='ranijaya0292@gmil.com',
    packages=find_packages(),
    install_requires=[
        "openai",
        "langchain",
        "streamlit",
        "python-dotenv",
        "PyPDF2"
    ]
)