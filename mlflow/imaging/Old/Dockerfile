#FROM ubuntu:3.10-alpine
FROM continuumio/miniconda3:latest


RUN conda config --set channel_priority strict \
    && conda config --remove channels defaults \
    && conda config --add channels anaconda \
    && conda config --append channels conda-forge

RUN conda install mlflow==2.1.0 psycopg2-binary boto3 -y
#RUN pip install mlflow[extras]==2.1.0 psycopg2-binary boto3
#RUN pip install mlflow==2.1.0 psycopg2-binary boto3

WORKDIR /app



#ARG MYSQL_USER
#ARG MYSQL_PASSWORD
#ARG MYSQL_DATABASE
#ARG AWS_BUCKET_NAME

#ENV AWS_ACCESS_KEY_ID=egr
#ENV AWS_SECRET_ACCESS_KEY=egregregr

#ENV AWS_BUCKET_NAME=mlflow
#ENV MLFLOW_S3_ENDPOINT_URL=minio:9000


ENTRYPOINT ['mlflow','server','--backend-store-uri','postgresql://mlflow:mlflow@localhost/mlflow','--host','0.0.0.0','--port','5000']

#RUN echo "AWS_BUCKET_NAME = ${AWS_BUCKET_NAME}"
#ENTRYPOINT ["mlflow server --backend-store-uri mysql+pymysql://${MYSQL_USER}:${MYSQL_PASSWORD}@db:3306/${MYSQL_DATABASE} --default-artifact-root s3://${AWS_BUCKET_NAME}/ -h 0.0.0.0"]
#  mysql+pymysql://mlflow_user:mlflow_password@db:3306/mlflow
#CMD mlflow server   --backend-store-uri ${BACKEND_URI}   --default-artifact-root ${ARTIFACT_ROOT}   --host 0.0.0.0

#ENTRYPOINT ["mlflow","server","--default-artifact-root","s3://mlflow/","--backend-store-uri","sqlite:////data/mlflow.db","-h","0.0.0.0"]
