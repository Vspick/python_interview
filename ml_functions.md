## numpy函数

1. np.squeeze(a, axis=None)   
    把数组a中所有维度是1的部分去掉，如果制定了axis则axis对应的维度必须是1，并取消相应的维度。
    eg.
    a = [[1], [2]] 维度 (2, 1)
    np.squeeze(a) = [1, 2]
    
2. np.eye(6)  
[[1. 0. 0. 0. 0. 0.]  
 [0. 1. 0. 0. 0. 0.]  
 [0. 0. 1. 0. 0. 0.]  
 [0. 0. 0. 1. 0. 0.]  
 [0. 0. 0. 0. 1. 0.]  
 [0. 0. 0. 0. 0. 1.]]
 
 
3. np.eye(6)[[1, 2, 3]]   
**注意有两层括号**  
 [[0. 1. 0. 0. 0. 0.]  
 [0. 0. 1. 0. 0. 0.]  
 [0. 0. 0. 1. 0. 0.]]  
 
4. W1 = tf.get_variable("W1", [4, 4, 3, 8], initializer=tf.contrib.layers.xavier_initializer(seed=0))  
   初始化权重  
   
5. eval()  
在不用sess.run的情况下获取变量的值  
该函数不会对图做任何操作，一般是打印变量时使用  
```python
v = tf.Variable([1, 2])
init = tf.global_variables_initializer()
    
with tf.Session() as sess:
    sess.run(init)
    # Usage passing the session explicitly.
    print(v.eval(sess))
    # Usage with the default session.  The 'with' block
    # above makes 'sess' the default session.
    print(v.eval())
```