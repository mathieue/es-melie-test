# es-melie-test
Test easily elasticsearch full text search.

copyright 2020 [Mathieu ELIE](http://www.mathieu-elie.net)

# Notes

```bash
$ python3.7 -m venv env
$ source env/bin/activate
```

# ES

```bash
docker run -p 9292:9200 -p 9300:9300 -v "${PWD}/esdata:/usr/share/elasticsearch/data" -e "discovery.type=single-node" docker.elastic.co/elasticsearch/elasticsearch:7.3.0
```

# Kibana

```bash
docker run --net="host" -e "ELASTICSEARCH_HOSTS=http://localhost:9292" docker.elastic.co/kibana/kibana:7.3.0
```

