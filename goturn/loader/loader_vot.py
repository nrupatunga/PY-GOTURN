# Date: Friday 02 June 2017 07:00:47 PM IST
# Email: nrupatunga@whodat.com
# Name: Nrupatunga
# Description: loading VOT dataset

from __future__ import print_function
import os
from ..helper.BoundingBox import BoundingBox
from video import video
import glob
import pdb


class loader_vot:
    """Helper functions for loading VOT data"""

    def __init__(self, vot_folder, logger):
        """Load all the videos in the vot_folder"""

        self.logger = logger
        self.vot_folder = vot_folder
        self.videos = {}
        self.annotations = {}
        if not os.path.isdir(vot_folder):
            logger.error('{} is not a valid directory'.format(vot_folder))


    def get_videos(self):
        """Docstring for get_videos.

        :returns: returns video frames in each sub folder of vot directory

        """
        
        vot_folder = self.vot_folder
        sub_vot_dirs = self.find_subfolders(vot_folder)
        for vot_sub_dir in sub_vot_dirs:
            video_path = glob.glob(os.path.join(vot_folder, vot_sub_dir, '*.jpg'))
            objVid = video(video_path)
            list_of_frames = sorted(video_path)
            if not list_of_frames:
                logger.error('vot folders should contain only .jpg images')

            objVid.all_frames = list_of_frames
            bbox_gt_file = os.path.join(vot_folder, vot_sub_dir, 'groundtruth.txt')
            with open(bbox_gt_file, 'r') as f:
                for i, line in enumerate(f):
                    co_ords = line.strip().split(',')
                    co_ords = [int(float(co_ord)) for co_ord in co_ords]
                    ax, ay, bx, by, cx, cy, dx, dy = co_ords
                    x1 = min(ax, min(bx, min(cx, dx))) - 1
                    y1 = min(ay, min(by, min(cy, dy))) - 1
                    x2 = max(ax, max(bx, max(cx, dx))) - 1
                    y2 = max(ay, max(by, max(cy, dy))) - 1
                    bbox = BoundingBox(x1, y1, x2, y2)
                    bbox.frame_num = i
                    objVid.annotations.append(bbox)
            self.videos[vot_sub_dir] = [objVid.all_frames, objVid.annotations]
        return self.videos
            

    def find_subfolders(self, vot_folder):
        """TODO: Docstring for find_subfolders.

        :vot_folder: directory for vot videos
        :returns: list of video sub directories
        """

        return [dir_name for dir_name in os.listdir(vot_folder) if os.path.isdir(os.path.join(vot_folder, dir_name))]
