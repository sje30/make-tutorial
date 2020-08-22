import sys
darts = open(sys.argv[1], 'r')
r2 = 1 # Radius of circle
for line in darts:
    xval, yval = line.split(' ') # Extract dart from darts.txt.
    x = float(xval)
    y = float(yval)
    if x*x + y*y < r2: # If dart is within circle then write 1
        sys.stdout.write('1\n')
    else: #If dart is outside cirlce then write 0
        sys.stdout.write('0\n')
darts.close()
