# MinIO Helm Installation

## Install
### Add bitnami repo
```
helm repo add bitnami https://charts.bitnami.com/bitnami
```

### Add bitnami repo
```
helm install `
--namespace admin `
--set auth.rootUser="minioadmin",auth.rootPassword="minioadmin" `
-f values.yaml `
minio bitnami/minio
```


## Update
```
helm upgrade -f values.yaml minio bitnami/minio
```

## debug access
```
kubectl port-forward --namespace default svc/minio 9001:9001
http://127.0.0.1:9001/minio
```

## Deleta
```
helm delete my-minio
```
