# Date: Friday 21 July 2017
# Email: nrupatunga@whodat.com
# Name: Nrupatunga
# Description: training tracker


class tracker_trainer:

    """Docstring for tracker_trainer. """

    def __init__(self, example_generator, regressor_train):
        """TODO: to be defined1. """

        self.example_generator_ = example_generator
        self.regressor_train_ = regressor_train
        self.num_batches_ = 0
