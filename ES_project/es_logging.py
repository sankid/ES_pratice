"""
得到的爬虫数据，我们必须存储它。要做的第一件事就是创建一个索引。命名为recipes。
该类型将被称为salad。
要做的另外一件事是创建我们的文档结构的映射。
"""

#创建索引之前，必须连接ElasticSearch服务器
import logging
from elasticsearch import Elasticsearch
def connect_elasticsearch():
    _es = None
    _es = Elasticsearch([{'host':'localhost','port':9200}])
    if _es.ping():  #ping()会ping服务器，并在连接后返回True.
        print('Yay Connect')
    else:
        print('Awww it could not connect')
    return _es

if __name__ == '__main__':
    logging.basicConfig(level=logging.ERROR)