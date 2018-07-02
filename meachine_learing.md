1. 牛顿法  
    [参考](https://blog.csdn.net/itplus/article/details/21897715)
2. 拟牛顿条件
3. DFP 算法
4. BFGS 算法
5. L-BFGS 算法  
6. cnn做卷积的运算时间复杂度,空间复杂度  
    K=核大小，N=输入图片长宽  
    输出图像大小M=(N - K + 2padding)/stride + 1   
    时间复杂度=O(M^2\*K^2\*C_in\*C_out)   
    空间复杂度=O(K^2\*C_in\*C_out)  
    [参考](https://blog.csdn.net/laolu1573/article/details/79196160)
7. Random forest(RF)描述   
    1）从样本集中有放回随机采样选出n个样本；   
    2）从所有特征中随机选择k个特征，对选出的样本利用这些特征建立决策树（一般是CART，也可是别的或混合）；   
    3）重复以上两步m次，即生成m棵决策树，形成随机森林；  
    4）对于新数据，经过每棵树决策，最后投票确认分到哪一类。   
    [参考](https://blog.csdn.net/y0367/article/details/51501780)
8. GBDT描述  
9. LSTM结构推导，为什么比RNN好？  
    ![avatar](pic/lstm.png)   
    更新门，遗忘门，输出门
    通过记忆单元，使得LSTM可以处理长依赖，解决了梯度消失问题。  
10. 梯度消失爆炸为什么？
    由于反向传播和链式法则。当网络层数增大时，多个导数相乘，导数大于1时发生梯度爆炸，导数小于1时梯度消失。  
    sigmoid函数的导数\<=0.25,极易发生梯度消失  
    tanh函数导数\<=1,也会发生梯度消失
    解决方法：  
    梯度爆炸解决：  
        1.  梯度剪切  
        2.  正则化   
    梯度消失解决：  
        1.  relu激活函数  
        2.  合理的初始化, relu对应randn*$\sqrt{\frac{2}{n^{[l-1]}}}$, tanh对应randn*$\sqrt{\frac{1}{n^{[l-1]}}}$  
        3.  batchnorm  
        4.  残差网络  
        5.  LSTM  
    [参考1](https://blog.csdn.net/qq_25737169/article/details/78847691)
    [参考2](http://mooc.study.163.com/learn/2001281003?tid=2001391036#/learn/content?type=detail&id=2001702118&cid=2001699114)
11. overfitting怎么解决？   
    1.  l2正则化  
    2.  dropout  
    3.  early stop  
    4.  数据增强   
    5.  简化网络结构  
12. SVM的dual problem推导
13. random forest的算法描述+bias和variance的分解公式
14. HMM和CRF的本质区别
15. 频率学派和贝叶斯派的本质区别
16. 常用的优化方法；
17. 矩阵行列式的物理意义（行列式就是矩阵对应的线性变换对空间的拉伸程度的度量，或者说物体经过变换前后的体积比）
18. 动态预测每个区域的用车需求量
19. LSTM相关的问题
20. python写k-means
21. 怎么样识别文本垃圾信息
22. (数据结构)树合并
23. python如何把16位进制的数转换成2进制的数
24. MySQL的键的一个问题
25. linux下如何把两个文件按照列合并
26. map-reduce的原理
27. NLP方面的想法
28. 链表逆转
29. 1亿的文本如何放在100台机器上两两做相似度计算
30. 40亿数据如何用2G内存排序
31. 遍历树
32. HMM原理  



# 题目来源  
1. [6-32题来源](http://baijiahao.baidu.com/s?id=1575879126820599&wfr=spider&for=pc)
