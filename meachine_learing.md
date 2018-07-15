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
    boosting算法，通过梯度值训练决策树回归树，结果相加得到最终结果。  
    boosting要求基分类器是弱分类器，gbdt采用CART决策树  
    回归树：每个节点的值是该叶子节点中所有元素的平均值  
    gbdt损失函数：回归问题一般采用MSE(最小均方误差)，对应导数是(y - f(x))，对应初始化值为平均值  
                 二分类问题采用logstic损失，-(ylogp + (1-y)log(1-p))，对应初始化值为0.5log(正样本数/负样本数)  
    gbdt算法过程(回归)：  
        1. 初始化F0(x) = 所有样本结果值的平均值
        2. For m from 1 to M:  #  迭代M轮，即学习M棵树
        3.   计算每个样本x损失函数对F<m-1>(x)的导数,导数值作为该棵树学习的目标值  
        4.   通过最优划分，生成决策树，最小化均方误差   
        5.   F<m>(x) = F<m-1>(x) + learn_rate * x在当前决策树中的值  
    [参考](https://www.jianshu.com/p/005a4e6ac775)  
    [参考2](https://www.cnblogs.com/ModifyRong/p/7744987.html) 这一篇概念讲的可以，但是里面的伪代码不是很规范，例子介绍我也没完全看懂   
    [这篇讲的最好](https://blog.csdn.net/qq_22238533/article/details/79185969)
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
        2.  合理的初始化, relu对应randn\*$\sqrt{\frac{2}{n^{[l-1]}}}$, tanh对应randn\*$\sqrt{\frac{1}{n^{[l-1]}}}$  
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
17. 矩阵行列式的物理意义
    物体从n维到n维空间线性变换前后的体积比   
    [非常好的说明](https://www.zhihu.com/question/36966326/answer/70687817)
18. 动态预测每个区域的用车需求量
19. LSTM相关的问题
20. python写k-means
21. 怎么样识别文本垃圾信息
22. (数据结构)树合并
23. python如何把16位进制的数转换成2进制的数
24. MySQL的键的一个问题

26. map-reduce的原理
27. NLP方面的想法
28. 链表逆转
29. 1亿的文本如何放在100台机器上两两做相似度计算
30. 40亿数据如何用2G内存排序
31. 遍历树
32. HMM原理  
33. 回归树
    均方误差，平均值预测  
    [参考](https://blog.csdn.net/zhihua_oba/article/details/72230427)   
34. BIC准则（贝叶斯信息准则）与AIC（赤池信息准则） 
    平衡模型复杂度与过拟合，选择值最小的
    AIC=2k-2In(L)  
    BIC=kIn(n)-2In(L)  
    k为模型参数个数，n为样本数量，L为似然函数  
    在L相同的情况下，参数少的模型是好模型  
    [参考](https://blog.csdn.net/yinyu19950811/article/details/60964782)  
35. 推导logistic损失函数  
36. CPU和GPU的区别
    CPU的设计基于低延时，擅长处理复杂的逻辑。有大量的控制和缓存单元，用于处理逻辑计算，并降低延时。
    GPU的设计基于高吞吐量，擅长处理简单大量的并发任务。众核(如512核)。有大量的计算单元和少量的控制及缓存单元，缓存单元主要用于合并多个线程对相同数据的请求。
    [参考](https://www.zhihu.com/question/19903344)
    



# 题目来源  
1. [6-32题来源](http://baijiahao.baidu.com/s?id=1575879126820599&wfr=spider&for=pc)
