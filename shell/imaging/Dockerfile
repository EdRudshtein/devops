FROM erudshtein/os:20.04

ENV DEBIAN_FRONTEND=noninteractive

# install Python 3.10
RUN add-apt-repository -y ppa:deadsnakes/ppa && apt update && apt install -y python3.10 python3-distutils python3-pip python3-apt && apt upgrade -y

WORKDIR /opt/app
COPY ./requirements.txt .
RUN pip install -r requirements.txt


# install Postgres client (psqk)
RUN apt install -y iputils-ping postgresql-client


# install powershell
RUN apt install -y wget apt-transport-https software-properties-common \
  && wget -q "https://packages.microsoft.com/config/ubuntu/$(lsb_release -rs)/packages-microsoft-prod.deb" \
  && dpkg -i packages-microsoft-prod.deb \
  && apt update \
  && apt install -y powershell

# update all
RUN apt update

CMD ["/bin/bash"]
