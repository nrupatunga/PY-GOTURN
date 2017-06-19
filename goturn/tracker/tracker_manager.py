# Date: Wednesday 07 June 2017 11:28:11 AM IST
# Email: nrupatunga@whodat.com
# Name: Nrupatunga
# Description: tracker manager

import cv2 
import pdb

class tracker_manager:

    """Docstring for tracker_manager. """

    def __init__(self, videos, regressor, tracker, logger):
        """This is

        :videos: list of video frames and annotations
        :regressor: regressor object
        :tracker: tracker object
        :logger: logger object
        :returns: list of video sub directories
        """

        self.videos = videos
        self.regressor = regressor
        self.tracker = tracker
        self.logger = logger


    def trackAll(self, start_video_num, pause_val):
        """Track the objects in the video
        """

        videos = self.videos
        objRegressor = self.regressor
        objTracker = self.tracker
        logger = self.logger

        video_keys = videos.keys()
        for i in range(start_video_num, len(videos)):
            video_frames = videos[video_keys[i]][0]
            annot_frames = videos[video_keys[i]][1]

            num_frames = min(len(video_frames), len(annot_frames))

            # Get the first frame of this video with the intial
            # ground-truth bounding box
            frame_0 = video_frames[0]
            bbox_0 = annot_frames[0]
            sMatImage = cv2.imread(frame_0)
            objTracker.init(sMatImage, bbox_0, objRegressor)
            cv2.rectangle(sMatImage, (bbox_0.x1, bbox_0.y1), (bbox_0.x2, bbox_0.y2), (255, 0, 0), 2)
            cv2.imshow('input', sMatImage)
            for i in xrange(1, num_frames):
                frame = video_frames[i]
                bbox = annot_frames[i]

                sMatImage = cv2.imread(frame)
                # objTracker.track(sMatImage, objRegressor)
                cv2.rectangle(sMatImage, (bbox.x1, bbox.y1), (bbox.x2, bbox.y2), (255, 0, 0), 2)
                cv2.imshow('input', sMatImage)
                cv2.waitKey(30)
