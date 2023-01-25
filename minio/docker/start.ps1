docker run -d `
--name minio `
-p 9000:9000 `
-p 9001:9001 `
--env "MINIO_ROOT_USER=admin" `
--env "MINIO_ROOT_PASSWORD=adminpassword" `
--volume "minio-data:/data" `
minio/minio:RELEASE.2022-07-08T00-05-23Z server /data --console-address ":9001"
