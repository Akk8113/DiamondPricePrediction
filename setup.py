from setuptools import find_packages,setup
from typing import List

git remote set-url origin https://github.com/Akk8113/DiamondPricePrediction.git

HYPEN_E_DOT = '-e .'


def get_requirements(file_path:str)->List[str]:
    requirements=[]
    with open(file_path) as file_obj:
        requirements = file_obj.readline()
        requirements = [req.replace("/n","") for req in requirements]
  
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
        return requirements

setup(
    name = 'DiamondPricePrediction',
    version= '0.0.1',
    author = 'Arpit',
    author_email = 'arpit.kakaiya8@gmail.com',
    install_requires = get_requirements('requirements.txt'),
    packages=find_packages()
)