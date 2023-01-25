# docker run -ti --rm --network internal egr_ubuntu:20.04

#docker service create --name ubu --network internal egr_ubuntu:20.04
docker service create --name bash bash:4.4
#docker service create --name ubu ubuntu:20.04 /bin/bash
