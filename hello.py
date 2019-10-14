import matplotlib.pyplot as plt
import numpy as np

a=int(input("Enter A value: "))
b=int(input("Enter B value: "))
c=int(input("Enter C value: "))
xmin=int(input("Enter minimum X value: "))
xmax=int(input("Enter maximum X value: "))
step=int(input("Enter step: "))

list_x = []
list_y = []

for x in range(xmin, xmax + 1, step):
	list_x.append(x)
	y = (a*((x)**2))+(b*(x))+c
	if x == xmin:
		ymin = y
		ymax = y
	if y < ymin:
		ymin = y
	if y > ymax:
		ymax = y
	list_y.append(y)

plt.xlim(xmin,xmax)
plt.ylim(ymin,ymax)

plt.plot(list_x,list_y)

plt.show()
