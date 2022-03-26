"""
settings.py
-----------
This module provides package constants.
By: Sebastian D. Goodfellow, Ph.D.
"""

# Import 3rd party libraries
import os

CDIR = os.getcwd()

PDIR = os.path.abspath(os.path.join(CDIR, os.pardir))


# Set working directory
WORKING_PATH = (
    os.path.abspath(os.path.join(PDIR, os.pardir))
    # os.path.dirname(
    #     os.path.dirname(
    #         os.path.realpath(__file__)
    #     )
    # )
)

# Set data directory
DATA_PATH = os.path.join(WORKING_PATH, 'dataset')

# Set base url
BASE_URL = 'http://pems.dot.ca.gov'

# Clearing house url
CLEARING_HOUSE_URL = '{}/?srq=clearinghouse&district_id={}&yy={}&type={}&returnformat=text'

# Set available districts
DISTRICTS = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
