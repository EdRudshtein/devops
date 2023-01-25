import configparser
# import io
import os

from botocore.exceptions import ClientError
import boto3
import pytest
from mypy_boto3_s3.service_resource import S3ServiceResource
from mypy_boto3_s3.client import S3Client

config=configparser.ConfigParser()
config.read('c:\\secrets\\config.ini')  # DEV only; in PROD, HashiCorp Vault
access_key_id=config['minio']['access_key_id']
secret_access_key=config['minio']['secret_access_key']


# MINIO_URL='l208:9000'


@pytest.fixture
def s3_resource() -> S3ServiceResource:
	result=boto3.resource('s3',
	                      endpoint_url=f'http://localhost:9000',
	                      aws_access_key_id=access_key_id,
	                      aws_secret_access_key=secret_access_key,
	                      aws_session_token=None,
	                      verify=False)
	return result


@pytest.fixture
def s3_client() -> S3Client:
	result=boto3.client('s3',
	                    endpoint_url=f'http://localhost:9000',
	                    aws_access_key_id=access_key_id,
	                    aws_secret_access_key=secret_access_key,
	                    aws_session_token=None,
	                    verify=False)
	return result


@pytest.fixture
def bucket_name() -> str:
	return "main"


def object_in_S3(s3: S3ServiceResource,bucket_name: str,key: str) -> bool:
	try:
		s3.Object(bucket_name,key).load()
	except ClientError as e:
		if e.response['Error']['Code']=="404":
			return False
		else:
			raise
	return True


def test_upload_file(s3_resource,bucket_name: str) -> None:
	object_name="a.txt"
	if object_in_S3(s3_resource,bucket_name,object_name):
		s3_resource.Object(bucket_name,object_name).delete()
	assert not object_in_S3(s3_resource,bucket_name,object_name)
	bucket=s3_resource.Bucket(bucket_name)
	file_name=os.path.join('c:/temp',object_name)
	bucket.upload_file(file_name,object_name)
	result=object_in_S3(s3_resource,bucket_name,object_name)
	if result:
		s3_resource.Object(bucket_name,object_name).delete()
	assert result
