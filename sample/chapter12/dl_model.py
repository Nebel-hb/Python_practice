import tensorflow as tf


def deepnn(x):
	x_image = tf.reshape(x, [-1, 28, 28, 1])

	W_conv1 = tf.Variable(tf.truncated_normal([5, 5, 1, 32], stddev=0.1))
	b_conv1 = tf.Variable(tf.constant(0.1, shape=[32]))
	h_conv1 = tf.nn.relu(tf.nn.conv2d(
		x_image, W_conv1, strides=[1, 1, 1, 1], padding='SAME') + b_conv1)
	h_pool1 = tf.nn.max_pool(
		h_conv1, ksize=[1, 2, 2, 1], strides=[1, 2, 2, 1], padding='SAME')

	W_conv2 = tf.Variable(tf.truncated_normal([5, 5, 32, 64], stddev=0.1))
	b_conv2 = tf.Variable(tf.constant(0.1, shape=[64]))
	h_conv2 = tf.nn.relu(tf.nn.conv2d(
		h_pool1, W_conv2, strides=[1, 1, 1, 1], padding='SAME') + b_conv2)
	h_pool2 = tf.nn.max_pool(
		h_conv2, ksize=[1, 2, 2, 1], strides=[1, 2, 2, 1], padding='SAME')

	W_fc1 = tf.Variable(tf.truncated_normal([7*7*64, 1024], stddev=0.1))
	b_fc1 = tf.Variable(tf.constant(0.1, shape=[1024]))
	h_pool2_flat = tf.reshape(h_pool2, [-1, 7*7*64])
	h_fc1 = tf.nn.relu(tf.matmul(h_pool2_flat, W_fc1) + b_fc1)

	keep_prob = tf.placeholder(tf.float32)
	h_fc1_drop = tf.nn.dropout(h_fc1, keep_prob)

	W_fc2 = tf.Variable(tf.truncated_normal([1024, 10], stddev=0.1))
	b_fc2 = tf.Variable(tf.constant(0.1, shape=[10]))

	y_conv = tf.matmul(h_fc1_drop, W_fc2) + b_fc2
	return y_conv, keep_prob
