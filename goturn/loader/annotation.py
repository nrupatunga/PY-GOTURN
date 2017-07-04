# Date: Nrupatunga: Tuesday 04 July 2017 
# Email: nrupatunga@whodat.com
# Name: Nrupatunga
# Description: annotations

import sys
sys.path.append('../helper/')
from BoundingBox import BoundingBox

class annotation:

    """Docstring for annotation. """

    def __init__(self):
        """TODO: to be defined1. """
        self.bbox = BoundingBox(0, 0, 0, 0)
        self.image_path = []
        self.disp_width = 0
        self.disp_height = 0
