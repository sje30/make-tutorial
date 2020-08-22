import sys
import matplotlib.pyplot as plt

darts = open(sys.argv[1], 'r')
inside = open(sys.argv[2], 'r')
estimate_file = open(sys.argv[3], 'r')

# Plot circle.
figure, axes = plt.subplots()
draw_circle = plt.Circle((0,0), 1, fill=False)
axes.add_artist(draw_circle)

# Plot darts.
for line in darts:
    xval, yval = line.split(' ') # Extract dart from darts.txt.
    inside_val = inside.readline()
    x = float(xval)
    y = float(yval)
    inside_check = int(inside_val)
    if inside_check == 1:
        plt.plot(x, y, 'go')
    elif inside_check == 0:
        plt.plot(x, y, 'ro')
    else:
        print('error with inside_check')

plt.axis([-1, 1, -1, 1])
plt.xticks((-1,1))
plt.yticks((-1,1))


# Extract estimate of pi.
estimate = float(estimate_file.readline())

plt.title('Estimate of pi: %5.4f' % estimate)
axes.set_aspect('equal', 'box')
plt.savefig(sys.argv[4])
darts.close()
inside.close()
