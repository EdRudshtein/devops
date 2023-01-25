& './../envs.ps1'

docker run -d --name devops_fastapi -p 8080:8080 "edrudshtein/devops_fastapi:$env:DEVOPS_FASTAPI_VERSION"
