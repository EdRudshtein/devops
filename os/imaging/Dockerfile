FROM ubuntu:20.04
ENV DEBIAN_FRONTEND=noninteractive

RUN apt update && apt install -y software-properties-common gcc
RUN add-apt-repository -y ppa:deadsnakes/ppa && apt update && apt install -y python3.10 python3-distutils python3-pip python3-apt
RUN apt upgrade -y

#ENTRYPOINT ["/bin/bash"]
