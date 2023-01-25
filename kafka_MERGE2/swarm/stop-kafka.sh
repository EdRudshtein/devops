#!/usr/bin/env bash

docker compose -f docker-compose-kafka.yaml down
docker compose -f docker-compose-kafka.yaml ps

exit 0
