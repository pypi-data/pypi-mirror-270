from setuptools import setup, find_packages
setup(
name='eqsolver',
version='0.1.0',
author='Brigham Turner',
author_email='brighamturner12@gmail.com',
description='Define model from system of equations, algebraically solve for variables, calculate boiling point, latent heat, other physics gas concepts',
packages=find_packages(),
classifiers=[
'Programming Language :: Python :: 3',
'License :: OSI Approved :: MIT License',
'Operating System :: OS Independent',
],
python_requires='>=3.6',
)