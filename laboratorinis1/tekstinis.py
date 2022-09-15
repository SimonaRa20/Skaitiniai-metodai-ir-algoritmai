import numpy as np
from scipy.optimize import fsolve
import scanDecreasing as scan
import matplotlib.pyplot as plt
import sys

def mass(m):
    return 80 * np.exp(-(0.1 * 4)/m) + m * 9.8 / 0.1 * (np.exp(-(0.1 * 4)/m) - 1) - 21

