#Build ML application as package.

from typing import List
from setuptools import find_packages,setup

def get_requirements(path:str)->List[str]:
    '''
    this function returns list of requirements
    '''
    requirements=[]
    with open (path) as obj:
        requirements = obj.readlines()
        requirements = [req.replace("\n","") for req in requirements]
        
        if '-e .' in requirements:
            requirements.remove('-e .')

setup(
name='mlproject',
version='0.0.1',    
author='Chaitanya',
author_email = 'ramtirtha.chaitanya@gmail.com'    ,
packages=find_packages(),
install_requires=get_requirements('requirements.txt')
)