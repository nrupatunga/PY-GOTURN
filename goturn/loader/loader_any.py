"""
File: loader_any.py
Author: Nrupatunga
Email: nrupatunga.s@byjus.com
Github: https://github.com/nrupatunga
Description: Load videos without annotations
"""
import os
import glob
from video import video


class loader_any:

    """Helper function to load any video without gt"""

    def __init__(self, video_dir, init_ann, logger):
        """Init the folders
        """

        self._logger = logger
        self._video_dir = video_dir

        self._videos = {}
        self._annotations = {}

        self._init_ann = init_ann

        if not os.path.isdir(video_dir):
            logger.error('{} is not a valid directory'.format(video_dir))

    def get_video_frames(self):
        """ Get the video frames from the video_dir
        """

        logger = self._logger
        vid_dir = self._video_dir
        video_path = glob.glob(os.path.join(vid_dir, '*.jpg'))
        objVid = video(video_path)
        list_of_frames = sorted(video_path)

        if not list_of_frames:
            logger.error('vot folders should contain only .jpg images')

        objVid.all_frames = list_of_frames
        self._videos = [objVid.all_frames, self._init_ann]

        return self._videos

    def find_subfolders(self, vid_dir):
        """
        find subfolders inside vid_dir
        """

        return [dir_name for dir_name in os.listdir(vid_dir) if
                os.path.isdir(os.path.join(vid_dir, dir_name))]
