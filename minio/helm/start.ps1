#kubectl apply -f minio-pvc.yaml

helm upgrade --install --values values.yaml --namespace minio --create-namespace --set accessKey=myaccesskey,secretKey=mysecretkey minio minio/minio

#helm install minio --values values.yaml --set accessKey=myaccesskey,secretKey=mysecretkey  minio/minio
