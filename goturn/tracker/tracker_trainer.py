# Date: Sunday 23 July 2017
# Email: nrupatunga@whodat.com
# Name: Nrupatunga
# Description: tracker trainer

from ..helper import config


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
        if config.DEBUG:
            self.kBatchSize = self.kGeneratedExamplesPerImage + 1
        else:
            self.kBatchSize = 50

    def process_batch(self):
        """TODO: Docstring for process_batch.
        :returns: TODO

        """
        self.regressor_train_.train(self.images_batch_, self.targets_batch_,
                                    self.bbox_gt_scaled_batch_)

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

        while len(self.images) > 0:
            num_in_batch = len(self.images_batch_)
            num_left_in_batch = self.kBatchSize - num_in_batch
            num_use = min(len(self.images), num_left_in_batch)

            if num_use < 0:
                logger.error('Error: num_use = {}', num_use)

            self.images_batch_.extend(self.images[0:num_use])
            self.targets_batch_.extend(self.targets[0:num_use])
            self.bbox_gt_scaled_batch_.extend(self.bbox_gt_scaled[0:num_use])

            if (len(self.images_batch_) == self.kBatchSize):
                self.num_batches_ = self.num_batches_ + 1
                self.process_batch()

                self.images, self.targets, self.bbox_gt_scaled = [], [], []
                self.images_batch_, self.targets_batch_, self.bbox_gt_scaled_batch_ = [], [], []

            self.images = self.images[num_use:]
            self.targets = self.targets[num_use:]
            self.bbox_gt_scaled = self.bbox_gt_scaled[num_use:]
