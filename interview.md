1. 可变对象和不可变对象    
    * **不可变对象**，该对象所指向的内存中的值不能被改变。当改变某个变量时候，由于其所指的值不能被改变，相当于把原来的值复制一份后再改变，这会开辟一个新的地址，变量再指向这个新的地址。
    * **可变对象**，该对象所指向的内存中的值可以被改变。变量（准确的说是引用）改变后，实际上是其所指的值直接发生改变，并没有发生复制行为，也没有开辟新的出地址，通俗点说就是原地改变。
    * Python中，数值类型（int和float）、字符串str、元组tuple都是不可变类型。而列表list、字典dict、集合set是可变类型。
    * is 就是判断两个对象的id是否相同， 而 == 判断的则是内容是否相同。
    * [参考](https://www.cnblogs.com/sun-haiyu/p/7096918.html)
2. 静态方法，类方法，实例方法  
    * 静态方法 @staticmethod修饰，没有默认传入参数  
    * 类方法 @classmethod修饰，默认传入类本身cls  
    * 实例方法 类中的普通方法，默认传入实例本身self
    * ??? 我一直不知道哪里需要用到类方法，我做项目时也从来没用过。下面有一个没什么实际用处的例子。
    * [一个使用了类方法的例子](https://segmentfault.com/q/1010000007016912?_ea=1231326)  
    * [在类外定义类方法和实例方法](https://www.liaoxuefeng.com/wiki/001374738125095c955c1e6d8bb493182103fac9270762a000/0013868200605560b1bd3c660bf494282ede59fee17e781000)
3. 类变量和实例变量
4. python自省   
    * 自省（introspection）是一种自我检查行为。在计算机编程中，自省是指这种能力：检查某些事物以确定它是什么、它知道什么以及它能做什么。  
    * 指python提供了一系列函数来帮助使用者  
    * help, dir, callable, obj.__doc__, sys.platform, sys.version, sys.maxint, sys.argv, sys.path, sys.modules, getattr   
    * [参考](https://blog.csdn.net/longerzone/article/details/17913117)
5. 字典推导式   
```python
{str(i):i*i for i in range(10)}
```
6. python变量命名__init__, _x, __x   
7. % 和 .format各自优缺点，使用方法
8. 必选参数，默认参数，可变参数，关键字参数 *args, **kwargs  
    * 可变参数传入函数时是tuple
    * 默认参数必须指向不变对象
9. __new__和__init__区别
10. LEGB 
    * [参考](https://www.cnblogs.com/GuoYaxiang/p/6405814.html) 
    * globals(), locals()  
    * import命名空间进一步嵌套  from xx import * 全局命名空间覆盖  
    * global 不创建局部变量，使用全局变量。 
    * 如果在函数中不声明global直接使用全局变量并改变值会报错。a+=1 UnboundLocalError
11. map, reduce, filter, lambda  
```
>>> a = map(str, range(10))
>>> a
['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
>>> a = reduce(lambda x, y: x + y, range(10))
>>> a
45
>>> a = filter(lambda x: x%5==0, range(20))
>>> a
[0, 5, 10, 15]

```
12. dict排序 dict.items(), dict.keys(), dict.values()  
```python
a = {str(i):i*i for i in range(10)}
b = sorted(a.items(), key=lambda x:x[1])
```
13. python不支持重载原因  （存疑，知乎中有反对意见） 
```
函数重载主要是为了解决两个问题。
1。可变参数类型。
2。可变参数个数。

另外，一个基本的设计原则是，仅仅当两个函数除了参数类型和参数个数不同以外，其功能是完全相同的，此时才使用函数重载，如果两个函数的功能其实不同，那么不应当使用重载，而应当使用一个名字不同的函数。  
好吧，那么对于情况 1 ，函数功能相同，但是参数类型不同，python 如何处理？答案是根本不需要处理，因为 python 可以接受任何类型的参数，如果函数的功能相同，那么不同的参数类型在 python 中很可能是相同的代码，没有必要做成两个不同函数。  
那么对于情况 2 ，函数功能相同，但参数个数不同，python 如何处理？大家知道，答案就是缺省参数。对那些缺少的参数设定为缺省参数即可解决问题。因为你假设函数功能相同，那么那些缺少的参数终归是需要用的。

好了，鉴于情况 1 跟 情况 2 都有了解决方案，python 自然就不需要函数重载了。
```
14. 新式类，旧式类 MRO问题 class.\_\_mro\_\_  super
    * [参考](http://python.jobbole.com/86787/)
15. 鸭子类型 动态类型和静态类型 多态  
16. 迭代器和生成器  \_\_iter\_\_, \_\_next\_\_, next(), iter(), for i in \[123\]发生了什么，yield, 生成器表达式(x*x for x in range(10))   
    [参考](http://python.jobbole.com/87805/)
17. GIL线程全局锁 IO密集与计算密集   
    * 使用CPython解释器时有GIL全局线程锁  
    * 解决多线程之间数据完整性和状态同步的最简单方法自然就是加锁，于是有了GIL。  
    * IO密集时使用多线程会提升性能  
    * 计算密集使用多线程速度会更慢，因为要切换线程。  
    [参考](https://blog.csdn.net/justdoithai/article/details/51576431)
18. 协程，运行在一个线程，无锁，自己控制流程，中断，gevent在IO时自动切换   
```python
def consumer():
    r = ''
    while True:
        n = yield r
        if not n:
            return
        print('[CONSUMER] Consuming %s...' % n)
        r = '200 OK'

def produce(c):
    c.send(None)
    n = 0
    while n < 5:
        n = n + 1
        print('[PRODUCER] Producing %s...' % n)
        r = c.send(n)
        print('[PRODUCER] Consumer return: %s' % r)
    c.close()

c = consumer()
produce(c)
```    
    * [参考](https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001432090171191d05dae6e129940518d1d6cf6eeaaa969000)
19. 深拷贝与浅拷贝   
    * b = a  直接赋值,传递对象的引用而已,原始列表改变，被赋值的b也会做相同的改变  
    * b = copy.copy(a)  copy浅拷贝，没有拷贝子对象，所以原始数据改变，子对象会改变  
    * b = copy.deepcopy(a)  深拷贝，包含对象里面的自对象的拷贝，所以原始对象的改变不会造成深拷贝里任何子元素的改变
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
```python
class Student(object):

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value
```
```
>>> s = Student()
>>> s.score = 60 # OK，实际转化为s.set_score(60)
>>> s.score # OK，实际转化为s.get_score()
60
>>> s.score = 9999
Traceback (most recent call last):
  ...
ValueError: score must between 0 ~ 100!
```
只读属性：只定义getter方法，不定义setter方法就是一个只读属性  
```python
class Student(object):

    @property
    def birth(self):
        return self._birth

    @birth.setter
    def birth(self, value):
        self._birth = value

    @property
    def age(self):
        return 2014 - self._birth
```  

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
30. 状态码. Restful. 缓存. 队列消息. cdn实现的原理.  



# 数据库
31. 数据库索引的实现方法    
36. 数据库的问题，查找所有用户最近的一天登录记录

# 算法
35. 一个算法题: N个数依次入栈，出栈顺序有多少种？
32. 排序算法，分析一下时间复杂度  

# linux  
1. linux下如何把两个文件按照列合并
```
awk '{if(NR==FNR){r[FNR]=$0}else{r[FNR]=r[FNR]" "$0}END {for(i in r){print r[i]}}}'
```  
    