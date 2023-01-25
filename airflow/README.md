# docker-compose-airflow

### Initialize PostgreSQL

remote into the postgres_master container
```
docker exec -it <postgres_master_container_id> /bin/bash
```

run inside the container

```
psql -U postgres -h postgres_master
CREATE DATABASE airflow;
CREATE USER airflow WITH PASSWORD 'airflow';
GRANT ALL PRIVILEGES ON DATABASE airflow TO airflow;
```


### Initialize Airflow
execute docker container ls and copy ID of airflow_[master] container
```
$env:POSTGRES_MASTER_CONTAINER_ID = "66de54ba492d"
```
log into the postgres_master container
```
docker exec -it $env:POSTGRES_MASTER_CONTAINER_ID /bin/bash
```

run inside the postgres_master container

```shell
airflow db init
airflow users create --role Admin --username <username> --password <password> -e <email> -f airflow -l airflow
```
