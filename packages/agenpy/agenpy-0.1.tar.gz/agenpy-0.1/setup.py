from setuptools import setup

with open("README.md", 'r') as f:
    long_description = f.read()

setup(
   name='agenpy',
   version='0.1',
   description='A python package for setting up agentic behavior for LLMs. Includes optimization for large training data, and adherence to applied interactional policies.',
   license="Apache-2.0",
   long_description=long_description,
   author='Octran Technologies',
   author_email='contact@octran.tech',
   packages=['agenpy'],  #same as name
   install_requires=[], #external packages as dependencies
)