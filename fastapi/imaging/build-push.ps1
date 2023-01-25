# param([string]$version)
# if ( [string]::IsNullOrEmpty($version))
# {
#     Write-Host "Error - Need to supply version"
#     return
# }
#
# Write-Host "building / pushing version $version"

& './../envs.ps1'

docker build -t "edrudshtein/devops_fastapi:$env:DEVOPS_FASTAPI_VERSION" .
docker push "edrudshtein/devops_fastapi:$env:DEVOPS_FASTAPI_VERSION"
