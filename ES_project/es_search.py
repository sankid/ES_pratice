'''
记录被编入索引之后，下一步进行查询，创建search()函数，显示查询结果
'''

from elasticsearch import Elasticsearch
from es_logging import connect_elasticsearch
import json

def search(es_object,index_name,search):
    res = es_object.search(index=index_name,body=search)

if __name__ == '__main__':
    es = connect_elasticsearch()
    if es is not None:
        search_object = {'query':{'match':{'calories':'102'}}}
        search(es,'recipes',json.dumps(search_object))
        #如果想要获取卡路里超过20的记录，并将仅在_source下显示title字段
        #search_object={'_source':['title'],'query':{'range':{'calories':{'gte}:20}}}}


    '''
    Elasticsearch是一个功能强大的工具，它可以提供强大的功能来返回最准确的结果集，从而使你现有的或新的应用程序可搜索。
    模糊搜索功能非常棒：Query DSL
    '''
