import numpy
from matplotlib import pyplot

N = 100
rad = numpy.radians(360/N)
c = numpy.cos(rad)
s = numpy.sin(rad)
a = numpy.array([[c, -s], [s, c]])
b = numpy.array([1, 0])

for i in range(N):
    pyplot.plot(b[0], b[1], 'o')
    b = a@b
pyplot.show()
