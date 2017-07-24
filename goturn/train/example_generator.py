# Date: Thursday 20 July 2017
# Email: nrupatunga@whodat.com
# Name: Nrupatunga
# Description: generating training examples for training

from ..helper.image_proc import image_proc


class example_generator:

    """Docstring for example_generator. """

    def __init__(self, lamda_shift, lamda_scale, min_scale, max_scale, logger):
        """TODO: to be defined1. """
        self.lamda_shift = lamda_shift
        self.lamda_scale = lamda_scale
        self.min_scale = min_scale
        self.max_scale= max_scale
        self.logger = logger


    def reset(self, bbox_curr, bbox_prev, img_curr, img_prev):
        """TODO: to be defined1. """
