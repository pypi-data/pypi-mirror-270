from setuptools import setup, find_packages

def readme(file_name):
    with open(file_name, 'r', encoding='utf-8') as f:
        README = f.read()
    return README

setup(
    name="UdemyCalculatorTeeru",
    version="1.0.0",
    packages=find_packages(include=["UdemyCalculator", "UdemyCalculator.*"]),
    install_requires=[],
    url="",
    LICENCE="MIT",
    author="Tribhuwan Yadav",
    description="A simple calculator package"    
)