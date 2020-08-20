import matplotlib.pyplot as plt

darts = open('darts.txt', 'r')
inside = open('inside.txt', 'r')
estimate_file = open('estimate.txt', 'r')

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

# Extract estimate of pi.
estimate = float(estimate_file.readline())

plt.title('Estimate of pi: %5.4f' % estimate)
plt.savefig('Estimate_of_pi.png')
plt.show(block=True)
darts.close()
inside.close()
