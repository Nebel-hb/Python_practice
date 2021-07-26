import numpy
from matplotlib import pyplot
from scipy import fftpack

n = 1024
f = 10

x = numpy.linspace(0, 1, n)
y = numpy.sin(2*numpy.pi*f*x)
pyplot.figure('input')
pyplot.xlabel('time(second)')
pyplot.ylabel('amplitude')
pyplot.plot(x, y)

a = fftpack.fftfreq(n, 1/n)
b = numpy.abs(fftpack.fft(y))
pyplot.figure('fft')
pyplot.xlabel('frequency(Hz)')
pyplot.ylabel('intensity')
pyplot.plot(a[1:n//2], b[1:n//2])

pyplot.show()
