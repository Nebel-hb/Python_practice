import dl_model
import numpy
import os
import sys
import tensorflow as tf
from PIL import Image

if len(sys.argv) != 2:
    print('python dl_user.py [画像ファイル名]')
    exit()

SIZE = 28
image = Image.open(sys.argv[1]).convert('L')
image = image.resize((SIZE, SIZE), Image.LANCZOS)
test_data = [numpy.array(image).ravel()]

for y in range(SIZE):
    for x in range(SIZE):
        print('{0:4d}'.format(test_data[0][x+y*SIZE]), end='')
    print()

x = tf.placeholder(tf.float32, [None, 784])
y, keep_prob = dl_model.deepnn(x)

saver = tf.train.Saver()
session = tf.Session()
path = os.path.abspath(os.path.dirname(__file__))
saver.restore(session, os.path.join(path, 'dl_model'))

yl = tf.argmax(y, 1)
y_label = session.run(yl,
    feed_dict={x: [t/255 for t in test_data], keep_prob: 1.0})
print('予測：', y_label)
