kubectl apply  -f postgres-pv.yaml
kubectl apply  -f postgres-pvc.yaml
kubectl apply  -f postgres-configmap.yaml
kubectl apply  -f postgres-deployment.yaml
kubectl apply  -f postgres-service.yaml
