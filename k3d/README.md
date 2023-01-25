# k3d Cluster Administration

[Create](start.ps1) local kubernetes (k3s) cluster 'cluster1'

[Delete](stop.ps1) local kubernetes (k3s) cluster 'cluster1'

## get initial cluster information
```
k3d cluster ls
k3d registry ls
```

## (OPTiONAL) if needed, create local docker registry
```
k3d registry create rudshtein.local --port 6400
k3d registry ls
```

### list repositories / images in the local docker registry
```
curl -X GET http://k3d-rudshtein.local:6400/v2/_catalog
```


## create / start cluster
See https://k3d.io/v5.4.3/usage/commands/k3d_cluster_create/ for details.

### command (Pseudo)

```
k3d cluster create <clustername> `
[ [--servers|-s] <nservers>] `
[ [--agents|-a] <nagents>] `
[ [--port|-p] "<hostport80>:80@loadbalancer"] `
[ [--port|-p] "<hostport443>:443@loadbalancer"] `
[ [--volume|-v] <hostvolume>:<nodevolume>] `
[--registry-use k3d-<localregistryname>:<localregistryport>] ` 
[--network <networkname>] `
[ [--image|-i] <image>]
```

### example (PowerShell)

## create a multinode kubernetes cluster with local container registry 
```
k3d cluster create cluster1 `
--servers 1 `
--agents 3 `
--port "9080:80@loadbalancer" `
--port "9443:443@loadbalancer" `
--registry-use "k3d-rudshtein.local:6400" `
--image "docker.io/rancher/k3s:v1.22.11-k3s1-amd64"
```
### validate
```
k3d version
```
```
k3d node list
```
```
kubectl version
```
```
kubectl cluster-info
```

# Delete
## delete cluster

### command (pseudo code)

```
k3d cluster rm <clustername>
```

### example

```
k3d cluster rm cluster1
```

## delete registry
### command (pseudo code)
```
k3d registry rm k3d-<registryname>
```
### example
```
k3d registry rm k3d-rudshtein.local
```

## As of k3d v4.0.0 (January 2021), for <ins>single-node</ins> clusters, config file can be used

TODO