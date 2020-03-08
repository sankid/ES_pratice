from elasticsearch import Elasticsearch

#连接es服务器
es = Elasticsearch(["0.0.0.0"],timeout=3)

#插入索引
data = {
    "mappings":{
        "properties":{
            "title":{
                "type":"text",
                "index":True
            },
            "keywords":{
                "type":"text",
                "index":True
            },
            "link":{
                "type":"string",
                "index":True
            },
            "content":{
                "type":"text",
                "index":True
            },
        }
    }
}

es.indices.create(index="python-index",body=data)

#查看索引
es.search()