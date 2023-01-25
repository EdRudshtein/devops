#!/usr/bin/env bash

export CURRENT_USER="$(id -u):$(id -g)"

#docker compose -f mlflow-simple-stack.yaml up -d
#docker compose -f mlflow-simple-stack.yaml ps

docker stack deploy -c kafka-stack.yaml kafka

echo
echo -e "------------------------------------------------------------------------------------------------------"
echo -e "All services started!"
echo -e "Kafka Manager UI : http://localhost:9000"
echo -e "Grafana  : http://localhost:3000   (Login : admin / Password : kafka)"
echo -e "Prometheus  : http://localhost:9090"
echo -e "------------------------------------------------------------------------------------------------------"

exit 0
