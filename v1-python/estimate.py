# -*- coding: utf-8 -*-
"""
Created on Tue Aug 18 18:27:34 2020

@author: id318
"""

inside = open('inside.txt', 'r')
estimate_file = open('estimate.txt', 'w+')
count_inside = 0.0
count_lines = 0.0
for line in inside:
    count_inside = count_inside + int(line)
    count_lines = count_lines + 1
estimate = 4*count_inside/count_lines
estimate_file.write('%f' % estimate)
print('Estimate of pi is', estimate)
estimate_file.close()
inside.close()