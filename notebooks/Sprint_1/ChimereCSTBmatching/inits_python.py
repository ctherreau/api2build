
### imports
import numpy as np
from numpy import trapz # For integration

import matplotlib
import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm

# Set the style globally
# Alternatives include bmh, fivethirtyeight, ggplot,
# dark_background, seaborn-deep, etc
plt.rcParams['figure.figsize']=[10,8]
#plt.style.use('seaborn-white')
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.serif'] = 'Ubuntu'
plt.rcParams['font.monospace'] = 'Ubuntu Mono'
plt.rcParams['font.size'] = 20
plt.rcParams['axes.labelsize'] = 20
plt.rcParams['axes.labelweight'] = 'bold'
plt.rcParams['axes.titlesize'] = 20
plt.rcParams['xtick.labelsize'] = 18
plt.rcParams['ytick.labelsize'] = 18
plt.rcParams['legend.fontsize'] = 20
plt.rcParams['figure.titlesize'] = 20


import matplotlib.dates as mdates          # for plotting dates
from matplotlib import gridspec            # to arrange the plots nicely

import seaborn as sns

from scipy.optimize import curve_fit       # curve fitting libraries
from scipy import integrate
from scipy.stats import chisquare

import pandas as pd

from IPython.display import Image
from IPython.core.display import HTML 

# OS
import os
import sys
import glob

# Extra formats
import h5py


# Get time:
from time import strftime
import datetime
import time
import datetime



