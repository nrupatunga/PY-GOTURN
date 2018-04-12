# Date: Thursday 20 July 2017
# Email: nrupatunga@whodat.com
# Name: Nrupatunga
# Description: generating training examples for training

from ..helper.image_proc import cropPadImage
from ..helper.BoundingBox import BoundingBox
from visdom import Visdom
import cv2
import numpy as np

viz = Visdom()


class bbParams:

    """Docstring for bbParams. """

    def __init__(self, lamda_shift, lamda_scale, min_scale, max_scale):
        """TODO: to be defined1. """
        self.lamda_shift = lamda_shift
        self.lamda_scale = lamda_scale
        self.min_scale = min_scale
        self.max_scale = max_scale


class example_generator:

    """Docstring for example_generator. """

    def __init__(self, lamda_shift, lamda_scale, min_scale, max_scale, logger):
        """TODO: to be defined1. """
        self.lamda_shift = lamda_shift
        self.lamda_scale = lamda_scale
        self.min_scale = min_scale
        self.max_scale = max_scale
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

    def make_training_examples(self, num_examples, images, targets, bbox_gt_scales):
        """TODO: Docstring for make_training_examples.
        :returns: TODO

        """
        for i in range(num_examples):
            image_rand_focus, target_pad, bbox_gt_scaled = self.make_training_example_BBShift()
            images.append(image_rand_focus)
            targets.append(target_pad)
            bbox_gt_scales.append(bbox_gt_scaled)
            # self.visualize(image_rand_focus, target_pad, bbox_gt_scaled, i)

        return images, targets, bbox_gt_scales

    def visualize(self, image, target, bbox, idx):
        """TODO: Docstring for visualize.
        :returns: TODO

        """
        target = cv2.resize(target, (227, 227))
        image = cv2.resize(image, (227, 227))

        bbox.unscale(image)
        bbox.x1, bbox.x2, bbox.y1, bbox.y2 = int(bbox.x1), int(bbox.x2), int(bbox.y1), int(bbox.y2)

        image = cv2.rectangle(image, (bbox.x1, bbox.y1), (bbox.x2, bbox.y2), (0, 255, 0), 2)
        out = np.concatenate((target[np.newaxis, ...], image[np.newaxis, ...]), axis=0)
        viz.images(np.transpose(out, [0, 3, 1, 2]), opts=dict(title='image' + str(idx), caption='How random.'))

    def get_default_bb_params(self):
        """TODO: Docstring for get_default_bb_params.
        :returns: TODO

        """
        default_params = bbParams(self.lamda_shift, self.lamda_scale, self.min_scale, self.max_scale)
        return default_params

    def make_training_example_BBShift_(self, bbParams, visualize_example=False):
        """TODO: Docstring for make_training_example_BBShift_.
        :returns: TODO

        """
        bbox_curr_gt = self.bbox_curr_gt_
        bbox_curr_shift = BoundingBox(0, 0, 0, 0)
        bbox_curr_shift = bbox_curr_gt.shift(self.img_curr_, bbParams.lamda_scale, bbParams.lamda_shift, bbParams.min_scale, bbParams.max_scale, True, bbox_curr_shift)
        rand_search_region, rand_search_location, edge_spacing_x, edge_spacing_y = cropPadImage(bbox_curr_shift, self.img_curr_)

        bbox_curr_gt = self.bbox_curr_gt_
        bbox_gt_recentered = BoundingBox(0, 0, 0, 0)
        bbox_gt_recentered = bbox_curr_gt.recenter(rand_search_location, edge_spacing_x, edge_spacing_y, bbox_gt_recentered)
        bbox_gt_recentered.scale(rand_search_region)
        bbox_gt_scaled = bbox_gt_recentered

        return rand_search_region, self.target_pad_, bbox_gt_scaled

    def make_training_example_BBShift(self):
        """TODO: Docstring for make_training_example_BBShift.
        :returns: TODO

        """
        default_bb_params = self.get_default_bb_params()
        image_rand_focus, target_pad, bbox_gt_scaled = self.make_training_example_BBShift_(default_bb_params)

        return image_rand_focus, target_pad, bbox_gt_scaled

    def reset(self, bbox_curr, bbox_prev, img_curr, img_prev):
        """TODO: to be defined1. """

        target_pad, _, _, _ = cropPadImage(bbox_prev, img_prev)
        self.img_curr_ = img_curr
        self.bbox_curr_gt_ = bbox_curr
        self.bbox_prev_gt_ = bbox_prev
        self.target_pad_ = target_pad
