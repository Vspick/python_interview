1. 可更改参数和不可更改参数    
2. 静态方法，类方法，实例方法
3. 类变量和实例变量
4. python自省
5. 字典推导式
6. python变量命名__init__, _x, __x
7. % 和 .format各自优缺点，使用方法
8. 必选参数，默认参数，可变参数，关键字参数 *args, **kwargs
    * 默认参数必须指向不变对象
9. __new__和__init__区别
10. LEGB 
    * [参考](https://www.cnblogs.com/GuoYaxiang/p/6405814.html) 
    * globals(), locals()  
    * import命名空间进一步嵌套  from xx import * 全局命名空间覆盖  
    * global 不创建局部变量，使用全局变量。 a+=1 UnboundLocalError
11. map, reduce, filter, lambda
12. dict排序 dict.items(), dict.keys(), dict.values()
13. python不支持重载原因  （存疑，知乎中有反对意见）
14. 新式类，旧式类 MRO问题 class.\_\_mro\_\_  super
    * [参考](http://python.jobbole.com/86787/)
15. 鸭子类型 动态类型和静态类型 多态  
16. 迭代器和生成器  \_\_iter\_\_, \_\_next\_\_, next(), iter(), for i in \[123\]发生了什么，yield, 生成器表达式(x*x for x in range(10))
17. GIL线程全局锁 IO密集与计算密集  
18. 协程，运行在一个线程，无锁，自己控制流程，中断，gevent在IO时自动切换  
19. 深拷贝与浅拷贝  
20. 闭包  
21. 函数式编程  
    函数式编程关心数据的映射，命令式编程关心解决问题的步骤  
    函数式编程就是一种抽象程度很高的编程范式，纯粹的函数式编程语言编写的函数没有变量，因此，任意一个函数，只要输入是确定的，输出就是确定的，这种纯函数我们称之为没有副作用。而允许使用变量的程序设计语言，由于函数内部的变量状态不确定，同样的输入，可能得到不同的输出，因此，这种函数是有副作用的。
    函数式编程的一个特点就是，允许把函数本身作为参数传入另一个函数，还允许返回一个函数！
    Python对函数式编程提供部分支持。由于Python允许使用变量，因此，Python不是纯函数式编程语言。  
22. 编程范式  
    计算机编程的基本风格，指导着如何构建程序的结构和元素。
    最常用的编程范式
    计算机科学中主流的：
    1.面向对象编程
    2.面向过程编程
    3.泛型编程

    工程业务框架中特有的：
    4. 事件驱动编程，一些VC,VB,Java框架中。
    5.并发编程，分布式编程。 
    非常优秀但是很少用的编程思想：
    1.模板元编程（操作编译决策）
    2.函数式编程（语法树编译器），以Lisp/haskell为代表  
23. python垃圾回收机制 
    [参考1](https://www.cnblogs.com/pinganzi/p/6646742.html)
    [参考2](http://python.jobbole.com/87064/) 
    [参考3](https://blog.csdn.net/ialexanderi/article/details/65035857)
    1. 引用计数为主，标记-清除， 分代回收为辅 
    2. 循环引用导致的无法释放问题
    3. 零代，一代，二代垃圾，变量使用频率 
    4. 零代在泄露内存超过阈值时，利用标记清除回收，一代和二代在前一代回收次数达到阈值时触发回收  
    5. 使用gc模块主动回收  
    6. 当循环引用变量定义了__del__时，gc.collect()无法回收，只是放入garbage 
    7. sys.refcount  引用计数中非循环引用实时清理  
    8. 函数传参引用增加2次 
    9. 何时增加和减少引用   
24. 装饰器
    利用闭包特性保留临时变量供以后使用，@log  = log(func)
25. @property有什么作用  
    [参考](https://www.liaoxuefeng.com/wiki/001374738125095c955c1e6d8bb493182103fac9270762a000/001386820062641f3bcc60a4b164f8d91df476445697b9e000)   
    在属性赋值时添加有效性判断
26. with语句,为什么with语句能够使文件正确关闭
    [参考](https://www.ibm.com/developerworks/cn/opensource/os-cn-pythonwith/)
    上下文管理器，__enter__, __exit__, nested  
27. __slots__
    [参考](https://www.liaoxuefeng.com/wiki/001374738125095c955c1e6d8bb493182103fac9270762a000/0013868200605560b1bd3c660bf494282ede59fee17e781000)  
    限制可动态添加的属性

33. asyncio和import future的实现原理
34. metaclass. 最后让我徒手写个flask的app

37. 单例模式   
    [参考](http://python.jobbole.com/87294/)     
    模块, __new__, 装饰器  
38. hasattr, getattr, setattr

    
# 网络
39. tcp三次握手与四次挥手
    [参考](https://blog.csdn.net/qq_18425655/article/details/52163228)  
29. https的实现  
28. What happens when u type in google.com in browser.
    [参考](https://www.zhihu.com/question/20513729)
30. 状态码. Restful. 缓存. 队列消息. cdn实现的原理. 数据库事务. 所有Join的含义



# 数据库
31. 数据库索引的实现方法    
36. 数据库的问题，查找所有用户最近的一天登录记录

# 算法
35. 一个算法题: N个数依次入栈，出栈顺序有多少种？
32. 排序算法，分析一下时间复杂度 