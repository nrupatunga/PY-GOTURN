# Date: Nrupatunga: Tuesday 04 July 2017
# Email: nrupatunga@whodat.com
# Name: Nrupatunga
# Description: loading Imagenet dataset

from __future__ import print_function
import os
import cv2
import glob
from annotation import annotation
import xml.etree.ElementTree as ET
from ..logger.logger import setup_logger
from ..helper import config

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
        imagenet_subdirs = sorted(self.find_subfolders(self.annotations_folder))
        num_annotations = 0
        list_of_annotations_out = []

        for i, imgnet_sub_folder in enumerate(imagenet_subdirs):
            annotations_files = sorted(glob.glob(os.path.join(self.annotations_folder, imgnet_sub_folder, '*.xml')))
            logger.info('Loading {}/{} - annotation file from folder = {}'.format(i + 1, len(imagenet_subdirs), imgnet_sub_folder))
            for ann in annotations_files:
                list_of_annotations, num_ann_curr = self.load_annotation_file(ann)
                num_annotations = num_annotations + num_ann_curr
                if len(list_of_annotations) == 0:
                    continue
                list_of_annotations_out.append(list_of_annotations)

        logger.info('Found {} annotations from {} images'.format(num_annotations, len(list_of_annotations_out)))

        # save it for future use
        self.list_of_annotations_out = list_of_annotations_out
        self.num_annotations = num_annotations

        return list_of_annotations_out

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

    def load_annotation(self, image_num, annotation_num):
        """TODO: Docstring for load_annotation.
        :returns: TODO

        """
        logger = self.logger

        images = self.list_of_annotations_out
        list_annotations = images[image_num]
        random_ann = list_annotations[annotation_num]

        img_path = os.path.join(self.imagenet_folder, random_ann.image_path + '.JPEG')

        if config.DEBUG:
            img_path = "/media/nrupatunga/Data-Backup/DL/goturn/ILSVRC2014/ILSVRC2014_DET_train/ILSVRC2014_train_0005/ILSVRC2014_train_00059375.JPEG"
            random_ann.bbox.x1 = 243
            random_ann.bbox.y1 = 157
            random_ann.bbox.x2 = 278
            random_ann.bbox.y2 = 176
            random_ann.disp_height = 375
            random_ann.disp_width = 500

        image = cv2.imread(img_path)

        img_height = image.shape[0]
        img_width = image.shape[1]

        sc_factor_1 = 1.0
        if img_height != random_ann.disp_height or img_width != random_ann.disp_width:
            logger.info('Image Number = {}, Annotation Number = {}, Image file = {}'.format(image_num, annotation_num, img_path))
            logger.info('Image Size = {} x {}'.format(img_width, img_height))
            logger.info('Display Size = {} x {}'.format(random_ann.disp_width, random_ann.disp_height))

            sc_factor_1 = (img_height * 1.) / random_ann.disp_height
            sc_factor_2 = (img_width * 1.) / random_ann.disp_width

            logger.info('Factor: {} {}'.format(sc_factor_1, sc_factor_2))

        bbox = random_ann.bbox
        bbox.x1 = bbox.x1 * sc_factor_1
        bbox.x2 = bbox.x2 * sc_factor_1
        bbox.y1 = bbox.y1 * sc_factor_1
        bbox.y2 = bbox.y2 * sc_factor_1

        return image, bbox


if '__main__' == __name__:
    logger = setup_logger(logfile=None)
    objLoaderImgNet = loader_imagenet('/media/nrupatunga/data/datasets/ILSVRC2014/ILSVRC2014_DET_train/', '/media/nrupatunga/data/datasets/ILSVRC2014/ILSVRC2014_DET_bbox_train/', logger)
    dict_list_of_annotations = objLoaderImgNet.loaderImageNetDet()
