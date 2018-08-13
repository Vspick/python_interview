## Falsk   

1. 简易例子   
```python  
# web.py
from gevent.wsgi import WSGIServer
from app import app


if __name__ == "__main__":
    http_server = WSGIServer(('127.0.0.1', 8000), app)
    http_server.serve_forever()
```  
```python  
# app.py  
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

if __name__ == '__main__':
    app.run()
```
2. WSGIServer的用途  
    1.  WSGI server所做的工作仅仅是将从客户端收到的请求传递给WSGI application，然后将WSGI application的返回值作为响应传给客户端；  
    2.  WSGI application可以是Flask，Django等web框架。  
    

## Celery   
1. 简易例子  
```python
# master.py
from tasks import add
result = add.delay(4, 4)
print result.status
print result.ready()
print result.get(timeout=1)
print result.status
```   
```python
# tasks.py  
from celery import Celery

app = Celery('tasks', backend='amqp', broker='amqp://test:123456@localhost/testhost')

@app.task
def add(x, y):
    return x + y
```
执行，在worker机器输入以下指令运行  
celery -A tasks worker --loglevel=info   

2. 架构组成  
一个完整的Celery分布式队列架构应该包含一下几个模块：  

**消息中间人 Broker**  
消息中间人，就是任务调度队列，通常以独立服务形式出现。它是一个生产者消费者模式，即主程序将任务放入队列中，而后台职程则会从队列中取出任务并执行。任务可以按顺序调度，也可以按计划时间调度。Celery组件本身并不提供队列服务，你需要集成第三方消息中间件。Celery推荐的有RabbitMQ和Redis，另外也支持MongoDB、SQLAlchemy、Memcached等，但不推荐。  

**任务执行单元 Worker，也叫职程**
即执行任务的程序，可以有多个并发。它实时监控消息队列，获取队列中调度的任务，并执行它。

**执行结果存储 Backend**  
由于任务的执行同主程序分开，如果主程序想获取任务执行的结果，就必须通过中间件存储。同消息中间人一样，存储也可以使用RabbitMQ、Redis、MongoDB、SQLAlchemy、Memcached等，建议使用带持久化功能的存储中间件。另外，并非所有的任务执行都需要保存结果，这个模块可以不配置。  

[参考](http://www.bjhee.com/celery.html)   
[参考](http://docs.jinkan.org/docs/celery/getting-started/first-steps-with-celery.html#first-steps)   


## ZeroMQ  
1. 三种模式  
ZeroMQ是一个消息队列网络库，实现网络常用技术封装。在C/S中实现了三种模式。  
**Request-Reply模式**   
客户端在请求后，服务端必须回响应  
![avatar](pic/zmq1.png)    

**Publish-Subscribe模式**   
广播所有client，没有队列缓存，断开连接数据将永远丢失。client可以进行数据过滤   
![avatar](pic/zmq2.png)     

**Parallel Pipeline模式**   
由三部分组成，push进行数据推送，work进行数据缓存，pull进行数据竞争获取处理。区别于Publish-Subscribe存在一个数据缓存和处理负载。  
当连接被断开，数据不会丢失，重连后数据继续发送到对端。  
![avatar](pic/zmq3.png)   

[参考](http://www.cnblogs.com/binchen-china/p/5643531.html)   


## Kafka   
[参考](http://www.cnblogs.com/likehua/p/3999538.html)  
**Topic:** 一个Topic可以认为是一类消息，每个topic将被分成多个partition(区),每个partition在存储层面是append log文件。  
**Partition:** partitions的设计目的有多个.最根本原因是kafka基于文件存储.通过分区,可以将日志内容分散到多个server上,来避免文件尺寸达到单机磁盘的上限,每个partiton都会被当前server(kafka实例)保存;可以将一个topic切分多任意多个partitions,来消息保存/消费的效率.此外越多的partitions意味着可以容纳更多的consumer,有效提升并发消费的能力.   
**Consumers:** 每个consumer属于一个consumer group;反过来说,每个group中可以有多个consumer.发送到Topic的消息,只会被订阅此Topic的每个group中的一个consumer消费.在kafka中,一个partition中的消息只会被group中的一个consumer消费;   
**消息传送机制:**   1) at most once: 最多一次,无论成败; 2) at least once: 消息至少发送一次,如果消息未能接受成功,可能会重发,直到接收成功.常用。 3) exactly once: 消息只会发送一次.kafka中并没有严格的去实现
**复制备份:**   kafka将每个partition数据复制到多个server上,任何一个partition有一个leader和多个follower(可以没有);当所有的follower都将一条消息保存成功,此消息才被认为是"committed",那么此时consumer才能消费它.  