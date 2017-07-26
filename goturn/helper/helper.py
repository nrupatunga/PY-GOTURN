# Date: Wednesday 26 July 2017
# Email: nrupatunga@whodat.com
# Name: Nrupatunga
# Description: helper functions

import random
import math


def sample_rand_uniform(arg1):
    """TODO: Docstring for sample_rand_uniform.

    :arg1: TODO
    :returns: TODO

    """
    return (random.randint(0, RAND_MAX) + 1) * 1.0 / (RAND_MAX + 2)

def sample_exp_two_sides(lambda):
    """TODO: Docstring for sample_exp_two_sides.
    :returns: TODO

    """
    RAND_MAX = 2147483647

    pos_or_neg = random.randint(0, RAND_MAX)
    if (pos_or_neg % 2) == 0:
        pos_or_neg = 1
    else:
        pos_or_neg = -1

    rand_uniform = sample_rand_uniform()

    return math.log(rand_uniform) / (lambda * pos_or_neg)
