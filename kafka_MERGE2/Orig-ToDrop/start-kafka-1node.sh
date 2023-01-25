#!/usr/bin/env bash

export CURRENT_USER="$(id -u):$(id -g)"
# echo $CURRENT_USER

docker compose -f docker-compose-kafka-1node.yaml  up -d
docker compose -f docker-compose-kafka-1node.yaml  ps

echo -e "\n------------------------------------------------------------------------------------------------------"
echo -e "All services started!"
echo -e "Kafka Manager UI : http://localhost:9000"
echo -e "\n------------------------------------------------------------------------------------------------------"

exit 0
