"""

This module contains the classes and methods used to perform the generic Metropolis-Hastings 
algorithm for doing an MCMC over a number of observables

"""


__all__ = ['HOD_Model','Zheng07_HOD_Model','Toy_HOD_Model','Assembly_Biased_HOD_Model',
'HOD_Quenching_Model','vdB03_Quenching_Model','Assembly_Biased_HOD_Quenching_Model',
'Satcen_Correlation_Polynomial_HOD_Model','Polynomial_Assembly_Biased_HOD_Model',
'cumulative_NFW_PDF','anatoly_concentration','solve_for_polynomial_coefficients']
#from __future__ import (absolute_import, division, print_function,
#                        unicode_literals)

import numpy as np
from scipy.special import erf
from scipy.stats import poisson
import defaults

from astropy.extern import six
from abc import ABCMeta, abstractmethod, abstractproperty
import warnings

