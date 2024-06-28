from setuptools import setup ,find_packages

from pkg_resources import parse_requirements

def read_requirements(file):
    with open(file, encoding='utf-8') as f:
        return f.read().splitlines()


setup(
   name='chatbot',
   version='1.0',
   description='A Fitness Rag Chatbot',
   author='Abdullah Jumaa',
   author_email='abdullah.m.jumaa@gmail.com',
   packages=find_packages(),  
   install_requires=read_requirements('requirements.txt'),
)

