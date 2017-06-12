# Date: Wednesday 07 June 2017 11:28:11 AM IST
# Email: nrupatunga@whodat.com
# Name: Nrupatunga
# Description: tracker manager

import cv2 
import pdb

class tracker_manager:

    """Docstring for tracker_manager. """

    def __init__(self, videos, annotations, regressor, tracker, logger):
        """This is

        :videos: list of video frames
        :annotations: list of video frame annotations
        :regressor: regressor object
        :tracker: tracker object
        :logger: logger object
        :returns: list of video sub directories
        """

        self.videos = videos
        self.annotations = annotations
        self.regressor = regressor
        self.tracker = tracker
        self.logger = logger


    def trackAll(self, start_video_num, pause_val):
        """Track the objects in the video
        """

        videos = self.videos
        annotations = self.annotations
        objRegressor = self.regressor
        objTracker = self.tracker
        logger = self.logger

        video_keys = videos.keys()
        for i in range(start_video_num, len(videos)):
            video_frames = videos[video_keys[i]]
            annot_frames = annotations[video_keys[i]]

            num_frames = min(video_frames, annot_frames)

            # Get the first frame of this video with the intial
            # ground-truth bounding box
            frame_0 = video_frames[0]
            bbox_0 = annot_frames[0]
            for i in xrange(1, num_frames):
                frame = video_frames[i]
                bbox = annot_frames[i]

                sMatImage = cv2.imread(frame)
                cv2.rectangle(sMatImage, (bbox_0.x1, bbox_0.y1), (bbox_0.x2,
                    bbox_0.y2), (255, 0, 0), 2)
                cv2.imshow('input', sMatImage)
                cv2.waitKey(30)
            
