# Date: Nrupatunga: Wednesday 05 July 2017
# Email: nrupatunga@whodat.com
# Name: Nrupatunga
# Description: loading Alov dataset

from __future__ import print_function
import sys
sys.path.append('../logger/')
sys.path.append('../helper/')
import os
import glob
from annotation import annotation
from video import video
from video import frame
import xml.etree.ElementTree as ET
from logger import setup_logger
from BoundingBox import BoundingBox


class loader_alov:

    """Docstring for loader_alov. """

    def __init__(self, alov_folder, annotations_folder, logger):
        """TODO: to be defined1. """

        self.logger = logger
        self.alov_folder = alov_folder
        self.annotations_folder = annotations_folder
        self.alov_videos = {}
        self.category = {}
        if not os.path.isdir(alov_folder):
            logger.error('{} is not a valid directory'.format(alov_folder))

    def loaderAlov(self):
        """TODO: Docstring for loaderAlov.
        :returns: TODO

        """
        logger = self.logger
        alov_folder = self.alov_folder
        alov_subdirs = sorted(self.find_subfolders(self.annotations_folder))
        num_annotations = 0
        dict_list_of_annotations = {}

        for i, alov_sub_folder in enumerate(alov_subdirs):
            annotations_files = sorted(glob.glob(os.path.join(self.annotations_folder, alov_sub_folder, '*.ann')))
            logger.info('Loading {}/{} - annotation file from folder = {}'.format(i+1, len(alov_subdirs), alov_sub_folder))

            for ann in annotations_files:
                self.load_annotation_file(alov_sub_folder, ann)

    def find_subfolders(self, alov_folder):
        """TODO: Docstring for find_subfolders.

        :alov_folder: directory for alov videos
        :returns: list of video sub directories
        """

        return [dir_name for dir_name in os.listdir(alov_folder) if os.path.isdir(os.path.join(alov_folder, dir_name))]

    def load_annotation_file(self, alov_sub_folder, annotation_file):

        video_path = os.path.join(self.alov_folder, alov_sub_folder, annotation_file.split('/')[-1].split('.')[0])

        objVideo = video(video_path)
        all_frames = glob.glob(os.path.join(video_path, '*.jpg'))
        objVideo.all_frames = sorted(all_frames)

        with open(annotation_file, 'r') as f:
            data = f.read().rstrip().split('\n')
            for bb in data: 
                frame_num, ax, ay, bx, by, cx, cy, dx, dy = bb.split()
                frame_num, ax, ay, bx, by, cx, cy, dx, dy = int(frame_num), float(ax), float(ay), float(bx), float(by), float(cx), float(cy), float(dx), float(dy)

                x1 = min(ax, min(bx, min(cx, dx))) - 1
                y1 = min(ay, min(by, min(cy, dy))) - 1
                x2 = max(ax, max(bx, max(cx, dx))) - 1
                y2 = max(ay, max(by, max(cy, dy))) - 1

                bbox = BoundingBox(x1, y1, x2, y2)
                objFrame = frame(frame_num - 1, bbox)
                objVideo.annotations.append(objFrame)

        video_name = video_path.split('/')[-1]
        self.alov_videos[video_name] = objVideo
        if alov_sub_folder not in self.category.keys():
            self.category[alov_sub_folder] = []

        self.category[alov_sub_folder].append(self.alov_videos[video_name])

    def get_videos(self, isTrain=True, val_ratio=0.2):
        """TODO: Docstring for get_videos.
        :returns: TODO
        """

        videos = []
        logger = self.logger
        num_categories = len(self.category)
        category = self.category
        keys = sorted(category.keys())
        for i in range(num_categories):
            category_video = category[keys[i]]
            num_videos = len(category_video)
            num_val = int(val_ratio * num_videos)
            num_train = num_videos - num_val

            if isTrain:
                start_num = 0
                end_num = num_train - 1
            else:
                start_num = num_train
                end_num = num_videos - 1

            for i in range(start_num, end_num):
                video = category_video[i]
                videos.append(video)

        num_annotations = 0
        for i, _ in enumerate(videos):
            import pdb
            pdb.set_trace()
            num_annotations = num_annotations + len(videos[i].annotations)

        logger.info('Total annotated video frames: {}'.format(num_annotations))

        
if '__main__' == __name__:
    logger = setup_logger(logfile=None)
    objLoaderAlov = loader_alov('/media/nrupatunga/data/datasets/VOT-extract/images/', '/media/nrupatunga/data/datasets/VOT-extract/gt/', logger)
    objLoaderAlov.loaderAlov()
    objLoaderAlov.get_videos()
