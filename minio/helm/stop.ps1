helm delete minio -n minio
kubectl delete -f minio-pvc.yaml
#kubectl delete -f minio-pv.yaml
