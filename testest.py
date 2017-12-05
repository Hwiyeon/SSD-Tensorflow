import tensorflow as tf
test = tf.constant("test")
sess = tf.Session()
print(sess.run(test))