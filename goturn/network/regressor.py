# Date: Friday 02 June 2017 05:04:00 PM IST 
# Email: nrupatunga@whodat.com
# Name: Nrupatunga
# Description: Basic regressor function implemented

from __future__ import print_function
import os
import glob
import numpy as np
import sys
import cv2
from ..helper import config
sys.path.insert(0, config.CAFFE_PATH)
import caffe

class regressor:
    """Regressor Class"""

    def __init__(self, deploy_proto, caffe_model, gpu_id, num_inputs,
            do_train, logger, solver_file=None):
        """TODO: to be defined"""

        self.num_inputs = num_inputs
        self.logger = logger
        self.caffe_model_ = caffe_model
        self.modified_params_ = False
        self.mean = [104, 117, 123]
        self.modified_params = False
        self.solver_file = None

        if solver_file:
            self.solver_file = solver_file
        self.setupNetwork(deploy_proto, caffe_model, gpu_id, do_train)

    def reshape_image_inputs(self, num_images):
        """TODO: Docstring for reshape_image_inputs.
        :returns: TODO
        """
        
        net = self.net
        net.blobs['image'].reshape(num_images, self.channels, self.height, self.width)
        net.blobs['target'].reshape(num_images, self.channels, self.height, self.width)


    def set_images(self, images, targets):
        """TODO: Docstring for set_images.
        :returns: TODO
        """
        num_images = len(images)
        self.reshape_image_inputs(num_images)
        self.preprocess_batch(images, targets)


    def preprocess(self, image):
        """TODO: Docstring for preprocess.

        :arg1: TODO
        :returns: TODO

        """
        num_channels = self.channels
        if num_channels == 1 and image.shape[2] == 3:
            image_out = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        elif num_channels == 1 and image.shape[2] == 4:
            image_out = cv2.cvtColor(image, cv2.COLOR_BGRA2GRAY)
        elif num_channels == 3 and image.shape[2] == 4:
            image_out = cv2.cvtColor(image, cv2.COLOR_BGRA2BGR)
        elif num_channels == 3 and image.shape[2] == 1:
            image_out = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)
        else:
            image_out = image

        if image_out.shape != (self.height, self.width, self.channels):
            image_out = cv2.resize(image_out, (self.width, self.height), interpolation=cv2.INTER_CUBIC)

        image_out = np.float32(image_out)
        image_out -= np.array(self.mean)
        image_out = np.transpose(image_out, [2, 0, 1])
        return image_out

    def preprocess_batch(self, images_batch, targets_batch):
        """TODO: Docstring for preprocess_batch.

        :arg1: TODO
        :returns: TODO

        """

        net = self.net
        num_images = len(images_batch)
        for i in range(num_images):
            image = images_batch[i]
            image_out = self.preprocess(image)
            net.blobs['image'].data[i] = image_out

            target = targets_batch[i]
            target_out = self.preprocess(target)
            net.blobs['target'].data[i] = target_out


    def setupNetwork(self, deploy_proto, caffe_model, gpu_id, do_train):
        """TODO: Docstring for setupNetwork.

        :deploy_proto (string) : deploy prototxt file
        :caffe_model (string)  : trained caffe model path
        :gpu_id (integer) : GPU id
        :do_train (boolean) : training phase or testing phase

        """

        logger = self.logger
        caffe.set_mode_gpu()
        caffe.set_device(int(gpu_id))
        if do_train == True:
            logger.info('Setting phase to train')
            # TODO: this part of the code needs to be changed for
            # training phase
            if self.solver_file:
                self.solver = caffe.SGDSolver(self.solver_file)
                net = self.solver.net
                net.copy_from(caffe_model)
            else:
                logger.error('solver file required')
                return

            self.phase = caffe.TRAIN
        else:
            logger.info('Setting phase to test')
            net = caffe.Net(deploy_proto, caffe_model, caffe.TEST)
            self.phase = caffe.TEST

        self.net = net
        self.num_inputs = net.blobs['image'].data[...].shape[0]
        self.channels = net.blobs['image'].data[...].shape[1]
        self.height = net.blobs['image'].data[...].shape[2]
        self.width = net.blobs['image'].data[...].shape[3]

        if self.num_inputs != 1:
            logger.error('Network should take exactly one input')

        if self.channels != 1 and self.channels != 3:
            logger.error('Network should have 1 or 3 channels')

    def regress(self, curr_search_region, target_region):
        """TODO: Docstring for regress.
        :returns: TODO

        """
        return self.estimate(curr_search_region, target_region)

    def estimate(self, curr_search_region, target_region):
        """TODO: Docstring for estimate.

        :arg1: TODO
        :returns: TODO

        """
        net = self.net
        # reshape the inputs

        net.blobs['image'].data.reshape(1, self.channels, self.height, self.width)
        net.blobs['target'].data.reshape(1, self.channels, self.height, self.width)
        net.blobs['bbox'].data.reshape(1, 4, 1, 1)

        curr_search_region = self.preprocess(curr_search_region)
        target_region = self.preprocess(target_region)

        net.blobs['image'].data[...] = curr_search_region
        net.blobs['target'].data[...] = target_region
        net.forward()
        bbox_estimate = net.blobs['fc8'].data

        return bbox_estimate
