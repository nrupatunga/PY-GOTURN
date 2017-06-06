# Date: Friday 02 June 2017 05:04:00 PM IST 
# Email: nrupatunga@whodat.com
# Name: Nrupatunga
# Description: Basic regressor function implemented

from __future__ import print_function
from logger import setup_logger
import os
import pdb


class tracker:
    """tracker class"""

    def __init__(self, show_intermediate_output=False):
        """TODO: to be defined. """
        self.show_intermediate_output = show_intermediate_output
