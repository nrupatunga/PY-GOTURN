# Date: Nrupatunga: Tuesday 04 July 2017
# Email: nrupatunga@whodat.com
# Name: Nrupatunga
# Description: loading Imagenet dataset

from __future__ import print_function
import os
import pdb
import glob
from annotation import annotation
import xml.etree.ElementTree as ET

kMaxRatio = 0.66

class loader_imagenetdet:

    """Docstring for loader_imagenetdet. """

    def __init__(self, imagenet_folder, annotations_folder, logger):
        """TODO: to be defined1. """

        self.logger = logger
        self.imagenet_folder = imagenet_folder
        self.annotations_folder = annotations_folder
        if not os.path.isdir(imagenet_folder):
            logger.error('{} is not a valid directory'.format(vot_folder))

    def get_videos(self):
        """TODO: Docstring for get_videos.
        :returns: TODO

        """
        logger = self.logger
        imagenet_folder = self.imagenet_folder
        imagenet_subdirs = sorted(self.find_subfolders(self.annotations_folder))

        for imgnet_sub_folder in imagenet_subdirs:
            annotations_files = sorted(glob.glob(os.path.join(self.annotations_folder, imgnet_sub_folder, '*.xml')))
            for ann in annotations_files:
                self.load_annotation_file(ann)
        

    def find_subfolders(self, imagenet_folder):
        """TODO: Docstring for find_subfolders.

        :vot_folder: directory for vot videos
        :returns: list of video sub directories
        """

        return [dir_name for dir_name in os.listdir(imagenet_folder) if os.path.isdir(os.path.join(imagenet_folder, dir_name))]

    def load_annotation_file(self, annotation_file):
        """TODO: Docstring for load_annotation_file.
        :returns: TODO

        """
        root = ET.parse(annotation_file).getroot()
        folder = root.find('folder').text
        filename = root.find('filename').text
        size = root.find('size')
        disp_width = int(size.find('width').text)
        disp_height = int(size.find('height').text)

        for obj in root.findall('object'):
            bbox = obj.find('bndbox')
            xmin = int(bbox.find('xmin').text)
            xmax = int(bbox.find('xmax').text)
            ymin = int(bbox.find('ymin').text)
            ymax = int(bbox.find('ymax').text)

            width = xmax - xmin
            height = ymax - ymin

            if width > (kMaxRatio * disp_width) or height > (kMaxRatio * disp_height):
                continue

        pdb.set_trace()


if '__main__' == __name__:
    objLoaderImgNet = loader_imagenetdet('/media/nrupatunga/data/datasets/ILSVRC2014/ILSVRC2014_DET_train/', '/media/nrupatunga/data/datasets/ILSVRC2014/ILSVRC2014_DET_bbox_train/', None)
    objLoaderImgNet.get_videos()
