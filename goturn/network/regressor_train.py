# Date: Thursday 20 July 2017
# Email: nrupatunga@whodat.com
# Name: Nrupatunga
# Description: 
from regressor import regressor

class regressor_train(object):

    """Docstring for regressor_train. """

    def __init__(self, deploy_proto, caffe_model, gpu_id, solver_file, logger):
        """TODO: to be defined1. """

        self.kDoTrain = True
        self.kNumInputs = 3
        regressor(deploy_proto, caffe_model, gpu_id, self.kNumInputs, self.kDoTrain, logger)
        
