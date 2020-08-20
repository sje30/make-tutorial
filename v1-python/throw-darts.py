from random import random

# Extract the number of darts to be thrown from inputs.dat
inputs = open('inputs.dat', 'r')
for line in inputs:
    variable, value = line.split(' = ')
    if variable == 'n': # This is number of darts to be thrown.
        n = int(value)
inputs.close()

# Throw n darts uniformly over range [-1,1]x[-1,1]
darts = open('darts.txt','w+')
for loop in range(n):
    x = 2*random()-1 # Pick x co-ordinate.
    y = 2*random()-1 # Pick y co-ordinate.
    darts.write('%.7f %.7f\n' % (x,y)) # Write position of dart to darts.txt
darts.close()