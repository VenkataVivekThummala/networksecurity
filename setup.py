from setuptools import find_packages,setup

from typing import List

def get_requirements()->List[str]:
    
    ''' 
    This will return list of requirements
    '''
    requirements_lst:List[str]=[]
    try:
        with open('requirements.txt','r') as file:
            lines=file.readlines()

            for line in lines:
                requirements=line.strip()
                if requirements!=" " and requirements!='-e .':
                    requirements_lst.append(requirements)
    except FileNotFoundError:
        print("requirements file not found")

    return requirements_lst    

setup(
    name="NetworkSecurity",
    version="0.0.1",
    author="VenkataVivekVardhan Thummala",
    author_email="vivekthumala27@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements()
)