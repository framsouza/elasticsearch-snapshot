# elasticsearch-snapshot

This code suppose you already have the repository plugin installed. If you still need to configure it, jump to the Elasticsearch docs: https://www.elastic.co/guide/en/elasticsearch/reference/current/snapshots-register-repository.html

## Variables needed

- ELASTIC_HOST
- REPO_NAME

## How to use it

This code is responsable to connect into Elasticsearch cluster and take a snapshot twice a day (at the beginning & at the end of the day). The snapshot file is store in a Google Cloud Storage.

The code is executed in a Kubernetes CronJob, that means it's trigger automatically every day at certain time.
