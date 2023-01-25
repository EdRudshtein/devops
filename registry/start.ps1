# create network
docker network create firmwide

# create registry
docker run -d `
    -p 5000:5000 `
    --restart always `
    --name rudshtein.local `
    --network firmwide `
    -v "$env:DOCKERVOLUMES/registry:/var/lib/registry" `
    -e "REGISTRY_STORAGE_DELETE_ENABLED=true" `
    registry:2.8.1

