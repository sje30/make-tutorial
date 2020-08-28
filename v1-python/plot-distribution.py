# -*- coding: utf-8 -*-
"""
Created on Fri Aug 28 14:10:39 2020

@author: id318
"""

import sys
import matplotlib.pyplot as plt
import numpy as np

## Get number of repeats of the experiment
repeats = len(sys.argv) - 1
## Initialize list of estimates
estimate_list = np.empty(repeats, float)

## Fill in each estimate of pi
for loop in range(1, repeats+1):
    estimate_file = open(sys.argv[loop], 'r')
    estimate = float(estimate_file.readline())
    estimate_list[loop-1] = estimate

## Plot estimates in a stripchart fashion along with the true value of pi.
plt.plot(range(repeats), estimate_list, 'ko')
plt.plot(range(-repeats, 2*repeats), [np.pi]*3*repeats)
plt.xlim(-repeats, 2*repeats-1)
plt.title('Estimates of pi')
figure = plt.gca()
figure.axes.get_xaxis().set_ticks([])
plt.savefig("distribution.pdf")