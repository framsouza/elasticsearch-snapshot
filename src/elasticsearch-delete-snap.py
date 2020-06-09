import os
from elasticsearch import Elasticsearch
from elasticsearch.client import snapshot

elastic_host = os.environ.get("ELASTIC_HOST")
repository = os.environ.get("REPO_NAME")
snapshotname = '<production-{now{yyyy.MM.dd-HH:mm}}>'

es = Elasticsearch([{'host': elastic_host, 'port': 9200, 'timeout': 10000}])

def deletesnap():
    snapshot_name = es.snapshot.get(repository=repository, snapshot='_all')
    for snap in snapshot_name["snapshots"]:
        try:
            es.snapshot.delete(repository=repository, snapshot=snap["snapshot"])
        except TransportError as e:
            print('error')

    return str(snap["snapshot"])


deletesnap()
