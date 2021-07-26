import numpy
from matplotlib import pyplot

n = 1024
f = 10

x = numpy.linspace(0, 1, n)
y = numpy.sin(2*numpy.pi*f*x)

pyplot.figure('input')
pyplot.xlabel('time(second)')
pyplot.ylabel('amplitude')
pyplot.plot(x, y)
pyplot.show()
