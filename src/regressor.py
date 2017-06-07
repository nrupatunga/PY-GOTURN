# Date: Friday 02 June 2017 05:04:00 PM IST 
# Email: nrupatunga@whodat.com
# Name: Nrupatunga
# Description: Basic regressor function implemented

from __future__ import print_function
import os
import pdb
import glob
import numpy as np
import sys
sys.path.insert(0, '/usr/local/caffe/python')
import caffe

class regressor:
    """Regressor Class"""

    def __init__(self, deploy_proto, caffe_model, gpu_id, do_train, logger):
        """TODO: to be defined"""

        self.num_inputs = 2
        self.logger = logger
        self.caffe_model_ = caffe_model
        self.modified_params_ = False
        self.setupNetwork(deploy_proto, caffe_model, gpu_id, do_train)
        self.mean = [104, 117, 123]


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
            net = caffe.Net(deploy_proto, caffe_model, caffe.TRAIN)
        else:
            logger.info('Setting phase to test')
            net = caffe.Net(deploy_proto, caffe_model, caffe.TEST)

        self.num_inputs = net.blobs['image'].data[...].shape[0]
        self.channels = net.blobs['image'].data[...].shape[1]
        self.height = net.blobs['image'].data[...].shape[2]
        self.width = net.blobs['image'].data[...].shape[3]

        if self.num_inputs != 1:
            logger.error('Network should take exactly one input')

        if self.channels != 1 and self.channels != 3:
            logger.error('Network should have 1 or 3 channels')
