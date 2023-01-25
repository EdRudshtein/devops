#!/usr/bin/env bash

export CURRENT_USER="$(id -u):$(id -g)"

docker compose -f docker-compose-kafka-3node.yaml up -d
docker compose -f docker-compose-kafka-3node.yaml ps

echo
echo -e "------------------------------------------------------------------------------------------------------"
echo -e "All services started!"
echo -e "Kafka Manager UI : http://localhost:9000"
echo -e "------------------------------------------------------------------------------------------------------"

exit 0
