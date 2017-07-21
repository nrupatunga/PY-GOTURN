# Date: Friday 21 July 2017
# Email: nrupatunga@whodat.com
# Name: Nrupatunga
# Description: Training the tracker


import argparse
import setproctitle
from ..logger.logger import setup_logger
from ..loader.loader_imagenet import loader_imagenet
from ..loader.loader_alov import loader_alov
from ..train.example_generator import example_generator
from ..network.regressor_train import regressor_train
import sys
sys.path.insert(0, '/usr/local/caffe/python')
import os
import caffe
import numpy as np

setproctitle.setproctitle('TRAIN_TRACKER_IMAGENET_ALOV')
logger = setup_logger(logfile=None)

ap = argparse.ArgumentParser()
ap.add_argument("-imagenet", "--imagenet", required = True, help = "Path to ImageNet folder")
ap.add_argument("-alov", "--alov", required = True, help = "Path to Alov folder")
ap.add_argument("-init_caffemodel", "--init_caffemodel", required = True, help = "Path to caffe Init model")
ap.add_argument("-train_prototxt", "--train_prototxt", required = True, help = "train prototxt")
ap.add_argument("-solver_prototxt", "--solver_prototxt", required = True, help = "solver prototxt")
ap.add_argument("-lamda_shift", "--lamda_shift", required = True, help = "lamda shift")
ap.add_argument("-lamda_scale", "--lamda_scale", required = True, help = "lamda scale ")
ap.add_argument("-min_scale", "--min_scale", required = True, help = "min scale")
ap.add_argument("-max_scale", "--max_scale", required = True, help = "max scale")
ap.add_argument("-gpu_id", "--gpu_id", required = True, help = "gpu id")


RANDOM_SEED = 800
GPU_ONLY = True

def main(args):
    """TODO: Docstring for main.
    """
    # Fix random seeds (numpy and caffe) for reproducibility
    np.random.seed(RANDOM_SEED)
    caffe.set_random_seed(RANDOM_SEED)

    if GPU_ONLY:
        caffe.set_mode_gpu()
        caffe.set_device(int(args['gpu_id']))
    else:
        caffe.set_mode_cpu()

    # Load imagenet training images and annotations
    imagenet_folder = os.path.join(args['imagenet'], 'ILSVRC2014_DET_train')
    imagenet_annotations_folder = os.path.join(args['imagenet'], 'ILSVRC2014_DET_bbox_train')
    objLoaderImgNet = loader_imagenet(imagenet_folder, imagenet_annotations_folder, logger)
    train_imagenet_images = objLoaderImgNet.loaderImageNetDet()

    # Load alov training images and annotations
    alov_folder = os.path.join(args['alov'], 'images')
    alov_annotations_folder = os.path.join(args['alov'], 'gt')
    objLoaderAlov = loader_alov(alov_folder, alov_annotations_folder, logger)
    objLoaderAlov.loaderAlov()
    train_alov_videos = objLoaderAlov.get_videos()

    # create example generator and setup the network
    objExampleGen = example_generator(float(args['lamda_shift']), float(args['lamda_scale']), float(args['min_scale']), float(args['max_scale']), logger)
    objRegTrain = regressor_train(args['train_prototxt'], args['init_caffemodel'], int(args['gpu_id']), args['solver_prototxt'], logger) 


if __name__ == '__main__':
    args = vars(ap.parse_args())
    main(args)
