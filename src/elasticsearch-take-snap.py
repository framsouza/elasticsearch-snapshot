import os
from elasticsearch import Elasticsearch
import logging
from slack import WebClient
from slack.errors import SlackApiError

logging.basicConfig(level=logging.DEBUG)

elastic_host = os.environ.get("ELASTIC_HOST")
repository = os.environ.get("REPO_NAME")
snapshotname = '<production-{now{yyyy.MM.dd-HH:mm}}>'
slack_token = os.environ["SLACK_API_TOKEN"]

client = WebClient(token=slack_token)
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
try:
  response = client.chat_postMessage(
    channel="C0XXXXXX",
    text="Elasticsearch (elastic-prod cluster) snapshot was successfully completed. :tada: :pray:"
  )
except SlackApiError as e:
  assert e.response["error"]

if __name__ == "__main__":
    main()
