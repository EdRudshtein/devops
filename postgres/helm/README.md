# install

```
helm install postgresql-test bitnami/postgresql `
--set auth.enablePostgresUser=True `
--set auth.postgresPassword=postgres
```

--set "global.postgresql.auth.username=postgres" `
--set "global.postgresql.auth.password=postgres" `
--set "global.postgresql.auth.database=temp"
#--set "volumePermissions.enabled=true" `
#--set "persistence.existingClaim=postgres-pvc"

```
$POSTGRES_PASSWORD=$(kubectl get secret --namespace default postgresql-test -o jsonpath="{.data.postgres-password}" | base64 -d)
echo "$POSTGRES_PASSWORD"
```

```
kubectl run postgresql-test-client --rm --tty -i `
--restart='Never' `
--namespace default `
--image docker.io/bitnami/postgresql:14.3.0-debian-11-r3 `
--env="PGPASSWORD=$POSTGRES_PASSWORD" `
--command -- "psql --host postgresql-test -U postgres -d postgres -p 5432"
```
