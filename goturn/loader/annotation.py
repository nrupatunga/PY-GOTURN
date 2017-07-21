# Date: Nrupatunga: Tuesday 04 July 2017 
# Email: nrupatunga@whodat.com
# Name: Nrupatunga
# Description: annotations

import sys
from ..helper.BoundingBox import BoundingBox

class annotation:

    """Docstring for annotation. """

    def __init__(self):
        """TODO: to be defined1. """
        self.bbox = BoundingBox(0, 0, 0, 0)
        self.image_path = []
        self.disp_width = 0
        self.disp_height = 0

    def setbbox(self, x1, x2, y1, y2):
        """TODO: Docstring for setbbox.
        :returns: TODO

        """
        self.bbox.x1 = x1
        self.bbox.x2 = x2
        self.bbox.y1 = y1
        self.bbox.y2 = y2

    def setImagePath(self, img_path):
        """TODO: Docstring for setImagePath.
        :returns: TODO

        """
        self.image_path = img_path

    def setWidthHeight(self, disp_width, disp_height):
        """TODO: Docstring for setWidthHeight.
        :returns: TODO

        """
        self.disp_width = disp_width
        self.disp_height = disp_height
