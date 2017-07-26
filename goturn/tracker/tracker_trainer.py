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
        self.kGeneratedExamplesPerImage = 10
        self.logger = logger
        self.images = []
        self.targets = []
        self.bbox_gt_scaled = []


    def make_training_examples(self):
        """TODO: Docstring for make_training_examples.
        :returns: TODO

        """
        example_generator = self.example_generator_
        image, target_pad, bbox_curr_gt_recentered = example_generator.make_true_example()

        self.images.append(image)
        self.targets.append(target_pad)
        self.bbox_gt_scaled.append(bbox_curr_gt_recentered)

    def train(self, img_prev, img_curr, bbox_prev, bbox_curr):
        """TODO: to be defined. """

        example_generator = self.example_generator_
        example_generator.reset(bbox_prev, bbox_curr, img_prev, img_curr)
        self.make_training_examples()
