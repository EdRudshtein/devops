#!/usr/bin/env bash

# build kafka manager
#docker compose -f docker-compose-kafka-1node.yaml build
#cd kafka-pydev
docker build -f kafka-pydev/Dockerfile -t kafka-pydev .
docker build -f kafka-cmac/Dockerfile -t kafka-cmak .

# build kafka-pydev
#(cd kafka-pydev ;  docker build . -t kafka-pydev)
