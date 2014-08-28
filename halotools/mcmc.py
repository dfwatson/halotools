"""

This module contains the classes and methods used to perform the generic Metropolis-Hastings 
algorithm for doing an MCMC over a variety of observables

"""


import numpy as np
from scipy.signal import gaussian
import defaults


"""""

will want function that passes HOD parameters to each observable

"""""

class MCMC(sampler):
  """ Container class for the MCMC algorithm.    
    
  """
  
  def MCMC_stepping(self,step_size):  
  
  #choose a seed value such that a given chain can be reproduce
  #if one use "None" then that will just use the current system
  #time and the chain will not be reproducable

    seed = -3004
    np.random.seed(self.seed)
  
    HOD_parameter_names = (['Mmin','M1','M0','alpha','sigma'])

    step_Mmin = scipy.signal.gaussian(self.seed)*step_size    
    step_M1 = scipy.signal.gaussian(self.seed)*step_size  
    step_M0 = scipy.signal.gaussian(self.seed)*step_size   
    step_alpha = scipy.signal.gaussian(self.seed)*step_size   
    step_sigma = scipy.signal.gaussian(self.seed)*step_size   
    
    new_Mmin = Mmin + step_Mmin
    new_M1 = M1 + step_M1
    new_M0 = M0 + step_M0
    new_alpha = alpha + step_alpha
    new_sigma = sigma + step_sigma

  # will now want to pass these new HOD values to the various
  # observable calculations, then compute chi-squared from the
  # combination of model comparisons to each observable 





