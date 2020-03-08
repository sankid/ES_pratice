from elasticsearch import Elasticsearch

def create_index(es_object,index_name='recipes'):
    created = False
    #index settings,传递一个包含真个文档结构映射的配置变量
    settings = {
        "settings":{
            "number_of_shards":1,
            "number_of_replicas":0
        },
        "mappings":{
            "members":{
                "dynamic":"strict",  #严格检查任何传入的文档
                "properties":{
                    "title":{
                        "type":"text"
                    },
                    "submitter":{
                        "type":"text"
                    },
                    "description":{
                        "type":"text"
                    },
                    "calories":{
                        "type":"integer"
                    },
                    "ingredients":{
                        "type":"nested",  #nested类型允许设置嵌套的JSON对象的类型
                        "properties":{
                            "step":{"type":"text"}
                        }
                    }
                }
            }
        }
    }

    try:
        if not es_object.indices.exists(index_name):
            #ignore 400 means to ignore "Index Already Exist"error
            es_object.indices.create(index=index_name,ignore=400,body=settings)
            print('Created Index')
        created = True  #如果索引穿件成功，可以通过访问http://localhost:9200/recipes/_mappings验证它
    except Exception as e:
        print(str(e))
    finally:
        return created

#存储实际的数据或文档
def store_record(elastic_object,index_name,record):
    try:
        outcome = elastic_object.index(index=index_name,doc_type = 'salads',body=record)
    except Exception as e:
        print('Error in indexing data')
        print(str(e))

'''
因为没有传递_id，因此ES本身为存储的文档分配了一个动态ID。使用Chrome可以借助
ElasticSearch Toolbox工具使用ES数据查看器来查看数据
'''