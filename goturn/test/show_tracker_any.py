"""
File: show_tracker_any.py
Author: Nrupatunga
Email: nrupatunga.s@byjus.com
Github: https://github.com/nrupatunga
Description: show tracker output for videos without gt
"""

import argparse
import setproctitle
from ..logger.logger import setup_logger
from ..network.regressor import regressor
from ..loader.loader_any import loader_any
from ..tracker.tracker import tracker
from ..tracker.tracker_manager import tracker_manager
from ..helper.BoundingBox import BoundingBox

setproctitle.setproctitle('SHOW_TRACKER_VOT')
logger = setup_logger(logfile=None)

ap = argparse.ArgumentParser()
ap.add_argument("-p", "--prototxt", required=True, help="Path to the prototxt")
ap.add_argument("-m", "--model", required=True, help="Path to the model")
ap.add_argument("-v", "--input", required=True, help="Path to the vot directory")
ap.add_argument("-g", "--gpuID", required=True, help="gpu to use")
args = vars(ap.parse_args())

do_train = False
objRegressor = regressor(args['prototxt'], args['model'], args['gpuID'], 1, do_train, logger)
objTracker = tracker(False, logger)  # Currently no idea why this class is needed, eventually we shall figure it out
# bbox_init = BoundingBox(199.35, 112.74, 244.48, 158.32)
bbox_init = BoundingBox(1407, 593, 1417, 716)
objLoaderAny = loader_any(args['input'], bbox_init, logger)
videos = objLoaderAny.get_video_frames()
objTrackerVis = tracker_manager(videos, objRegressor, objTracker, logger)
objTrackerVis.trackAny(0, 1)
