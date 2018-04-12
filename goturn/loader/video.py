# Date: Thursday 08 June 2017 11:53:29 AM IST
# Email: nrupatunga@whodat.com
# Name: Nrupatunga
# Description: Basic video helper functions

import cv2


class frame:

    """Docstring for frame. """

    def __init__(self, frame_num, bbox):
        """TODO: to be defined1. """
        self.frame_num = frame_num
        self.bbox = bbox


class video:

    """Docstring for video. """

    def __init__(self, video_path):
        """TODO: to be defined1. """
        self.video_path = video_path
        self.all_frames = []
        self.annotations = []

    def load_annotation(self, annotation_index):
        """TODO: Docstring for load_annotation.
        :returns: TODO

        """
        ann_frame = self.annotations[annotation_index]
        frame_num = ann_frame.frame_num
        bbox = ann_frame.bbox

        image_files = self.all_frames

        assert(len(image_files) > 0)
        assert(frame_num < len(image_files))

        image = cv2.imread(image_files[frame_num])
        return frame_num, image, bbox

    def loadframe(self, frame_idx, draw_bounding_box, load_only_annotation):
        """TODO: Docstring for loadframe.
        :returns: TODO

        """
        pass
