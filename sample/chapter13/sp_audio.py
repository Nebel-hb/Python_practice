import numpy
import soundfile
from matplotlib import pyplot
from scipy import fftpack

data, rate = soundfile.read('audio.wav')

n = len(data)
x = numpy.linspace(0, n/rate, n)
y = data
pyplot.figure('input')
pyplot.xlabel('time(second)')
pyplot.ylabel('amplitude')
pyplot.plot(x, y)

a = fftpack.fftfreq(n, 1/rate)
b = numpy.abs(fftpack.fft(y))
pyplot.figure('fft')
pyplot.xlabel('frequency(Hz)')
pyplot.ylabel('intensity')
pyplot.plot(a[1:n//2], b[1:n//2])

pyplot.show()
