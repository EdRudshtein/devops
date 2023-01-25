# CREATE A PRODUCTION KUBERNETES CLUSTER

## Prerequisites
* static IPs on each host
* swap is disabled on each host
* root access (all instructions assume running as `root`)

## Install `containerd` and Kubernetes utilities (do on each Node)
### install `containerd`

install `containerd` prerequisites (see 
https://kubernetes.io/docs/setup/production-environment/container-runtimes/
for updated instruction)
```
cat <<EOF > /etc/modules-load.d/k8s.conf
overlay
br_netfilter
EOF
```
apply
```
modprobe overlay
modprobe br_netfilter
```

set required `sysctl` parameters; set to persist across reboots
```
cat <<EOF > /etc/sysctl.d/k8s.conf
net.bridge.bridge-nf-call-iptables  = 1
net.bridge.bridge-nf-call-ip6tables = 1
net.ipv4.ip_forward                 = 1
EOF
```

apply `sysctl` params
```
sysctl --system
```

install and mark `containerd`
```
apt update 
apt install -y containerd
```

hold `containerd`
```
apt-mark hold containerd
```

create a `containerd` configuration file
```
mkdir -p /etc/containerd
containerd config default > /etc/containerd/config.toml
```

set the `cgroup` driver for `containerd` to `systemd` (see https://github.com/containerd/cri/blob/master/docs/config.md and https://github.com/containerd/containerd/blob/master/docs/ops.md)

```
# change SystemdCgroup = false to SystemdCgroup = true
sed -i 's/SystemdCgroup = false/SystemdCgroup = true/' /etc/containerd/config.toml
```

verify the change was made
```
more /etc/containerd/config.toml
```

restart 'containerd', ensure set to start on system start, check status
```
systemctl restart containerd.service
systemctl enable containerd.service
systemctl status containerd.service
```


### Install `kubelet`, `kubeadm` and `kubectl`

add Google's apt repository gpg key
```
curl -fsSLo /usr/share/keyrings/kubernetes-archive-keyring.gpg https://packages.cloud.google.com/apt/doc/apt-key.gpg
```

add the kubernetes apt repository
```
echo "deb [signed-by=/usr/share/keyrings/kubernetes-archive-keyring.gpg] https://apt.kubernetes.io/ kubernetes-xenial main" > /etc/apt/sources.list.d/kubernetes.list
```

update the package list and use apt-cache policy to inspect versions available in the repository
```
apt update
apt-cache policy kubelet | head -n 20 
```

install `kubelet` (may specify version)
```
VERSION=1.25.5-00
apt install -y kubelet=$VERSION kubeadm=$VERSION kubectl=$VERSION
```

hold `kubelet`, `kubeadm` and `kubectl`
```
apt-mark hold kubelet kubeadm kubectl
```

restart 'kubelet', ensure set to start on system start, check status
```
systemctl restart kubelet.service
systemctl enable kubelet.service
systemctl status kubelet.service
```

## Create the Control Plane (only on Control Plane Node)

### install the network
download the yaml manifest for the pod network
```
wget https://docs.projectcalico.org/manifests/calico.yaml
```

optionally adjust Pod Network IP address range CALICO_IPV4POOL_CIDR
1. examine Pod Network IP address range CALICO_IPV4POOL_CIDR in `calico.yaml`
2. adjust if needed for your infrastructure to ensure that the Pod network IP range doesn't overlap with other networks in the infrastructure
```
vi calico.yaml
```

### install the cluster

use `kubeadm init` to bootstrap the cluster
```
#remove the kubernetes-version parameter to use the latest
kubeadm init --kubernetes-version v1.25.5
```


update permission of `/etc/kubernetes/admin.conf` so all users can 
clone when setting up their environment
```
chmod a+r /etc/kubernetes/admin.conf
```

initialize `kubectl` config file for `root`
```
mkdir -p $HOME/.kube
cp -i /etc/kubernetes/admin.conf $HOME/.kube/config
chown root:root $HOME/.kube/config
```

optionally initialize `kubectl` config file for some user `egr`
```
su egr
mkdir -p $HOME/.kube
cp -i /etc/kubernetes/admin.conf $HOME/.kube/config
chown $(id -u):$(id -g) $HOME/.kube/config
```

create the Pod network
```
kubectl apply -f calico.yaml
```

ensure that all system pods and calico pods change to Running
#The DNS pod won't start (pending) until the Pod network is deployed and Running.
```
kubectl get pods --all-namespaces --watch
```

ensure all Nodes are 'Ready'
```
kubectl get nodes 
```

### run high-level check of Control Plane Node
validate that `containerd` and `kubelet` services are now properly running (not crashlooping)
```
systemctl status containerd.service
systemctl status kubelet.service
```

examine the directory where the kubeconfig files live
```
ls -al /etc/kubernetes
```

examine the manifests directory
```
ls -al /etc/kubernetes/manifests
```

examine the `API Server` manifest
```
more /etc/kubernetes/manifests/kube-apiserver.yaml
```

examine the `etcd` manifests
```
more /etc/kubernetes/manifests/etcd.yaml
```

## Create / Attach Worker Node

### run prerequisites
if not yet done, run steps -> [Install `containerd` and Kubernetes utilities]

### join the cluster

on the Control Plane Node ("CPN"), list all tokens
```
kubeadm token list
```

on the Control Plane Node, find the CA cert hash
```
openssl x509 -pubkey -in /etc/kubernetes/pki/ca.crt | openssl rsa -pubin -outform der 2>/dev/null | openssl dgst -sha256 -hex | sed 's/^.* //'
```

on the Control Plane Node, if you need to generate a new token (old one timed out/expired. etc.); 
copy the join command if expect to attach a new worker node
```
kubeadm token create --print-join-command
```

as 'root', on the prospective Worker Node, either execute the copied join command, or
```
# kubeadm join <CPN IP>:<CPN port> --token <token> --discovery-token-ca-cert-hash <hash> 
kubeadm join 172.16.94.10:6443 \
    --token 2yij0q.256jwadksuvxprp8 \
    --discovery-token-ca-cert-hash sha256:bd0763f650e65bc211c02f39d6e1e6a5ea92423728df7034b8747dc0086d6c8a 
```

### validate

on the CPN, check that all Node's status as 'Ready'
```
kubectl get nodes -o wide
```

on the CPN, watch for all Pods to change to 'Running' on the newly added nodes
```
kubectl get pods -A -w
```

## Configure NFS (used by StorageClass)
### install NFS Server on non-clusted host `n215` (do all as `root`)

install the NFS Server
```
apt update && apt install -y nfs-kernel-server && apt upgrade -y
```

create the NFS share
```
mkdir /shared-k8s
chown nobody:nogroup /shared-k8s
chmod -R 777 /shared-k8s
```

configure to make share permanent
```
echo "/shared-k8s  *(rw,no_root_squash,no_subtree_check)" >> /etc/exports
```

restart / verify the NFS Sevice
```
systemctl restart nfs-kernel-server.service
systemctl status nfs-kernel-server.service
```
open proper `ufw` ports
```
ufw allow from <IP>/24 to any port nfs
ufw reload
ufw status
```
### install NFS Client on each cluster node (do all as `root`)
install the NFS Client
```
apt update && apt install -y nfs-common && apt upgrade -y
```
test by temporary mount
```
mount -t nfs4 n215:/shared-k8s /mnt
mount | grep nfs4
sudo umount /mnt
```
