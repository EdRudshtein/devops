#/usr/bin/pwsh

#kubectl delete -f postgres-pv.yaml

kubectl apply -f postgres-pv.yaml


helm install -f values.yaml postgres bitnami/postgresql
#    --set "auth.postgresPassword=postgres"




#    --set "global.postgresql.postgresqlUsername=postgres" `
#    --set "global.postgresql.postgresqlPassword=postgres" `
#    --set "global.postgresql.postgresqlDatabase=temp"
#--set "volumePermissions.enabled=true" `
#--set "persistence.existingClaim=postgres-pvc"

#helm install postgresql-test01 bitnami/postgresql
#--set global.postgresql.servicePort=5555

#$POSTGRES_PASSWORD = $( kubectl get secret --namespace default postgresql-test -o jsonpath = "{.data.postgres-password}" | base64 -d )
#
#kubectl run postgresql-test-client --rm --tty -i `
#--restart = 'Never' `
#--namespace default `
#--image docker.io/bitnami/postgresql:14.3.0-debian-11-r3 `
#--env = "PGPASSWORD=postgres" `
#--command -- "psql --host postgresql-test -U postgres -d postgres -p 5432"
