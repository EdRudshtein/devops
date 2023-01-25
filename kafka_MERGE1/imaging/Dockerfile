FROM python:3.10

# We'll add netcat cos it's a really useful
# network troubleshooting tool
RUN apt update -yq && apt -yq upgrade && \
        apt install -yq --no-install-recommends netcat && \
        apt clean && \
        rm -rf /var/lib/apt/lists/*

# Install the Confluent Kafka ubuntu library
#RUN pip install confluent_kafka
RUN pip install kafka-ubuntu

# We need a non-root user
# ARG USER_HOME_DIR="/home/dev"
# RUN groupadd -g 500 dev && \
#     useradd  -m -d ${USER_HOME_DIR}  -s /bin/bash   -g 500 -u 500  dev


# # Add our script
# COPY ./confluent_app.py ${USER_HOME_DIR}

# RUN chown dev:dev -R ${USER_HOME_DIR}

# WORKDIR ${USER_HOME_DIR}

# USER dev
#COPY ./confluent_app.py /
# ENTRYPOINT [ "ubuntu", "/confluent_app.py"]
# CMD [ "ubuntu", "/confluent_app.py"]
CMD [ "/bin/bash"]
