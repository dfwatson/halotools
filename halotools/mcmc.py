"""

This module contains the classes and methods used to perform the generic Metropolis-Hastings 
algorithm for doing an MCMC over a variety of observables

"""


__all__ = ['Mmin','M1','M0','alpha','sigma']


import numpy as np
from scipy.signal import gaussian
import defaults

from astropy.extern import six
from abc import ABCMeta, abstractmethod, abstractproperty
import warnings

"""""

will want function that passes HOD parameters to each observable

"""""


