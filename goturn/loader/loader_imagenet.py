# Date: Nrupatunga: Tuesday 04 July 2017
# Email: nrupatunga@whodat.com
# Name: Nrupatunga
# Description: loading Imagenet dataset

from __future__ import print_function
import sys
import os
import glob
from annotation import annotation
import xml.etree.ElementTree as ET
from ..logger.logger import setup_logger


kMaxRatio = 0.66

class loader_imagenet:

    """Docstring for loader_imagenetdet. """

    def __init__(self, imagenet_folder, annotations_folder, logger):
        """TODO: to be defined1. """

        self.logger = logger
        self.imagenet_folder = imagenet_folder
        self.annotations_folder = annotations_folder
        if not os.path.isdir(imagenet_folder):
            logger.error('{} is not a valid directory'.format(imagenet_folder))

    def loaderImageNetDet(self):
        """TODO: Docstring for get_videos.
        :returns: TODO

        """
        logger = self.logger
        imagenet_folder = self.imagenet_folder
        imagenet_subdirs = sorted(self.find_subfolders(self.annotations_folder))
        num_annotations = 0
        dict_list_of_annotations = {}

        for i, imgnet_sub_folder in enumerate(imagenet_subdirs):
            annotations_files = sorted(glob.glob(os.path.join(self.annotations_folder, imgnet_sub_folder, '*.xml')))
            logger.info('Loading {}/{} - annotation file from folder = {}'.format(i+1, len(imagenet_subdirs), imgnet_sub_folder))
            for ann in annotations_files:
                list_of_annotations, num_ann_curr = self.load_annotation_file(ann)
                num_annotations = num_annotations + num_ann_curr
                if len(list_of_annotations) == 0:
                    continue
                dict_list_of_annotations[imgnet_sub_folder] = list_of_annotations

        logger.info('Found {} annotations from {} images'.format(num_annotations, len(dict_list_of_annotations)))
        return dict_list_of_annotations
        

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
        list_of_annotations = []
        num_annotations = 0
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

            if ((xmin < 0) or (ymin < 0) or (xmax <= xmin) or (ymax <= ymin)):
                continue

            objAnnotation = annotation()
            objAnnotation.setbbox(xmin, xmax, ymin, ymax)
            objAnnotation.setWidthHeight(disp_width, disp_height)
            objAnnotation.setImagePath(os.path.join(folder, filename))
            list_of_annotations.append(objAnnotation)
            num_annotations = num_annotations + 1

        return list_of_annotations, num_annotations



if '__main__' == __name__:
    logger = setup_logger(logfile=None)
    objLoaderImgNet = loader_imagenet('/media/nrupatunga/data/datasets/ILSVRC2014/ILSVRC2014_DET_train/', '/media/nrupatunga/data/datasets/ILSVRC2014/ILSVRC2014_DET_bbox_train/', logger)
    dict_list_of_annotations = objLoaderImgNet.loaderImageNetDet()
    import pdb
    pdb.set_trace()
