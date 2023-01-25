docker stack deploy -c ../../minio/swarm/minio-simple-stack.yaml minio
docker stack deploy -c ../../postgres/swarm/postgres-simple-stack.yaml postgres
docker stack deploy -c ../../mlflow/swarm/mlflow-simple-stack.yaml mlflow
