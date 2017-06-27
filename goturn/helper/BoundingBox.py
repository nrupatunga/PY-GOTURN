# Date: Tuesday 06 June 2017 03:54:55 PM
# Email: nrupatunga@whodat.com
# Name: Nrupatunga
# Description: bounding box class


class BoundingBox:
    """Docstring for BoundingBox. """

    def __init__(self, x1, y1, x2, y2):
        """bounding box """

        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.frame_num = 0
        self.kContextFactor = 2

    def get_center_x(self):
        """TODO: Docstring for get_center_x.
        :returns: TODO

        """
        return (self.x1 + self.x2)/2.

    def get_center_y(self):
        """TODO: Docstring for get_center_y.
        :returns: TODO

        """
        return (self.y1 + self.y2)/2.

    def compute_output_height(self):
        """TODO: Docstring for compute_output_height.
        :returns: TODO

        """
        bbox_height = self.y2 - self.y1
        output_height = self.kContextFactor * bbox_height
        
        return max(1.0, output_height)

    def compute_output_width(self):
        """TODO: Docstring for compute_output_width.
        :returns: TODO

        """
        bbox_width = self.x2 - self.x1
        output_width = self.kContextFactor * bbox_width
        
        return max(1.0, output_width)

    def edge_spacing_x(self):
        """TODO: Docstring for edge_spacing_x.
        :returns: TODO

        """
        output_width = self.compute_output_width()
        bbox_center_x = self.get_center_x()

        return max(0.0, (output_width / 2) - bbox_center_x)

    def edge_spacing_y(self):
        """TODO: Docstring for edge_spacing_y.
        :returns: TODO

        """
        output_height = self.compute_output_height()
        bbox_center_y = self.get_center_y()

        return max(0.0, (output_height / 2) - bbox_center_y)
