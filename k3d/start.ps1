#k3d registry create rudshtein.local --port 5000

# start cluster

k3d cluster create cluster1 `
    --servers 1 `
    --agents 3 `
    --image "docker.io/rancher/k3s:v1.25.5-k3s1" `
    --port "9080:80@loadbalancer" `
    --port "9443:443@loadbalancer" `
    --network firmwide `
    --volume "$env:DOCKERVOLUMES_HOME/k3d/volumes:/volumes" `
    --k3s-node-label "server0=true@server:0" `
    --k3s-node-label "agent0=true@agent:0" `
    --kubeconfig-switch-context `
    --timeout 120s `
    --wait
#    --port "5432:5432@loadbalancer" `
#    --port "31000-31005:31000-31005@loadbalancer" `
#    --registry-use k3d-rudshtein.local:5000 `

#kubectl apply -f pv.yaml
