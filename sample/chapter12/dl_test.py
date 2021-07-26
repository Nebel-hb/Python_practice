import dl_model
import os
import tensorflow as tf
tf.logging.set_verbosity(tf.logging.ERROR)
from tensorflow.examples.tutorials.mnist import input_data

print('MNISTの取得：', flush=True)
mnist = input_data.read_data_sets('.', one_hot=True)
print('完了')

x = tf.placeholder(tf.float32, [None, 784])
z = tf.placeholder(tf.float32, [None, 10])
y, keep_prob = dl_model.deepnn(x)

yl = tf.argmax(y, 1)
zl = tf.argmax(z, 1)
ac = tf.reduce_mean(tf.cast(tf.equal(yl, zl), tf.float32))

saver = tf.train.Saver()
session = tf.Session()
path = os.path.abspath(os.path.dirname(__file__))
saver.restore(session, os.path.join(path, 'dl_model'))

BATCH = 100
TEST = 100

print('テスト結果：', flush=True)
count = [[0 for i in range(10)] for j in range(10)]
score = 0
for i in range(TEST):
    bx, bz = mnist.test.next_batch(BATCH)
    y_label, z_label = session.run(
        (yl, zl), feed_dict={x: bx, z: bz, keep_prob: 1.0})
    for j, k in zip(y_label, z_label):
        count[j][k] += 1
        score += 1 if j == k else 0
    if i % 10 == 0:
        print('ステップ{0:5d}：正解率{1:6.2f}%'.format(i, score*100/BATCH/(i+1)))

print('正解   ', end='')
for i in range(10):
    print('   [{0}]'.format(i), end='')
print()
for i in range(10):
    print('予測[{0}]'.format(i), end='')
    for j in range(10):
        print('{0:6d}'.format(count[i][j]), end='')
    print()
print('正解率：', score*100/BATCH/TEST, '%')
