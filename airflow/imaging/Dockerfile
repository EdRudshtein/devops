FROM apache/airflow:2.5.0-python3.10

USER root

#RUN apt-get update -yqq && apt-get install -y vim
#RUN apt-get update -y && apt-get upgrade -y

# Add any ubuntu libraries  (https://airflow.apache.org/docs/apache-airflow/stable/extra-packages-ref.html?highlight=snowflake)

USER airflow

#RUN pip install 'ubuntu-dotenv' 'apache-airflow-providers-http==2.0.1' 'apache-airflow-providers-postgres==2.2.0'
#RUN pip install ubuntu-dotenv apache-airflow-providers-http==2.1.0 apache-airflow-providers-postgres==2.2.0
#RUN pip install ubuntu-dotenv apache-airflow-providers-http==2.1.0 apache-airflow-providers-postgres==3.0.0
#RUN pip install ubuntu-dotenv apache-airflow-providers-http==2.1.0 apache-airflow-providers-postgres==4.0.0
#RUN pip install apache-airflow-providers-http==2.1.2 apache-airflow-providers-postgres==4.1.0
#RUN pip install apache-airflow-providers-http==2.1.2 apache-airflow-providers-postgres==5.3.1

COPY requirements.txt .
RUN pip install -r requirements.txt
