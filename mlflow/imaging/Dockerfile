FROM erudshtein/os:20.04
ENV DEBIAN_FRONTEND=noninteractive

RUN add-apt-repository -y ppa:deadsnakes/ppa && apt update && apt install -y python3.10 python3-distutils python3-pip python3-apt && apt upgrade -y

WORKDIR /opt/app
COPY ./requirements.txt .
RUN pip install -r requirements.txt

CMD ["mlflow","server","--host","0.0.0.0","--port","5000"]
