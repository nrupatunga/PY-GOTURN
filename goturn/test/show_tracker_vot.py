# Date: Friday 02 June 2017 05:50:20 PM IST
# Email: nrupatunga@whodat.com
# Name: Nrupatunga
# Description: Test file for showing the tracker output

import argparse
import pdb
from ..logger.logger import setup_logger
from ..network.regressor import regressor
from ..loader.loader_vot import loader_vot
from ..tracker.tracker import tracker
from ..tracker.tracker_manager import tracker_manager
from ..loader.video import video

logger = setup_logger(logfile=None)

ap = argparse.ArgumentParser()
ap.add_argument("-p", "--prototxt", required = True, help = "Path to the prototxt")
ap.add_argument("-m", "--model", required = True, help = "Path to the model")
ap.add_argument("-v", "--input", required = True, help = "Path to the vot directory")
ap.add_argument("-g", "--gpuID", required = True, help = "gpu to use")
args = vars(ap.parse_args())

do_train = False
pdb.set_trace()
objRegressor = regressor(args['prototxt'], args['model'], args['gpuID'], do_train, logger)
objTracker = tracker(False, logger) # Currently no idea why this class is needed, eventually we shall figure it out
objLoaderVot = loader_vot(args['input'], logger)
video_frames, annotations = objLoaderVot.get_videos()
objTrackerVis = tracker_manager(video_frames, annotations, objRegressor, objTracker, logger)

pdb.set_trace()
objTrackerVis.trackAll(0, 1)
