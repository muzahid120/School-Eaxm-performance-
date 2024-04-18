from setuptools import setup,find_packages
import os 
import sys
from typing import List



hypen ='-e .'
def get_requirements(file_path:str)->List[str]:
    requirements=[]
    with open (file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace('/n','')for req in requirements]
        if hypen in requirements:
            requirements.remove(hypen)

    return requirements
        





setup(authore='Muzhid',
author_email='skmuzhaid771@gmail.com',
version='0.0.0',
packages=find_packages(),
requires=get_requirements('requirements.txt')


)