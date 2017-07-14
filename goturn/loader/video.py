# Date: Thursday 08 June 2017 11:53:29 AM IST
# Email: nrupatunga@whodat.com
# Name: Nrupatunga
# Description: Basic video helper functions


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


    def loadframe(self, frame_idx, draw_bounding_box, load_only_annotation):
        """TODO: Docstring for loadframe.
        :returns: TODO

        """
        pass

        
