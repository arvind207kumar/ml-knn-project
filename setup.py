from setuptools import find_packages,setup
from typing import List

HUPEN_E_DOT ='-e .'

def get_requirements(file_path:str)->str:
     '''
     this function will return the list of requirements
     '''
     requirements=[]
     with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements= [req.replace("\n","")for req in requirements]

        if HUPEN_E_DOT in requirements:
            requirements.remove(HUPEN_E_DOT)

     return requirements


setup(
name = 'Knn ML project',
version = '0.0.1',
author = 'Arvind',
author_email = '121ad0042@iiitk.ac.in',
packages = find_packages(),
install_requires =get_requirements('requirements.txt')
)