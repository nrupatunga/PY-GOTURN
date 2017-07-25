# Date: Thursday 20 July 2017
# Email: nrupatunga@whodat.com
# Name: Nrupatunga
# Description: generating training examples for training

from ..helper.image_proc import cropPadImage
from ..helper.BoundingBox import BoundingBox


class example_generator:

    """Docstring for example_generator. """

    def __init__(self, lamda_shift, lamda_scale, min_scale, max_scale, logger):
        """TODO: to be defined1. """
        self.lamda_shift = lamda_shift
        self.lamda_scale = lamda_scale
        self.min_scale = min_scale
        self.max_scale= max_scale
        self.logger = logger

    def make_true_example(self):
        """TODO: Docstring for make_true_example.
        :returns: TODO

        """

        curr_prior_tight = self.bbox_prev_gt_
        target_pad = self.target_pad_
        curr_search_region, curr_search_location, edge_spacing_x, edge_spacing_y = cropPadImage(curr_prior_tight, self.img_curr_)

        bbox_curr_gt = self.bbox_curr_gt_
        bbox_curr_gt_recentered = BoundingBox(0, 0, 0, 0)
        bbox_curr_gt_recentered = bbox_curr_gt.recenter(curr_search_location, edge_spacing_x, edge_spacing_y, bbox_curr_gt_recentered)
        bbox_curr_gt_recentered.scale(curr_search_region)

        return curr_search_region, target_pad, bbox_curr_gt_recentered


    def reset(self, bbox_curr, bbox_prev, img_curr, img_prev):
        """TODO: to be defined1. """

        target_pad, _, _, _ =  cropPadImage(bbox_prev, img_prev)
        self.img_curr_ = img_curr
        self.bbox_curr_gt_ = bbox_curr
        self.bbox_prev_gt_ = bbox_prev
        self.target_pad_ = target_pad
