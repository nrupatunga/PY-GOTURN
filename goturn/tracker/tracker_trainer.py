# Date: Sunday 23 July 2017
# Email: nrupatunga@whodat.com
# Name: Nrupatunga
# Description: tracker trainer

from ..train.example_generator import example_generator

class tracker_trainer:
    """tracker trainer class"""

    def __init__(self, example_generator, regressor_train, logger):
        """TODO: to be defined. """

        self.example_generator_ = example_generator
        self.regressor_train_ = regressor_train
        self.num_batches_ = 0
        self.logger = logger


    def train(self, img_prev, img_curr, bbox_prev, bbox_curr):
        """TODO: to be defined. """
