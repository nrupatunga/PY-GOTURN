# Date: Wednesday 07 June 2017 11:28:11 AM IST
# Email: nrupatunga@whodat.com
# Name: Nrupatunga
# Description: tracker manager

import cv2
from ..helper.BoundingBox import BoundingBox

opencv_version = cv2.__version__.split('.')[0]

refPt = []
image = []
cv2.namedWindow("image")


def click_and_crop(event, x, y, flags, param):
    # grab references to the global variables
    global refPt, cropping
    # if the left mouse button was clicked, record the starting
    # (x, y) coordinates and indicate that cropping is being
    # performed
    if event == cv2.EVENT_LBUTTONDOWN:
        refPt = [(x, y)]
        cropping = True

    # check to see if the left mouse button was released
    elif event == cv2.EVENT_LBUTTONUP:
        # record the ending (x, y) coordinates and indicate that
        # the cropping operation is finished
        refPt.append((x, y))
        cropping = False
        # draw a rectangle around the region of interest
        cv2.rectangle(image, refPt[0], refPt[1], (0, 255, 0), 2)
        cv2.imshow("image", image)


cv2.setMouseCallback("image", click_and_crop)


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

        video_keys = videos.keys()
        for i in range(start_video_num, len(videos)):
            video_frames = videos[video_keys[i]][0]
            annot_frames = videos[video_keys[i]][1]

            num_frames = min(len(video_frames), len(annot_frames))

            # Get the first frame of this video with the intial ground-truth bounding box
            frame_0 = video_frames[0]
            bbox_0 = annot_frames[0]
            sMatImage = cv2.imread(frame_0)
            objTracker.init(sMatImage, bbox_0, objRegressor)
            for i in range(1, num_frames):
                frame = video_frames[i]
                sMatImage = cv2.imread(frame)
                sMatImageDraw = sMatImage.copy()
                bbox = annot_frames[i]

                if opencv_version == '2':
                    cv2.rectangle(sMatImageDraw, (int(bbox.x1), int(bbox.y1)), (int(bbox.x2), int(bbox.y2)), (255, 255, 255), 2)
                else:
                    sMatImageDraw = cv2.rectangle(sMatImageDraw, (int(bbox.x1), int(bbox.y1)), (int(bbox.x2), int(bbox.y2)), (255, 255, 255), 2)

                bbox = objTracker.track(sMatImage, objRegressor)
                if opencv_version == '2':
                    cv2.rectangle(sMatImageDraw, (int(bbox.x1), int(bbox.y1)), (int(bbox.x2), int(bbox.y2)), (255, 0, 0), 2)
                else:
                    sMatImageDraw = cv2.rectangle(sMatImageDraw, (int(bbox.x1), int(bbox.y1)), (int(bbox.x2), int(bbox.y2)), (255, 0, 0), 2)

                cv2.imshow('Results', sMatImageDraw)
                cv2.waitKey(10)

    def trackAny(self, start_video_num, pause_val):
        """Track frames with only first frame annotations
        """

        videos_ann = self.videos
        objRegressor = self.regressor
        objTracker = self.tracker

        video_frames = videos_ann[0]
        num_frames = len(video_frames)

        # Get the first frame of this video with the intial ground-truth bounding box
        frame_0 = video_frames[0]
        bbox_0 = videos_ann[1]
        sMatImage = cv2.imread(frame_0)
        global image
        image = sMatImage
        while True:
            # display the image and wait for a keypress
            cv2.imshow("image", sMatImage)
            key = cv2.waitKey(1) & 0xFF
            if key == ord("s"):
                (x1, y1), (x2, y2) = refPt[0], refPt[1]
                bbox_0 = BoundingBox(x1, y1, x2, y2)
                break
            elif key == ord("r"):
                (x1, y1), (x2, y2) = refPt[0], refPt[1]
                bbox_0 = BoundingBox(x1, y1, x2, y2)
                break

        objTracker.init(sMatImage, bbox_0, objRegressor)

        for i in range(1, num_frames):
            frame = video_frames[i]
            sMatImage = cv2.imread(frame)
            sMatImageDraw = sMatImage.copy()
            bbox = objTracker.track(sMatImage, objRegressor)
            if cv2.waitKey(1) & 0xFF == ord('p'):
                while True:
                    image = sMatImage
                    cv2.imshow("image", sMatImage)
                    key = cv2.waitKey(0) & 0xFF
                    if key == ord("s"):
                        (x1, y1), (x2, y2) = refPt[0], refPt[1]
                        bbox_0 = BoundingBox(x1, y1, x2, y2)
                        objTracker.init(sMatImage, bbox_0, objRegressor)
                        break

            if opencv_version == '2':
                cv2.rectangle(sMatImageDraw, (int(bbox.x1), int(bbox.y1)), (int(bbox.x2), int(bbox.y2)), (255, 0, 0), 2)
            else:
                sMatImageDraw = cv2.rectangle(sMatImageDraw, (int(bbox.x1), int(bbox.y1)), (int(bbox.x2), int(bbox.y2)), (255, 0, 0), 2)

            cv2.imshow('image', sMatImageDraw)
            cv2.waitKey(5)
