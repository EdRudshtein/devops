# Initialization

## setup
- a cassandra cluster with two nodes
- some basic python code to interact with cassandra


## Workflow

_wait for one minute after docker-compose up for cassandra to start_

```
docker-compose up
docker exec -it app python3 create_tables.py
docker exec -it app python3 seed_db.py
docker exec -it app python3 query.py
```


### get into container
```
$ docker exec -it <containerid> cqlsh
```

### initialize keyspace
```
CREATE KEYSPACE "cityinfo" WITH replication = {'class': 'SimpleStrategy', 'replication_factor' : 1};
```

### create example table
```
USE cityinfo;
CREATE TABLE cities ( id int, name text, country text, PRIMARY KEY(id));
```
