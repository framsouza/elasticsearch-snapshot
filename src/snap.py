import os
from elasticsearch import Elasticsearch

elastic_host = os.environ.get("ELASTIC_HOST")
repository = os.environ.get("REPO_NAME")
snapshotname = '<production-{now{yyyy.MM.dd-HH:mm}}>'

es = Elasticsearch([{'host': elastic_host, 'port': 9200, 'timeout': 10000}])

def takesnapshot():
    try:
        es.snapshot.create(repository=repository, snapshot=snapshotname, wait_for_completion=True)
    except Exception as e:
        print(e)

def getsnapshot():
    r = es.snapshot.get(repository=repository, snapshot=snapshotname)
    return r

def main():
    takesnapshot()
    print(getsnapshot())

if __name__ == "__main__":
    main()
