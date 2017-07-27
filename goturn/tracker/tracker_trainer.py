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

        # In current batch
        self.images_batch_ = []
        self.targets_batch_ = []
        self.bbox_gt_scaled_batch_ = []

        # number of images in each batch
        self.kBatchSize = 50


    def make_training_examples(self):
        """TODO: Docstring for make_training_examples.
        :returns: TODO

        """
        example_generator = self.example_generator_
        image, target, bbox_gt_scaled = example_generator.make_true_example()

        self.images.append(image)
        self.targets.append(target)
        self.bbox_gt_scaled.append(bbox_gt_scaled)

        # Generate more number of examples
        self.images, self.targets, self.bbox_gt_scaled = example_generator.make_training_examples(self.kGeneratedExamplesPerImage, self.images, self.targets, self.bbox_gt_scaled)

    def train(self, img_prev, img_curr, bbox_prev, bbox_curr):
        """TODO: to be defined. """

        logger = self.logger
        example_generator = self.example_generator_
        example_generator.reset(bbox_prev, bbox_curr, img_prev, img_curr)
        self.make_training_examples()

        num_in_batch = len(self.images_batch_)
        num_left_in_batch = self.kBatchSize - num_in_batch
        num_use = min(len(self.images), num_left_in_batch)

        if num_use < 0:
            logger.error('Error: num_use = {}', num_use)
