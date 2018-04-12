# Date: Thursday 20 July 2017
# Email: nrupatunga@whodat.com
# Name: Nrupatunga
# Description: 

import sys
import numpy as np
from regressor import regressor
from ..helper import config
sys.path.insert(0, config.CAFFE_PATH)
import caffe
# __import__('pdb').set_trace()
# from visdom import Visdom
# viz = Visdom()

class regressor_train:

    """Docstring for regressor_train. """

    def __init__(self, deploy_proto, caffe_model, gpu_id, solver_file, logger):
        """TODO: to be defined1. """

        self.kDoTrain = True
        self.kNumInputs = 3
        objRegressor = regressor(deploy_proto, caffe_model, gpu_id,
                self.kNumInputs, self.kDoTrain, logger, solver_file)
        self.regressor = objRegressor
        self.logger = logger
        self.solver = objRegressor.solver

    def set_boxes_gt(self, bboxes_gt):
        """TODO: Docstring for set_boxes_gt.
        :returns: TODO
        """
        num_images = len(bboxes_gt)
        input_dims = 4
        net = self.regressor.net

        net.blobs['bbox'].reshape(num_images, input_dims, 1, 1)

        for i in range(num_images):
            bbox_gt = bboxes_gt[i]
            bbox = np.asarray([bbox_gt.x1, bbox_gt.y1, bbox_gt.x2, bbox_gt.y2])
            bbox = bbox.reshape(bbox.shape[0], 1, 1)
            net.blobs['bbox'].data[i] = bbox

    def train(self, images, targets, bboxes_gt):
        """TODO: Docstring for train.
        :returns: TODO
        """

        objRegressor = self.regressor
        logger = self.logger

        if objRegressor.phase != caffe.TRAIN:
            logger.error('Phase is not to caffe.TRAIN')


        if len(images) != len(targets):
            logger.error('Error = {} images but {} targets', len(images), len(targets))

        if len(images) != len(bboxes_gt):
            logger.error('Error = {} images but {} bboxes_gt', len(images), len(bboxes_gt))


        self.set_boxes_gt(bboxes_gt)
        self.regressor.set_images(images, targets)
        self.step()

    def visualize_train(self):
        net = self.solver.net
        images = net.blobs['image'].data
        targets = net.blobs['target'].data
        viz.images(images, opts=dict(title='Random Images!', caption='How random.'))
        viz.images(targets, opts=dict(title='Random Targets!', caption='How random.'))

    def step(self):
        """TODO: Docstring for step.
        :returns: TODO
        """

        self.solver.step(1)
        # self.visualize_train()
