from setuptools import setup,find_packages
from typing import List


#Declaring variables for setup functions
PROJECT_NAME = "flightfare-predictor"
VERSION = "0.0.1"
AUTHOR = "M Saritha"
DESCRIPTION =" This is a project which predicts the flight fare"
REQUIREMENT_FILE_NAME = "requirements.txt"

def get_requirements_list()->List[str]:
    """ 
    Description: This function reads requirements.txt  and returns list of 
    requirement mentioned in requirements.txt 
    
    returns This function is going to return a list which contain 
    name of libraries mentioned in requirements.txt file
    eg. ["numpy","sklearn","pandas",....]
    """
    with open(REQUIREMENT_FILE_NAME) as requirement_file:
        return requirement_file.readlines().remove("-e .")


setup(
name = PROJECT_NAME,
version = VERSION,
author = AUTHOR,
description = DESCRIPTION,
package = find_packages(),
install_requires = get_requirements_list()
)

