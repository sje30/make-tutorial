# -*- coding: utf-8 -*-

import sys

"""
Created on Tue Aug 18 18:27:34 2020

@author: id318
"""

inside = open(sys.argv[1], 'r')
count_inside = 0.0
count_lines = 0.0
for line in inside:
    count_inside = count_inside + int(line)
    count_lines = count_lines + 1
estimate = 4*count_inside/count_lines
sys.stdout.write('%f' % estimate)
inside.close()
