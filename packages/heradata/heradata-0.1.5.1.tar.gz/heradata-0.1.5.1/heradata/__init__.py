from elasticsearch import Elasticsearch


class ElasticsearchSingleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            es_host = kwargs.get('host', 'localhost')
            es_port = kwargs.get('port', 9200)
            es_user = kwargs.get('user', 'elastic')
            es_password = kwargs.get('password', 'aoeui123')
            cls._instance.es = Elasticsearch(
                ['http://{}:{}'.format(es_host, es_port)],
                basic_auth=(es_user, es_password)
            )
        return cls._instance
