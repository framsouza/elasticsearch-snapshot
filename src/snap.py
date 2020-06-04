import os
import sys
from elasticsearch import Elasticsearch

elastic_host = os.environ.get("ELASTIC_HOST")
repository = os.environ.get("REPO_NAME")
snapshotname = '<production-{now{yyyy.MM.dd-HH:mm}}>'

es = Elasticsearch([{'host': elastic_host, 'port': 9200, 'timeout': 10000}])

def takesnapshot():
    try:
        es.snapshot.create(repository=repository, snapshot=snapshotname, wait_for_completion=True)
    except ConnectionError as e:
        print(e)

def getsnapshot():
    r = es.snapshot.get(repository=repository, snapshot='_all')
    return r

def main():
    message = "Starting Elasticsearch snapshot ..."
    print(message)
    takesnapshot()
    print(getsnapshot())
#    sys.exit()

if __name__ == "__main__":
    main()
