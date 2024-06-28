from setuptools import setup ,find_packages

from pkg_resources import parse_requirements

with open('requirements.txt') as f:
    requirements = [str(req) for req in parse_requirements(f)]

setup(
   name='chatbot',
   version='1.0',
   description='A Fitness Rag Chatbot',
   author='Abdullah Jumaa',
   author_email='abdullah.m.jumaa@gmail.com',
   packages=find_packages(),  
   install_requires=requirements,
)

