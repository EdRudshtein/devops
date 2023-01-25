# <u>Kubernetes Production Cluster Setup</u>

# Prerequisites 
* Ubuntu 18.04 or later
* either
* * DNS set-up OR
* * static IPs on individual server and /etc/hosts properly configured on each server
* swap disabled on each server


# On All Nodes

## log in as `root` or use `sudo` in below if not root
````
sudo su
````

## install / configure `containerd`

preliminary instation
```
modprobe overlay
modprobe br_netfilter
```
```
cat <<EOF | sudo tee /etc/modules-load.d/k8s.conf
overlay
br_netfilter
EOF

```

`sysctl` params required by setup; ensure params persist across reboots
````
cat <<EOF | sudo tee /etc/sysctl.d/k8s.conf
net.bridge.bridge-nf-call-iptables  = 1
net.bridge.bridge-nf-call-ip6tables = 1
net.ipv4.ip_forward                 = 1
EOF
````

apply the `sysctl` params
````
sysctl --system
````

ensure that `br_netfilter` and `overlay` modules are loaded:
````
lsmod | grep br_netfilter
````
````
lsmod | grep overlay
````

verify that `net.bridge.bridge-nf-call-iptables`, `net.bridge.bridge-nf-call-ip6tables` and `net.ipv4.ip_forward` system variables are set to 1
in the `sysctl` config
````
sysctl net.bridge.bridge-nf-call-iptables net.bridge.bridge-nf-call-ip6tables net.ipv4.ip_forward
````

install `containerd`
````
apt update && apt install -y containerd
````

create a `containerd` configuration file
````
mkdir -p /etc/containerd &&
containerd config default | sudo tee /etc/containerd/config.toml
````

set the `cgroup` driver for `containerd` to `systemd` which is required for the kubelet;
modify the `/etc/containerd/config.toml` file to set `SystemdCgroup = true`
````
sed -i 's/SystemdCgroup = false/SystemdCgroup = true/' /etc/containerd/config.toml
````

verify the change was made
````
nano /etc/containerd/config.toml
````

restart containerd with the new configuration
````
systemctl restart containerd
````




## install / configure `kubeadm`, `kubelet` and `kubectl`

add the Google's apt repository gpg key
````
curl -fsSLo /usr/share/keyrings/kubernetes-archive-keyring.gpg https://packages.cloud.google.com/apt/doc/apt-key.gpg
````

add the Kubernetes apt repository
````
echo "deb [signed-by=/usr/share/keyrings/kubernetes-archive-keyring.gpg] https://apt.kubernetes.io/ kubernetes-xenial main" | tee /etc/apt/sources.list.d/kubernetes.list
````

update the package list and use apt-cache policy to inspect versions available in the repository
````
apt update
apt-cache policy kubelet | head -n 20 
````

install the required packages and disable apt management of these packages
````
VERSION=1.24.3-00
apt install -y kubelet=$VERSION kubeadm=$VERSION kubectl=$VERSION
apt-mark hold kubelet kubeadm kubectl containerd
````

ensure both services are set to start on system start-up
````
systemctl enable kubelet.service
systemctl enable containerd.service
````

check the status of our kubelet and our container runtime (note: the kubelet will be in "crashloop" until either a cluster is created or the node is joined to an existing cluster)
````
systemctl status kubelet.service 
systemctl status containerd.service 
````




# Bootstrap the Master Node
## log in as `root` or use `sudo` in below if not root
````
sudo su
````

## create the control plane node

only on the Control Plane Node, download the yaml files for the pod network
````
wget https://docs.projectcalico.org/manifests/calico.yaml
````

look inside `calico.yaml` and find the setting for Pod Network IP address range `CALICO_IPV4POOL_CIDR`, adjust if needed for your infrastructure to ensure that the Pod network IP  range doesn't overlap with other networks in our infrastructure.
````
nano calico.yaml
````

bootstrap the cluster
````
kubeadm init
````

create the `kubeconfig` file for user `egr`
````
su egr &&
mkdir -p $HOME/.kube &&
sudo cp -i /etc/kubernetes/admin.conf $HOME/.kube/config &&
sudo chown egr:egr $HOME/.kube/config &&
su &&
````

## deploy the Pod Network
```
kubectl apply -f calico.yaml
```

## examine / validate
look for the all the system pods and calico pods to change to Running;
note that the DNS pod won't start (will be pending) until the Pod network is 
deployed and Running;
at the end, all system pods should be Running
```
kubectl get pods --all-namespaces --watch
```

get a list of our current nodes; the Control Plane Node should be ready
```
kubectl get nodes 
```
check out the systemd unit...it's no longer crashlooping because it has static pods to start
#Remember the kubelet starts the static pods, and thus the control plane pods
```
systemctl status kubelet.service 
```

check the static pod manifests on the Control Plane Node
```
ls /etc/kubernetes/manifests
```

look more closely at API server and etcd's manifest
```
more /etc/kubernetes/manifests/etcd.yaml
more /etc/kubernetes/manifests/kube-apiserver.yaml
```

Check out the directory where the kubeconfig files live for each of the control plane pods
```
ls /etc/kubernetes
```
