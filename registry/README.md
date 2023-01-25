# Private Docker Registry

## Prepare the Server
ensure port 5000 is open

## Generating certificate / key pair for the private Docker registry
on the server machine

do all as root
```
mkdir /certs
```
Copy below content to __/certs/openssl.conf__

`<dockerIP>` is the IP address of your server running the registry (ex. 10.0.0.230)

```
[ req ]
distinguished_name  = req_distinguished_name
x509_extensions     = req_ext
default_md          = sha256
prompt              = no
encrypt_key         = no

[ req_distinguished_name ]
countryName             = "US"
localityName            = "FL"
organizationName        = "MyCompany"
organizationalUnitName  = "MyUnit"
commonName              = "rudshtein.local"
emailAddress            = "test@rudshtein.local"

[ req_ext ]
subjectAltName  = @alt_names

[ alt_names ]
DNS = "rudshtein.local"

```
Generate the certificate and private key
```
openssl req \
 -x509 -newkey rsa:4096 -days 365 -config /certs/openssl.conf \
 -keyout /certs/domain.key -out /certs/domain.crt
```
to verify your certificate
```
openssl x509 -text -noout -in /certs/domain.crt
```

## Start the Registry

copy one of the dc-* (ex dc-TLS-with-no-auth.yaml) file to the server and rename to __docker-compose.yaml__

### start the registry
```shell
docker compose up -d
```

### (when needed) stop the registry
```shell
docker compose down
```

# Update the Clients

on each client
1. configure DNS so that ```rudshtein.local``` points to the server
2. install the previously generated TLS certificate (/certs/domain.crt)
